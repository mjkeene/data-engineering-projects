<h2>Ingesting data with AWS DMS & Streaming data with Kinesis Firehose</h2>

<h3>Ingesting data with AWS DMS</h3>

* AWS DMS can be used to replicate a database into an S3-based data lake (among other uses).
* We'll deploy a cfn template (`mysql-ec2loader.cfn`) to configure a MySQL RDS instance and then deploy an EC2 
  instance to load a demo database into MySQL.
* Next, we'll set up a DMS replication instance and configure endpoints and tasks; run the instance in full-load 
  mode; run a Glue crawler to add the tables that were newly added into the AWS Glue Data Catalog; query this data 
  with Athena.

<h3>Deploying MySQL and an EC2 data loader via CloudFormation</h3>

* CloudFormation is a service that allows you to deploy infrastructure as code. Using cfn templates provides the 
  ability to deploy AWS services using either JSON or YAML formatted templates.
  * You can treat your infrastructure as code, meaning you can store the templates in a version control system.
  * You can manage changes to templates and integrate code reviews, as well as easily deploying infrastructure 
    reliably and repeatably via CI/CD pipelines.

* The CloudFormation template `mysql-ec2loader.cfn` does the following:
  1. Request that the user provides a password (`DBPassword`) that will be the admin password for the MySQL instance.
  2. Set a parameter (`LatestAmiId`) that provides a path to the AWS Secrets Manager entry that contains the Amazon 
     Machine Image (AMI) ID for deploying an instance with AL23.
  3. Create RDS MySQL instance (`MySQLInstance`) with 20GB of allocated storage, using the `db.t3.micro` instance type.
  4. Create an EC2 instance `EC2Instance` of type `t3.micro`. The `DependsOn` option specifies that the MySQL 
     instance resource must be created prior to this resource being created.

<h3>Create an IAM policy and role for DMS</h3>

* Create an IAM policy and role that will allow DMS to write to our target S3 bucket (`iam_policy_dms.json`)
* This policy grants permissions for all S3 operations (get, put, etc.) for the `dataeng-landing-zone-mjk25` bucket 
  to give DMS permissions needed to write out CSV files in the landing zone bucket with the data from the MySQL 
  database.
* Attach that policy to a new role for DMS `DataEngDMSLandingS3BucketRole`, take note of the ARN which will be 
  required later.
`arn:aws:iam::841162706900:role/DataEngDMSLandingS3BucketRole`

<h3>Configuring DMS settings and performing a full load from MySQL to S3</h3>

* Here we will create a DMS replication instance (a managed EC2 instance that connects to the source endpoint, 
  retrieves data, and writes to the target endpoint). We'll also configure the source and target endpoints.
* Next, we'll create a database migration task that provides configuration settings for the migration. The 
  CloudFormation template must be completely deployed before doing these steps.

* In the DMS service console, create a Replication Instance `mysql-s3-replication`.
* Next, create an endpoint -- this will be a source endpoint of type RDS DB Instance. Select the MySQL database that 
  was created by the cfn template.
* Now that we have created the source endpoint, we can create the target endpoint by clicking on Create endpoint again.
  * This will be a Target endpoint, named `s3-landing-zone-sakila-csv`.
  * The Target engine is S3.
  * The bucket name will be `dataeng-landing-zone-mjk25`.

* Now we will create a Database migration task, naming it `dataeng-mysql-s3-sakila-task`.
  * The Replication instance is `mysql-s3-replication`
  * The source database endpoint is the MySQL instance
  * The target database endpoint is the s3 target endpoint
  * This will be a one-time migration


* Once this task is created, the full load will be automatically initiated and the data will be loaded from the 
  MySQL instance to S3. Click on the task identifier and review the Table statistics tab to monitor your progress.

* We can now query this data with Athena; select the sakila database and sample some data from the tables:

```sql
SELECT *
FROM film_text
LIMIT 20;
```

