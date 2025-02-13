<h2>Quickstart for dbt Cloud and Snowflake</h2>

https://docs.getdbt.com/guides/snowflake?step=1

* This guide shows how to use dbt Cloud with Snowflake. Specifically, it shows how to:
  * Create a new Snowflake worksheet
  * Load sample data into your Snowflake account
  * Connect dbt Cloud to Snowflake
  * Take a sample query and turn it into a model in your dbt project (a model in dbt is a select statement).
  * Add sources to your dbt project. Sources allow you to name and describe the raw data already loaded into Snowflake.
  * Add tests to your models
  * Document your models
  * Schedule a job to run


<b>Other resources</b>
* [dbt fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) has a learning course with videos
* [YouTube video](https://www.youtube.com/watch?v=kbCkwhySV_I&list=PL0QYlrC86xQm7CoOH6RS7hcgLnd3OQioG) on dbt and Snowflake (only 8 mins)
* Snowflake also has a [quickstart guide](https://quickstarts.snowflake.com/guide/accelerating_data_teams_with_snowflake_and_dbt_cloud_hands_on_lab/#0) to use dbt Cloud. It uses a different dataset.


<h3>Getting Started - creating Snowflake warehouse, database, tables</h3>

* In the Snowflake account, create a new SQL Worksheet
* Execute the SQL statements in `create_db_load_data.sql` to create a new virtual warehouse, two new databases, and two new schemas within the raw database.
Load the data from the appropriate S3 buckets.
* Connect dbt Cloud to Snowflake with either:
1. Partner Connect, which provides a streamlined setup to create your dbt Cloud account from within Snowflake.
2. Create dbt Cloud separately and built the Snowflake connection yourself (manually).
* Partner Connect is quicker, and is recommended for this tutorial, so I'll do that.
* Within Snowflake, click Home -> Data Products -> Partner Connect -> dbt
  * Add RAW and ANALYTICS databases privileges 
  * Then Click Connect and Activate, finish setting up dbt Cloud account
* Within dbt account, click your account name -> Account settings -> Partner Connect Trial
  * Edit the database and warehouse fields to be analytics, transforming, respectively

<h3>Set up dbt Cloud managed repository</h3>

* Partner Connect initializes a managed repository for you. Otherwise, you need to create your repository connection.
* When you develop in dbt Cloud, you can leverage Git to version control your code


<h3>Initialize dbt project and start developing</h3>

* Initialize your project and start development in dbt Cloud:
1. On dbt UI, click on Develop -> Cloud IDE
2. Click on Initialize the project to build folder structure
3. Click Commit and sync to push these changes to your managed repo
4. Directly query data from the warehouse and execute `dbt run` - create a new file, add a quick `select *`, save the file and run to test this out

Leaving off here: https://docs.getdbt.com/guides/snowflake?step=6
