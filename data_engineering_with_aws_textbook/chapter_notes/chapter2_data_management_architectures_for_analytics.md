<h2>Chapter 2: Data Management Architectures for Analytics</h2>

* There are many different cloud services, open-source frameworks, file formats, and architectures that can be used 
  in analytic projects, depending on the business requirements and objectives.
* This chapter will cover how analytical technologies have evolved and will introduce the key technologies and 
  concepts that are foundational for building modern analytical architectures, irrespective of whether you build 
  them on <b>Amazon Web Services (AWS)</b> or elsewhere.

<h3>The evolution of data management for analytics</h3>

* It is important to be familiar with some of the key developments in analytics over time, as well as to understand 
  the foundational concepts of analytical data storage, data management, and data pipelines. 
  * As a Data engineer, you may come across analytic pipelines that were built using technologies from different 
    generations, and be expected to understand them. 

<h4>Databases and data warehouses</h4>

* There are two broad types of database systems, and both have been around for many years:
  * <b>Online Transaction Processing (OLTP)</b> systems are primarily used to store and update transactional data in 
    high volumes. For example, OLTP-type databases are often used to store customer records, including transaction 
    details (such as purchases, returns, and refunds).
  * <b>Online Analytical Processing (OLAP)</b> systems are primarily used for reporting on large volumes of data. It 
    is common for OLAP systems to take data from multiple OLTP databases, and provide a centralized repository of 
    data that can be used for reporting purposes.
* In the 1980s, data warehouses (OLAP systems) became a popular tool with which data could be ingested from multiple 
  database systems into a central repository, and the data warehouse could focus on running analytic reports.
  * The data warehouse was designed to store <b>integrated, highly curated, trusted</b> data, that was also very 
    structured (formatted with a well-defined schema).
  * Data would be ingested on a regular basis from other highly structured sources, but before entering the data 
    warehouse, the data would go through a significant amount of pre-processing, validation, and transformations.
  * Any changes to the data warehouse schema (how the data was organized, or structured), or the need to ingest new 
    data sources, would require a significant effort to plan the schema and related processes.

* In the last few decades, there has been a rapid growth in data sources, data volumes, and the options for 
  analyzing this increasing amount of data.
  * In parallel, organizations have realized the business value of the insights they can gain by combining data from 
    their internal systems with external data from their partners, the web, social media, and third-party data 
    providers.
  * To process consistently larger data volumes and increased demands to support new consumers, data warehouses have 
    evolved through multiple generations of technology and architectural innovations.

<h3>Dealing with big, unstructured data</h3>

* While data warehouses have steadily evolved over the last 25+ years to support increasing volumes of highly 
  structured data, there has been exponential growth in the amount of semi-structured and unstructured data produced 
  by modern digital platforms (such as mobile and web applications, sensors, IoT devices, social media, and audio 
  and video media platforms).
  * These platforms produce data at a high velocity, and in much larger volumes than data produced by traditional 
    structured sources.
  * It has become essential for organizations to gain deeper insights from these new data sources to gain a 
    competitive advantage and transform customer experiences.


* <b>Traditional data warehouses are good at storing and managing flat, structured data from sources such as a set of 
  tables, organized as a relational schema. However, they are not well suited to handling the huge volumes of 
  high-velocity semi-structured and unstructured data that are becoming increasingly popular.</b>
  * `Getting more experience with high-velocity (i.e., streaming) data that is also semi-structured or unstructured 
    would be really valuable for me.`


* <b>Hadoop</b>, an open-source framework for processing large datasets on clusters of computers, became the leading 
  way to work with big data in the early 2010s. These clusters contained tens or hundreds of machines with attached 
  disk volumes that could hold tens of thousands of terabytes of data managed under a single distributed filesystem 
  known as the <b>Hadoop Distributed File System (HDFS)</b>.
  * However, building and scaling on-prem Hadoop clusters typically required a large upfront capital investment in 
    machines and storage. The ongoing management of the cluster and big data processing pipelines required a team of 
    specialists that included Hadoop admins and data engineers specialized in processing frameworks like Spark, Hive,
    and Presto.
  * Big data teams managing on-prem clusters typically spent a significant percentage of their time managing and 
    upgrading their cluster's hardware and software, as well as optimizing workloads.