* We have successfully used S3 as a target for AWS Database Migration Service, and used a MySQL-compatible database 
  as a source for DMS.


* Make sure to delete the DMS replication instance and resources deployed by cfn template.

---

---
<h3>Ingesting streaming data</h3>

* AWS provides an open source solution for streaming sample data into Kinesis; we will use the Kinesis service to 
  ingest streaming data.
  * To generate the data, we'll use Kinesis Data Generator (KDG)
* High-level, we will complete the following tasks:
1. Configure <b>Kinesis Data Firehose</b> to ingest streaming data, and write the data out to S3.
2. Configure <b>KDG</b> to create mock streaming data.

* Let's configure the Kinesis Data Firehose instance first.
* Create a delivery stream named `dataeng-firehose-streaming-s3`
  * We'll leave the optional <b>Transform and convert records</b> unchecked. <b>Transform source records with AWS 
    Lambda</b> functionality can be used to run data validation tasks or perform light processing on incoming data 
    with AWS Lambda, but we don't want to do any processing here.
  * <b>Convert record format</b> can be used to convert incoming data into Apache Parquet or Apache ORC format. We'd 
    need to specify the schema of the incoming data upfront to do this though.
* By default, Kinesis Data Firehose writes the data to S3 with a prefix to split incoming data by `YYYY/MM/dd/HH`. 
  We want to load streaming data into a "streaming" prefix, and only want the data split by the year and month it 
  was ingested. Set the S3 bucket prefix to `streaming/!{timestamp:yyyy/MM/}`. 
  * We must now also set a custom error prefix since we set a custom prefix for incoming data. Set this to
     `!{firehose:error-output-type}/!{timestamp:yyyy/ MM/}`


* <b>The S3 buffer conditions allow us to control the parameters for how long Kinesis buffers incoming data before 
  writing it out to our target. We specify both a buffer size (in MB), and a buffer interval (in seconds), and 
  whichever is reached first will trigger Kinesis to write to the target.</b>


* Set the Buffer size to 1MB and Buffer interval to 60 seconds.

<h3>Configuring the Kinesis Data Generator (KDG)</h3>

* We will simulate data with KDG that includes:
  * streaming timestamp
  * rented, purchased, or watched the trailer
  * `film_id` that matches the Sakila film database (we'll later join these datasets)
  * distribution partner's name
  * streaming platform
  * state the movie was streamed in

* To use KDG, you need an Amazon Cognito user in your AWS account, an then use that user to log into KDG on the 
  GitHub account.
* https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html
* Follow the instructions on this link, and then enter the `record_template_kinesis_data_generator.json` for the 
  record template.
* Specify 20 records per second, and leave it running for 5-10 mins to get ~10,000 records. I stopped at 10,420 
  records.

<h3>Adding newly ingested data to the Glue Data Catalog</h3>

* Run a <b>Glue crawler</b> to examine the newly ingested data, infer the schema, and automatically add the data to 
  the Glue Data Catalog.
  * Once we do this, we can query the newly ingested data using services such as <b>Amazon Athena</b>.
* Navigate to the Glue console, create a new crawler.
  * Name it `dataeng-streaming-crawler`
  * Add the data source as the streaming s3 bucket: `s3://dataeng-landing-zone-mjk25/streaming/`
    * Make sure to include the trailing slash
  * Add a new database, `streaming_db`
* Run the crawler. When it finishes, there will be a table for the newly ingested streaming data.

<h3>Querying the data with Athena</h3>

* You can see the data coming in at near real-time. I ran the below query every 60-90 seconds, and the results 
  show the growing row count in the table, as well as the more recent timestamps. 

```sql
select count(*), max(timestamp)
from streaming

-- 7520 | 2025-02-09T11:14:16-07:00
-- 8180 | 2025-02-09T11:15:46-07:00
-- 8780 | 2025-02-09T11:16:50-07:00
-- 10420 | 2025-02-09T11:18:26-07:00
```
