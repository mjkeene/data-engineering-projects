<h2>Chapter 7: Transforming Data to Optimize for Analytics</h2>

* <b>Transforming data for analytics</b> enables an organization to efficiently gain new insights into their data.
  * This is one of the key tasks for a data engineer.
  * Some transformations are common and can be generically applied to a dataset (e.g., converting from raw files to 
    Parquet format).
  * Other transformations use business logic and vary based on contents of the data and specific requirements.
* We'll cover some of the engines that are available in AWS for performing data transformations.

<h3>How transformations can create value</h3>

* Data can be one of the most valuable assets that an organization owns.
  * However, raw, siloed data has limited value on its own, and we unlock the value of an organization's data when 
    we combine various raw datasets and transform that data through an analytics pipeline.
  * Think of it like the following ingredients:
    * sugar
    * butter
    * milk
    * eggs
  * On their own, some aren't that great (imagine eating a stick of butter). When combined, you can make something 
    entirely different, like a cake. 
  * If you combine in the right way, you can create something totally new and different. The same is true with 
    datasets.


<h3>Types of data transformation tools</h3>

<b>Apache Spark</b>

* Apache Spark is an in-memory engine for working with large datasets, providing a mechanism to split a dataset 
  among multiple nodes in a cluster for efficient processing.
* It's very popular, and there are multiple ways to run Spark jobs within AWS.
* You can process both batch data (such as a daily basis or every few hours) and near real-time streaming data using 
  <b>Spark Streaming</b>.
* You can also use <b>Spark SQL</b> to process data using standard SQL, and <b>Spark ML</b> for applying machine 
  learning techniques to your data.
* There's also <b>Spark GraphX</b> which can work with highly interconnected points of data to analyze complex 
  relationships, such as for social networking applications.
* There are multiple services for running Spark jobs on AWS:
  * AWS Glue provides a serverless way to run Spark
  * Elastic MapReduce (EMR) provides both a managed service for deploying a cluster for running Spark as well as a 
    serverless option.
  * You can also use AWS container services like Elastic Container Service (ECS) or Elastic Kubernetes Service (EKS) 
    to run a Spark engine in a containerized environment or use a managed service from a partner service, like 
    <b>Databricks</b>.

<b>Hadoop and MapReduce</b>

* Before Apache Spark, tools within the Hadoop framework -- such as Hive and MapReduce -- were the most popular way 
  to transform and process large datasets.
* Hadoop MapReduce is used in a similar way to Apache Spark, with the biggest difference being that Apache Spark 
  does all processing in memory. Hadoop MapReduce makes extensive use of traditional disk-based reads and writes to 
  interim storage during processing
  * For massive datasets that cannot be economically processed in memory, MapReduce may be better suited.
  * However, for most use cases, Spark provides significant performance benefits, as well as the ability to handle 
    streaming data, access to machine learning libraries, and an API for graph computation with GraphX.
  * Spark has become the leading big data processing solution in recent years, but there are still many legacy 
    Hadoop systems being used.
* Note that there are still some components of Hadoop that are still commonly used in Spark processing.
  * The Apache Hive metadata store (Data Catalog) is used by Spark to map databases and tables to physical files in 
    storage. The AWS Glue Catalog is an Apache Hive-compatible metastore.


<b>SQL</b>

* <b>Structured Query Language (SQL)</b> is a very common method for data transformation.
* SQL knowledge and experience is widely available.
* A code-based approach to transformations (such as Spark) can be a more powerful and versatile way of performing 
  transformations than SQL though.
* If you're in an environment with a heavy focus on SQL, and SQL skill sets being widely available and other skill 
  sets being limited, then using SQL for transformations may make sense.
* If you're in an environment with complex data processing requirements, and where latency and throughput 
  requirements are high, it may be worthwhile to invest in upskilling to use a modern data processing approach like 
  Spark.
* If the target for your data transformations is a data warehousing system, such as <b>AWS Redshift</b> or 
  <b>Snowflake</b>, then an ELT approach may be used, where raw data is loaded into the data warehouse, and then the 
  transformation of data is performed within the data warehouse using SQL.
* Spark can be used through Spark SQL.
  * This allows the use of SQL for transformations while using a modern data processing engine to perform the 
    transformations, rather than using a data warehouse.
  * This allows the data warehouse to be focused on responding to end-user queries, while data transformation jobs 
    are offloaded to an Apache Spark cluster. 
  * This is an ETL approach where data is extracted into intermediate storage, Spark is used to transform the data, 
    and the data is then loaded into a different zone of the data lake, or into a data warehouse.