<h3>Cloud-based solutions for big data analytics</h3>

* After AWS launched Amazon EMR in 2009 (a managed platform for running Hadoop frameworks), and Redshift in 2013 (a 
  cloud-native data warehouse), the number of other companies developing cloud-based solutions for big data 
  analytics rapidly increased.
  * Companies like Google Cloud Platform (GCP), Microsoft Azure, Snowflake, and Databricks provide a number of 
    solutions for ingesting, storing, and analyzing large datasets in the cloud.

* Cloud providers require no upfront investment, and offer a petabyte scale, as well as high performance and elastic 
  capacity scaling. They have a usage-based cost model, and freedom from infrastructure management. Basically, they 
  are vastly superior to on-prem systems for most use cases.

* A notable trend brought on by the move to the cloud has been the adoption of highly durable, inexpensive, and 
  virtually limitless cloud object stores.
  * S3 can store hundreds of petabytes of data at a fraction of the cost of on-prem storage, and support storing 
    data regardless of its source, format, or structure. There are also tons of cloud-native and third-party data 
    processing and analytic tools.

<h4>Cloud object stores and the emergence of data lakes</h4>

* These new cloud object stores have enabled organizations to build a new, more integrated analytics data management 
  approach with decoupled compute and storage, called a <b>data lake</b> architecture. 
  * A data lake architecture makes it possible to create a single source of truth by bringing together a variety of 
    data of all sizes and types (structured, semi-structured, or unstructured) in one place: a central, highly 
    scalable repository built using inexpensive cloud storage.
  * A wide variety of analytic tools have been created or modified to integrate with these cloud object stores, 
    providing organizations with many options for building data lake-based big data platforms.


<h3>A deeper dive into data warehouse concepts and architecture</h3>

* An <b>Enterprise Data Warehouse (EDW)</b> is the central data repository that contains structured, curated, 
  consistent, and trusted data assets that are organized into a well-modeled schema. The data assets in an EDW are 
  made up of all the relevant information about key business domains and are built by integrating data sourced from 
  ERPs, CRMs, and line-of-business applications, as well as external data sources from partners or third parties.
* An EDW provides business users and decision makers with an easy-to-use, central platform that helps them find and 
  analyze a well-modeled, well-integrated, single version of truth for various business subject areas such as 
  customers, products, sales, marketing, supply chain, and more. Business users analyze data in the warehouse to 
  measure performance, find current and historical business trends, find business opportunities, and understand 
  customer behavior.


* Typically, a data-warehouse-centric architecture includes the following:
  * Data sources from across the business that provide raw data to the data warehouse via <b>Extract, Transform, 
    Load (ETL), or Extract, Load, Transform (ELT)</b> processes.
  * One or more data warehouses (and, optionally, multiple subject-focused data marts).
  * End user analytic tools for consuming data from the warehouse (such as SQL-based analytic tools, and business 
    intelligence visualization systems).
    
