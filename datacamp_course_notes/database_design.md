<h2>Database Design</h2>
https://app.datacamp.com/learn/courses/database-design

* Main question: how should we organize and manage data?

<h3>1. Processing, Storing, and Organizing Data</h3>

<b>OLTP and OLAP</b>
* Online Transaction Processing (OLTP), Online Analytical Processing (OLAP)
* These help define the way data is going to flow, be structured, and stored
* OLTP is focused on supporting day-to-day operations, while OLAP tasks are vaguer and focus on business decision making
  * OLTP systems are application-oriented (e.g., bookkeeping)
  * They can be seen as a current snapshot of transactions that are archived often
  * Simpler queries 
  * These systems are used by more people throughout a company, and even a company's customers
  * Data is inserted and updated more often
  * Most likely to have data from the past hour
  * Typically uses an operational database (optimized for write-heavy operations with fast inserts, updates, deletes)


* OLAP systems are oriented around a certain subject that's under analysis, like last quarter's book sales
  * The data in these systems tends to be from a larger time period for long-term analysis
  * Larger, more complex queries for analysis
  * Typically only used by analysts and data scientists within the company
  * Typically uses a data warehouse (stores large volumes of historical data; optimized for read-heavy querying and analysis)
    
![Screenshot 2025-01-15 at 2 09 24 PM](https://github.com/user-attachments/assets/84a2a2a0-bc0a-4b1b-ab41-8b60ae8b8b13)

* These systems work together; they need each other.
* OLTP data is usually stored in an operational database that is pulled and cleaned to create an OLAP data warehouse
* Without transactional data, no analyses can be done in the first place
* Analyses from OLAP systems inform business practices and day-to-day activities, thereby influencing the OLTP databases

![Screenshot 2025-01-15 at 2 10 27 PM](https://github.com/user-attachments/assets/1d1da0e3-13ca-4890-ba53-b7961409a6a2)

<u>OLTP & OLAP Summary</u>

| Feature                | OLTP (Operational Databases)               | OLAP (Data Warehouses)                  |
|------------------------|--------------------------------------------|-----------------------------------------|
| **Purpose**            | Manages daily transactions and operations | Supports decision-making and analytics |
| **Data Type**          | Current, detailed, transactional data      | Historical, aggregated, multidimensional data |
| **Operations**         | Insert, update, delete, and retrieve data | Complex read-heavy queries and analysis |
| **Query Type**         | Simple and frequent queries (e.g., CRUD)  | Complex, long-running analytical queries |
| **Optimization**       | Write-heavy performance                   | Read-heavy performance                 |
| **Schema**             | Highly normalized (to reduce redundancy)  | Denormalized (to improve query speed)  |
| **Focus**              | Data integrity and transaction consistency| Data analysis and insights             |
| **Processing Type**    | OLTP (transactional processing)           | OLAP (analytical processing)           |
| **Users**              | Application users and developers          | Data analysts, scientists, and executives |
| **Concurrency**        | High concurrency for many users           | Lower concurrency for fewer analytical users |
| **Data Volume**        | Smaller volumes (e.g., gigabytes)         | Larger volumes (e.g., terabytes to petabytes) |
| **Examples**           | MySQL, PostgreSQL, Oracle Database        | Snowflake, Amazon Redshift, BigQuery   |

<b>Database Design</b>
Database design determines how data is logically stored. This affects how the database will be queried, whether for 
reading data or updating data.

Two important concepts for database design:
1. Database models
2. Database schemas

Models are high-level specifications for database structure. The relational model is the most popular.
It defines rows as records and columns as attributes. It calls for rules such as each row having unique keys.

A schema is a database's blueprint; it is the implementation of the database model. It takes the logical structure
more granularly by defining the specific tables, fields, relationships, indexes, and views a database will have.

Schemas must be respected when inserting structured data into a relational database.

<b>Data modeling</b>
The first step to database design is data modeling. This is the abstract design phase, where we define a data model for
the data to be stored. Three levels to a data model:
1. Conceptual data model: describes entities, relationships, attributes
*  Tools: data structure diagrams, e.g., entity-relational diagrams and UML diagrams
2. Logical data model: defines tables, columns, relationships
*  Tools: database models and schemas, e.g., relational model and star schema
3. Physical data model: describes physical storage
* Tools: partitions, CPUs, indexes, backup systems and tablespaces

https://en.wikipedia.org/wiki/Data_model

Example of data model using songs

![Screenshot 2025-01-15 at 2 32 37 PM](https://github.com/user-attachments/assets/0847e7cc-86a5-40f0-a6c5-433405a6465e)
![Screenshot 2025-01-15 at 2 33 29 PM](https://github.com/user-attachments/assets/ea6c0780-edf8-4a8e-aea1-d6a19c7e4e60)

Dimensional modeling is an adaptation of the relational model specifically for data warehouses.
It's optimized for OLAP type queries that aim to analyze rather than update. It uses the star schema.
Dimensional models are made up of two types of tables: 
1. Fact tables
2. Dimension tables

The fact table contents are decided by the business use case. It contains records of a key metric, and this metric changes often.
Fact tables also hold foreign keys to dimension tables. Dimension tables hold descriptions of specific attributes
and these do not change as often. This is illustrated below with the song example.

![Screenshot 2025-01-15 at 2 38 19 PM](https://github.com/user-attachments/assets/fe67ee45-415d-46ca-813d-9f00479b2c68)

The dimension tables expand on the attributes of a fact table, such as the album it is in and the artist who made it.
The records in fact tables often change as new songs get inserted. Albums, labels, artists, and genres will be shared my more
than one song -- hence records in dimension tables won't change as much.

Summary: to decide the fact table in a dimensional model, consider what is being analyzed and how often entities change.


<h3>2. Database Schemas and Normalization</h3>