* Tools like <b>AWS Glue Studio</b> provide a visual interface that can be used to design ETL jobs, including jobs 
  that use SQL statements to perform complex transformations.
  * This helps to run SQL-based transformations using the power of the Apache Spark engine, without having specific 
    Spark coding skills.

<b>GUI-based tools</b>

* Drag-and-drop type approach to creating complex transformation pipelines
* These make ETL-type transformations accessible to those without advanced coding skills
* Some tools can generate transformation code (like Apache Spark code), providing a good starting point for a user 
  to further develop the code.
* <b>AWS Glue DataBrew</b> is designed as a visual data preparation tool, enabling you to easily apply 
  transformations to a set of files.
* <b>AWS Glue Studio</b> also provides a visual interface for developing Spark transformations.
  * <b>This is good starting point for those trying to learn Spark. It also helps to develop custom transforms by 
    giving you some code to work with upfront.</b>
* Outside of AWS, there are many commercial products that provide a visual approach to ETL design, such as 
  Informatica, Matillion, Stitch, Talend, Panoply, Fivetran, and many others.

<h3>Common data preparation transformations</h3>

* These transformations are designed to apply relatively generic optimizations to individual datasets that we are 
  ingesting into a data lake.
* For these, you may need some understanding of the source system and context, but you generally do not need to 
  understand the ultimate business use case or specifics for the dataset.

<b>Protecting PII data</b>

* Datasets with <b>personally identifiable information (PII)</b> data may have governance restrictions on which PII 
  data can be stored in the data lake.
  * We need a process to protect PII data as soon as possible after it is ingested.
* Common approaches with PII data: tokenization or hashing, each with its own advantages and disadvantages (see 
  chapter 4 for more details there).
  * The purpose is to remove the PII data from the raw data and replace it with a value, or token, in a way that 
    enables us to still use the data for analytics.
* This transformation is often done in a specific zone of the data lake designed specifically for handling PII data.
  * This zone has strict access controls
  * Best practice is to have the anonymizing process run in a totally separate AWS account.
* AWS Glue DataBrew provides many options for obfuscating data -- redact, replace/swap data, encrypt, or hash the 
  PII values.

<b>Optimizing the file format</b>

* For analytics, the most popular file format is <b>Apache Parquet</b>.
* Parquet files are column-based, meaning that the contents of the file are physically stored to have data grouped 
  by columns, rather than grouped by rows as with most file formats (e.g., CSV files).
  * As a result, queries that select a set of specific columns (rather than the entire row) do not need to read 
    through all the data in the Parquet file to return a result, leading to performance improvements.
* Parquet files contain store metadata about the data they store:
  * Schema information (data type for each column)
  * Statistics like the min and max value for each column
  * Number of rows in the file, etc.
* Another benefit of Parquet files is that they are optimized for compression.
  * A 1TB dataset in CSV format could potentially be ~130GB in Parquet format once compressed. Parquet supports 
    multiple compression algorithms, with <b>Snappy</b> being the most widely used.
* <b>These optimizations result in significant savings for both storage space used, and increased performance when 
  running queries.</b>
  * As a concrete example, Athena queries cost $5 per TB of scanned data. If only certain columns are queried of a 
    Parquet file, and it is compressed, significantly less data needs to be scanned to resolve the query.
* If your data is stored across hundreds of Parquet files in a data lake, the analytics engine is able to get 
  further performance advantages by reading the metadata of the files.
  * <b>Example: if your query just counts all the rows in a table, this information is stored in the Parquet file 
    metadata, so the query doesn't need to actually scan any of the data.</b>
  * Athena scans 0KB of the data, so there is actually no cost to run this query.
  * Another example: if your query is for where the sales amount is above a specific value, the analytics engine can 
    read the metadata for a column to determine the min and max values stored in the specific data chunk. It can 
    avoid scanning irrelevant data this way. Cost savings for query, and increased performance.
* Because of these benefits, it is a very common transformation to convert incoming files from things like JSON, CSV,
  XML, etc. into the analytics-optimized Parquet format.

<b>Optimizing with data partitioning</b>

* 

Leaving off on p. 213