![Screenshot 2025-02-02 at 10 47 22 PM](https://github.com/user-attachments/assets/05f507db-7114-4508-b106-c93d4f6c9aee)

<h3>Dimensional modeling in data warehouses</h3>

* Data assets in the warehouse are typically stored as relational tables that are organized into widely used 
  dimensional models, such as a <b>star schema</b> or <b>snowflake schema</b>. Storing data in a warehouse using a 
  dimensional model makes it easier to retrieve and filter relevant data, and it also makes analytic query 
  processing flexible, simple, and performant.
  
![Screenshot 2025-02-02 at 10 49 30 PM](https://github.com/user-attachments/assets/7c811b79-749c-46f9-af70-fcc7f4367e92)

<b>Star schema</b>

* In data warehouses, tables are generally separated into <b>fact tables</b> and <b>dimension tables</b>. In the 
  above figure, the data entities are organized like a star, with the sales fact table (i.e., a sale "event" that 
  took place) forming the middle of the star, and the dimension tables forming the corners.
  * A fact table stores granular numeric measurements/metrics for a specific domain (such as sales). The `SALES_FACT` 
    table stores facts about an individual sales transaction, such as the price and quantity sold. The fact table also 
    has a large number of <b>foreign key</b> columns that reference the primary keys of associated dimension tables.
  * The dimension tables store the context under which the fact measurements were captured. Each individual 
    dimension table essentially provides granular attributes related to one of the dimensions of the fact (such as 
    the store where the sale took place).
  * Rather than storing all of the details of the store (such as street address, region, phone number, etc.) in the 
    sales table, we just store the `store_id` related to the specific sale as a foreign key. We can join the 
    `SALES_FACT` table and the `STORE_DIMENSION` table to retrieve that information if necessary.

* In a <b>star schema</b>, while data for a subject area is <b>normalized</b> by splitting measurements and context 
  information into separate <i>fact</i> and <i>dimension</i> tables, individual dimension tables are typically kept 
  <b>denormalized</b> so that all related attributes of a dimensional topic can be found in a single table. 
  * This makes it easier to find all related attributes of a dimensional topic in a single table (fewer joins, and a 
    simple-to-understand model).
  * For larger dimension tables, a denormalized approach can lead to data duplication and inconsistencies within the 
    dimension table. Large denormalized dimension tables can be slow to update.
  * One approach to work around these issues is a slightly modified type of schema, the <b>snowflake schema</b>.
  
![Screenshot 2025-02-02 at 10 59 25 PM](https://github.com/user-attachments/assets/b455df58-4780-4d90-840b-53792079ae0a)

<b>Snowflake schema</b>

* The challenges of inconsistencies and duplication in a star schema can be addressed by <b>snowflaking</b> 
  (basically normalizing) each dimension table into multiple related dimension tables.
* <b>This normalization of tables continues until each individual dimension table contains only attributes with a 
  direct correlation with the table's primary key.</b>
* This highly normalized model from this snowflaking is called a <b>snowflake schema</b>.
* A snowflake schema can reduce redundancy and minimize disk space, compared to a star schema, which often contains 
  duplicate records. However, on the other hand, the snowflake schema may necessitate complex joins to answer 
  business queries and may slow down query performance.
* To decide on whether to use a snowflake or star schema, you need to consider the types of queries that are likely 
  to be run against the dataset and balance the pros and cons of potentially slower and more complex queries with a 
  snowflake schema versus less performant updates and more complexity in managing changes to dimension tables with a 
  star schema.

<h3>Reduced duplication example with snowflake schema vs. star schema:

<h3>Star Schema (Denormalized, More Duplication)</h3>

Customer Table
--------------------------------------
| CustomerID | Name    | State       | Country   |
|-----------|--------|------------|----------|
| 101       | Alice  | Texas      | USA      |
| 102       | Bob    | Texas      | USA      |
| 103       | Charlie | California | USA      |

* The "State" and "Country" fields are repeated for multiple customers.

<h3>Snowflake Schema (Normalized, Less Duplication)</h3>

Customer Table
--------------------------------------
| CustomerID | Name    | StateID |
|-----------|--------|---------|
| 101       | Alice  | TX      |
| 102       | Bob    | TX      |
| 103       | Charlie | CA     |

State Table
--------------------------------------
| StateID | StateName   | CountryID |
|---------|------------|-----------|
| TX      | Texas      | USA       |
| CA      | California | USA       |

Country Table
--------------------------------------
| CountryID | CountryName      |
|-----------|-----------------|
| USA       | United States   |

* The "State" and "Country" information is stored once and referenced via IDs, reducing redundancy/duplication.

Advantages of Snowflake Schema for Reducing Duplication:
1. Less Storage Waste: Since attributes like state and country are stored in separate tables, they don’t need to be 
repeated.
2. Improved Data Integrity: Updates to a state or country only need to happen in one place. In a snowflake schema, 
   the database enforces referential integrity using foreign key constraints, which means a misspelled StateID would 
   be rejected if it doesn't exist in the State table. In a denormalized schema, you could have a misspelling like 
   "Texs" for the state, and that would not be rejected since it is not referencing a foreign key.
3. Better Scalability: Large datasets benefit from normalized structures because they reduce redundant data storage.

<h3>Understanding the role of data marts</h3>

* Data warehouses contain data from all relevant business domains and have a comprehensive yet complex schema.
* Organizations have a narrower set of users who want to focus on a particular line of business, department, or 
  business subject area.
  * These users typically prefer to work with a repository that has a simple-to-learn schema, and only the subset of 
    data that focuses on the area they are interested in. Organizations typically build <b>data marts</b> to serve 
    these users.
* A data mart is focused on a single business subject repository (for example, marketing, sales, or finance) and is 
  typically created to serve a narrower group of business users, such as a single department.
  * A data mart often  has a set of denormalized fact tables organized into a much simpler schema compared to that 
    of an EDW.
* Both data warehouses and data marts provide an integrated view of data from multiple sources, but they differ in 
  the scope of data they store. Data warehouses provide a central store of data for the entire business, or division,
  and cover all business domains. Data marts serve a specific business function by providing an integrated view of a 
  subject area relevant to that business function.

<h3>Distributed storage and massively parallel processing (MPP)</h3>

* Below is the underlying architecture of a <b>Redshift</b> cluster. This shows a Redshift cluster based on <b>RA3 
  nodes</b>.
  
![Screenshot 2025-02-02 at 11 31 22 PM](https://github.com/user-attachments/assets/abe68376-148f-4f0a-8ec4-9c8674ce55d0)

* The leader node interfaces with client applications, receives and parses queries, and coordinates query executions 
  on compute nodes.
* For RA3 node types, Amazon S3 is used as <b>Redshift Managed Storage (RMS)</b> for warehouse data, and the compute 
  node high-performance local storage is used as a cache for hot data.
* Each compute node has its own independent processors, memory, and high-performance storage volumes that are 
  isolated from other compute notes in the cluster (this is called a shared-nothing architecture).
* In the MPP approach, the cluster leader node first compiles the incoming client query into a distributed execution 
  plan. It then coordinates the execution of segments of compile query code on multiple compute nodes of the data 
  warehouse cluster, in parallel. Each compute node executes assigned query segments on a portion of the distributed 
  dataset.

<h3>Columnar data storage and efficient data compression</h3>

* Modern data warehouses boost query performance through <b>column-oriented</b> storage and <b>data compression</b>.
* Let's first look at how OLTP databases store their data.
  * To serve OLTP applications, backend databases need to efficiently read and write full rows to the disk. To speed 
    up full-row lookups and updates, OLTP databases use a row-oriented layout to store table rows on the disk. In a 
    <b>row-oriented</b> physical data layout, all the column values of a given row are co-located, as seen below.

![Screenshot 2025-02-02 at 11 37 18 PM](https://github.com/user-attachments/assets/0112156e-dc3c-40f9-b97a-836ea8e0ae89)

* Most analytic queries against a data warehouse are written to answer a specific question and typically include 
  grouping or aggregations on a large number of rows, but a narrow set of columns from the fact and dimension tables.
  * A <b>row-oriented</b> physical data layout forces analytics queries to scan a large number of full rows (all 
    columns), even though they need only a subset of the columns from these rows. Analytics queries on a 
    row-oriented database can thus require a much higher number of disk I/O operations than necessary. 


* Modern data warehouses store data on disks using a <b>column-oriented</b> physical layout.
  * This is more suitable for analytical query processing, which only requires a subset of columns per query.
  * A data warehouse breaks a table into groups of rows, called row chunks/groups. It then takes a row chunk at a 
    time and lays out data from that row chunk, one column at a time, so that all the values for a column (that is, 
    for that row chunk) are physically co-located on the disk, as seen below.

![Screenshot 2025-02-03 at 12 49 53 AM](https://github.com/user-attachments/assets/fb75f045-27c6-44de-a79b-dfc191249bd5)

```
Example: Row vs. Column Storage Impact
Imagine a 1 billion row table with 50 columns, but your query only selects 3 columns.

* Row-oriented storage: Reads all 50 columns from disk (even though only 3 are needed).
* Column-oriented storage: Reads only 3 columns, skipping the rest → less disk I/O, faster queries.
```

```
Note on Redshift:
A single Redshift query CAN hog resources, but you can prevent this by:
1. Limiting memory/CPU per query, as well as query timeout limit for automatic termination of long-running queries 
(WLM settings)
2. Optimizing queries (filters, keys, compression)
3. Avoiding unnecessary data shuffling on nodes (bad distribution key)
4. Using Concurrency Scaling for large workloads

```

* In addition to the column-oriented storage layout, modern data warehouses also employ <b>compression algorithms</b> 
  for a table.
  * The warehouse is able to match individual columns with the compression algorithm that is most optimal for the 
    given column's type and profile of its data content (reducing disk I/O and saving space).
  * Data warehouses typically have good compression ratios since there are a larger percentage of duplicate values 
    among the columns. This results in faster reads/writes, and smaller on-disk footprints.

<h3>Feeding data into the warehouse -- ETL and ELT pipelines</h3>

* To bring data into the warehouse (and optionally, data marts), organizations typically build data pipelines that 
  do the following:
  * Extract data from source systems
  * Transform source data by validating, cleaning, standardizing, and curating it
  * Load the transformed source data into the enterprise data warehouse schema, and optionally a data mart as well
* In these pipelines, the first step is to extract data from source systems, but the next two steps can either take 
  place in a Transform-Load or Load-Transform sequence (ETL or ELT).

![Screenshot 2025-02-03 at 12 02 28 AM](https://github.com/user-attachments/assets/98799f8c-1651-4752-b0ae-9c202ef5ea30)

* With an ETL pipeline, transformations are performed outside the data warehouse using custom scripts, a 
  cloud-native ETL service such as AWS Glue, or a specialized ETL tool from a commercial vendor such as Informatica, 
  Talend, DataStage, Microsoft, or Pentaho.


* An ETL approach to building a data pipeline is typically used when the following are true:
  * Source database technologies and formats are different from those of the data warehouse
  * The engineering team wants to perform transformations using a programming language (such as PySpark) rather than 
    using pure SQL
  * Data transformations are complex and compute-intensive

* ELT pipelines extracts data (typically highly structured) from various sources, and loads it as is into the 
  staging area of the data warehouse. The database engine powering the data warehouse is then used to perform 
  transformation operations on the staged data and writes the transformed data to a production table (ready for 
  consumption).

![Screenshot 2025-02-03 at 12 06 27 AM](https://github.com/user-attachments/assets/995ff878-17bc-42a0-9565-4ae5937debce)

* ELT is typically leveraged when the following are true:
  * Data sources and the warehouse have similar database technologies, making it easier to directly load source data 
    into the staging tables in the warehouse.
  * A large volume of data needs to be quickly loaded into the warehouse.
  * All the required transformation steps can be executed using the native SQL capabilities of the warehouse's 
    database engine.

<h3>ELT vs ETL</h3>

* The primary difference between ETL and ELT is about where the data transformation takes place.
* With ELT, the data is loaded directly into the data warehouse, and the data warehouse engine is used for the 
  transformation.
  * Using an ELT approach limits your transformations to using SQL, which may or may not be ideal depending on the 
    use case.
* With ETL, an engine outside the data warehouse first transforms the data before writing it to the data warehouse.

<h3>An overview of data lake architecture and concepts</h3>

* Data warehouses are limited to processing data primarily using only SQL, and SQL is not the right tool for all 
  data processing requirements.
* A cloud data lake is a central, highly scalable repository in the cloud where an organization can manage exabytes 
  of various types of data, including:
  * Structured data (row-column based tables)
  * Semi-structured data (JSON, XML, logs, sensor/IoT device data streams)
  * Unstructured data (audio, video streams, Word/PDF documents, emails)

* Unlike a data warehouse, data does not need to first be converted into a standard structure before it is consumed.
* A cloud data lake also natively integrates with cloud analytic services that are decoupled from data lake storage 
  and enables diverse analytic tools, including SQL, code-based tools (such as Apache Spark), specialized machine 
  learning tools, and business intelligence visualization tools.

![Screenshot 2025-02-03 at 12 13 47 AM](https://github.com/user-attachments/assets/42db40b4-ef0b-4ed3-bc9a-40a4acfe1eac)

<h3>Data lake logical architecture</h3>

* Data lake architecture has a set of components organized into five logical layers:
1. <b>Storage layer</b>: this is built on an object store (such as S3). It provides virtually unlimited, low-cost 
   storage 
   that can store any format. There are no hard rules about how many data zones there should be, but having three is 
   common. The <b>landing zone</b> is raw data straight from the source. The <b>clean zone</b> contains data after the 
   initial data processing such as validating, cleaning, and optimizing. PII in this zone may have been removed, 
   masked, or replaced with tokens. The <b>curated zone</b> contains data in its most consumable state and meets all 
   organizational standards. Data here is typically partitioned, cataloged, and optimized for the consumption layer.
2. <b>Catalog and search layers</b>: data lakes have potentially thousands of datasets, from a variety of internal and 
   external sources. Teams need to have the ability to search for available datasets and review the schema and other 
   metadata of those datasets.
3. <b>Ingestion layer</b>: this layer is responsible for connecting to diverse types of data sources and brinigng their 
   data into the landing/raw zone of the storage layer. A typical ingestion layer may include tools such as AWS 
   Database Migration Service (DMS) for ingesting data from various databases, AWS Kinesis Firehose for ingesting 
   streaming data, and AppFlow for ingesting data from SaaS applications.
4. <b>The processing layer</b>: this layer makes data ready for consumption by data consumers. The processing layer 
   transforms the data in the lake through various stages of data cleanup, standardization, and enrichment. The 
   processing layer stores transformed data into different zones along the way -- writing it into the clean zone, 
   and then the curated zone, and then ensuring that the technical data catalog gets updated. Common tools here are 
   AWS Glue and EMR.
5. <b>The consumption layer</b>: This layer provides purpose-built tools that are able to access data from the 
   storage layer, and the schema from the catalog layer (to apply schema-on-read to the lake-hosted data).

<h3>Bringing together the best of data warehouses and data lakes</h3>

* Data lakes are well-suited to storing different types of data inexpensively, and provide a wide variety of tools 
  to work with and consume the data.
* Limitations: data lakes do not support the <b>ACID</b> (atomicity, consistency, isolation, and durability) 
  properties common in most databases.
  * This can cause issues if one team is updating data in the data lake while another team attempts to query the 
    data, leading to inconsistencies.
* Due to the use of inexpensive object storage, query performance does not match what is possible with data 
  warehouses that use high-performance, SSD-based local storage.
* These challenges can be worked around by loading a subset of the data from the data lake into a data warehouse, 
  such as Redshift or Snowflake. This offers performance needed for demanding business intelligence applications, 
  and also provides consistency when multiple teams are working with the same dataset.
  * However, <b>data warehousing storage is expensive</b>, and some use cases require joining data across a diverse 
    set of data, and it is not economical to load all this data into the warehouse.
* This led to an approach called the <b>data lake house</b>.

<h3>The data lake house approach</h3>

* The data lake house (Lakehouse data lakehouse) approach brings together the best of data warehouses and data lakes.
* There is no standard definition of a lake house, beyond the intention of different vendors to provide the best of 
  both data warehouses and data lakes with their own technology stacks.
* Three main table types: Delta Lake, Apache Hudi, and Apache Iceberg. Apache Iceberg seems to be gaining the most 
  traction recently.


<h3>Federated queries across database engines</h3>

* Federated queries allow queries across different database engines or storage platforms
* For example, the most recent 12 months of data could be loaded into a data warehouse, while the previous 4 years 
  could be in the data lake. Most queries only need the recent 12 months, and that is stored in the highly 
  performant storage of the data warehouse.
  * For the queries that need access to the historical information, the data warehouse could join tables in the S3 
    data lake with the recent data in the warehouse. 
* With federated queries, the requirement to copy data between different data systems through ETL pipelines is 
  reduced. However, querying across different systems does not perform as well as querying on local-only data, so 
  there are use cases where you would still want to copy data between systems.
* Having the ability to query across data systems is useful in many situations, and helps create a more integrated 
  big data ecosystem. 


* Refer to hands-on chapter 2 activity: Using the AWS Command Line Interface (CLI) to create Simple Storage Service 
  (S3) buckets
