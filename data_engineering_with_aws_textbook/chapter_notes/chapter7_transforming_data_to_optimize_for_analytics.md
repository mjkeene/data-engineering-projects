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

* Another common approach for optimizing datasets for analytics is to <b>partition</b> the data, which relates to 
  how the data files are organized in the storage system for a data lake.
* <b>Hive partitioning</b> splits the data from a table to be grouped together in different folders, based on one or 
  more of the columns in the dataset.
  * A common column used is the date.

```
datalake_bucket/year=2023/file1.parquet
datalake_bucket/year=2022/file1.parquet
datalake_bucket/year=2021/file1.parquet
datalake_bucket/year=2020/file1.parquet
```

* If a SQL query is run against this with `WHERE year = 2020`, the analytics engine would only open up the single 
  file in the `datalake_bucket/year=2020/` folder.
* Less data is scanned, so it costs less and completes quicker.

* Note that deciding which column to partition on requires a good understanding of how the dataset will be used. If 
  you partition based on year, but the majority of queries are across all years, then this partitioning strategy 
  would not be effective.
  * Having many partitions can also slow queries that do not utilize them, since the analytics engine needs to read 
    data in all partitions — there is overhead in working between the different folders.
* You can partition across multiple columns to get more granular. Example:

```
datalake_bucket/year=2021/month=6/day=1/file1.parquet
```

* Be careful to not end up with a large number of very small files. The optimal size for each Parquet file in a data 
  lake is between 128MB and 1GB.
  * The Parquet file format can be split, which means that multiple nodes in a cluster can process data from a file 
    in parallel. 
  * However, having lots of small files requires a lot of overhead for opening files, reading metadata, 
    scanning data, and closing each file — all of which can end up significantly impacting performance.
* It is generally better to have fewer partitions with larger files than hundreds or thousands of partitions with 
  small files (e.g., a few MB each).


<b>Data cleansing</b>

* Optimizing the data format and partitioning data are transformation tasks that work on the format and structure of 
  the data, but do not directly transform the data.
  * Cleansing, however, is a transformation that alters parts of the 
    data.
* Some common data transformation tasks for data cleansing:
1. <b>Ensuring consistent column names</b>: Different sources may have the same data with different names (e.g. 
   `date_of_birth` vs. `birthdate`)
2. <b>Changing column data types</b>: It's important that a column has consistent data types for analytics. A column 
   of integers should not include a string, which can cause a query to fail. Cleansing this may consist of replacing 
   the string with a `NULL` value.
3. <b>Ensuring a standard column format</b>: Like the column names, data may have different formats (e.g., 
   `MM-DD-YYYY` vs. `DD-MM-YYYY` for dates). Convert them all to be consistent.
4. <b>Removing duplicate records</b>: Identify, and either flag or remove duplicates.
5. <b>Providing missing values</b>: Various strategies here. Can replace missing values with a valid value (average, 
   median, NULL, etc.). Can also remove any rows that have missing values for specific columns. How to handle this 
   depends on the specific dataset and the ultimate analytics use case.


* The AWS Glue DataBrew service has been designed to provide an easy way to cleanse and normalize data using a 
  visual design tool. It includes over 250 common data cleansing transformations.


<h3>Common business use case transformations</h3>

* In a data lake environment, you ingest raw data from many different source systems into a landing, or raw, zone. 
  You then optimize the file format and partition the dataset, as well as doing any cleansing, potentially moving 
  the data into a "clean" zone. 
* <b>These initial transforms can be done without understanding too much about how the data is ultimately being used by 
  the business.</b>
* Eventually, however, a data engineer will need to use a variety of these ingested data sources to deliver value to 
  the business for a specific use case. After all, the whole point of the data lake is to bring varied data sources 
  from across the business to a central location, to enable new insights to be drawn from across these datasets.
* The transformations discussed below work across multiple datasets to enrich, denormalize, and aggregate the data 
  based on the specific business use case requirements.

<b>Data denormalization</b>

* Source data systems, especially those from relational database systems, are mostly going to be highly normalized. 
  Each table has been designed to contain information about a specific entity or topic, and will then link to other 
  topics with related information through the use of foreign keys.
* Structuring tables this way has write-performance advantages for <b>Online Transaction Processing (OLTP)</b> 
  systems and also helps to ensure the referential integrity of the database.
  * <i>Normalized tables also consume less disk space, since data is not repeated across multiple tables. This was a 
    larger benefit in the early days of databases when storage was limited and expensive, but it is not a 
    significant benefit today with low-cost storage options.</i>
* When it comes to <b>Online Analytical Processing (OLAP)</b> queries, having to join the data across multiple 
  tables does incur a performance hit.
  * Therefore, data is often denormalized for analytics purposes.
  * Within a denormalized table, you often do not have to do any joins to determine details of multiple entities.
* It is important to understand the use case requirements and how the data will be used, and then determine the 
  right table structure for these denormalized tables.
* These denormalization transforms can be done with Apache Spark, GUI-based tools, or SQL. AWS Glue Studio can also 
  be used to design these kinds of table joins using a visual interface.

<b>Enriching data</b>

* Similar to joining tables for denormalization purposes, another common transform is to join tables for the purpose 
  of enriching the original dataset.
* Combining data with more data from third parties, or with data from other parts of the business can increase a 
  dataset's value.
* For example, a company that knows that its sales are impacted by weather conditions may purchase historical and 
  future weather forecast data to help them analyze and forecast sales.
* AWS provides a data marketplace called <b>AWS Data Exchange</b>, which is a catalog of datasets available via paid 
  subscription, as well as a number of free datasets.
  * 










