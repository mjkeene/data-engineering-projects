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

<h3>Ingesting streaming data</h3>

* 

