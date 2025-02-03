<h2>Chapter 1: An Introduction to Data Engineering</h2>


<h3>The rise of big data as a corporate asset</h3>

* Data engineering continues to be a fast-growing career path and a role in high demand, as data becomes ever more
critical to organizations of all sizes.
* This chapter will cover the many ways that data engineering has become an important, and increasingly valuable,
corporate asset.


* We can see the importance of data in large companies, as demonstrated by those companies creating a new executive
C-level position -- the <b>Chief Data Officer (CDO).</b>
* According to an [HBR article](https://hbr.org/2021/08/why-do-chief-data-officers-have-such-short-tenures), the role of
CDO was first established at Capital One in 2002. By 2012, it was estimated that 12% of firms ad a CDO. By 2021, this had
grown to 65% of firms.


* There is no doubt that data, when harnessed correctly and optimized for maximum analytic value, can be a game-changer
for an organization.


<h3>The challenges of ever-growing datasets</h3>

* Today, with the modern application development approach of microservices, companies commonly have hundreds, or even
thousands, of databases. Faced with many data silos, organizations invested in data warehousing systems that would 
  enable them to ingest data from multiple siloed databases into a central location for analytics.
* As data continued to grow, multiple data warehouses and data marts would be implemented for different business 
  units or groups. 
* New technologies were invented that were better able to work with very large datasets and different types. 
  <b>Hadoop</b>, and the underlying <b>MapReduce</b> technology, became a popular way for all types of companies to 
  store and process very large datasets. 
  * <b>Apache Spark</b> was the next evolution for big data processing. Spark showed significant increases in 
    performance when working with large datasets due to the fact that it did most processing in memory, 
    significantly reducing the amount of reading and writing to and from disks.
  * <b>Today, Apache Spark is often regarded as the gold standard for processing large datasets and is used by a 
    wide variety of companies.</b>


<h4>Data Lakes and Data Mesh</h4>

* In parallel with the rise of Apache Spark as a popular big data processing tool was the rise of the concept of 
  data lakes -- an approach that uses low-cost object storage as a physical storage layer for a variety of data 
  types, Apache Hive as a central catalog of all the datasets, and makes that data available for processing with a 
  wide variety of tools, including Apache Spark. 
* Data lakes were great for centralizing data but were often run by a centralized team that would look to ingest 
  data from all the data silos in an organization, transform and aggregate the data, and make it available centrally 
  for use by other teams. While this was a definite improvement on having databases and data warehouses spread out 
  with no central repository governance, there was still room for improvement.
  * By centralzing all the data and having a single team manage this repository of data, the teams working to 
    transform and extract additional value out of the data were often not the people most familiar with the business 
    context behind the data.
  * A <b>data mesh</b> is a new approach developed to address this. With a data mesh architecture, the idea is to 
    make the teams that generate the data responsible for creating an analytics version of the data, and then make 
    that data easily accessible to the rest of the organization without needing to make multiple copies of the data.
  * <i>A limited view of the data mesh is to consider it primarily a means of sharing data between teams without 
    needing to physically move or copy the data.</i>
  * <b>A full data mesh implementation goes well beyond the technology of how to share the data.</b>
  * A data mesh implementation meant a change to the processes of how operational data was converted into analytical 
    data, and along with it, the personas that were responsible for the data. A data mesh implementation was not 
    just a technical implementation, but rather <i>a change to the culture and operation of teams within an 
    organization.</i>
  * Whereas in many organizations, large-scale analytics had been done by a centralized team, with a data mesh 
    approach, the team that owns an application that generates data must <i>productize</i> that data to make it 
    available to the rest of the business.
  * Rather than being data engineers that transformed data, the centralized team would focus on being <b>data platform 
    engineers</b>, creating a standardized platform that met best practices. They would then make this platform 
    available to individual development teams to use in order to create and share their own data analytic products.


<h3>Understanding the role of the data engineer</h3>

The role of a <b>data engineer</b> is to do the following:
1. Design, implement, and maintain the pipelines that enable the ingestion of raw data into a storage platform. 
2. Transform that data to be optimized for analytics, based on data consumer requirements. 
3. Make that data available for various data consumers using their tool of choice.


* Data engineers must first design the pipelines that ingest raw data from various internal and external sources.
* They must then transform the raw input datasets to optimize them for analytics, using various techniques.
* Finally, the data engineer may need to assist in integrating various data consumption tools with the transformed 
  data, enabling data analysts and data scientists to use their preferred tools to draw insights from the data.


* Data engineers use tools such as <b>Apache Kafka, Apache Spark, Presto</b> (and many others), to build the data 
  pipeline and optimize data for analytics.


* Data scientists draw complex insights and make predictions based on various datasets, using machine learning and 
  artificial intelligence.
* Data analysts examine and combine multiple datasets in order to help a business understand trends in the data and 
  to make more informed business decisions.
  * Data scientists develop models that make <i>future predictions</i>, or identify non-obvious patterns in data; 
    the data analyst works with well-structured and modeled data to understand current conditions and to highlight 
    recent patterns from data.


<h3>Understanding other common data-related roles</h3>

* Organizations may have other role titles and job descriptions for data-related positions, but generally, these 
  will be a subset of the roles described above.
  * Big data architect or data platform architect could be a subset of the data engineer role, focused on designing 
    the architecture for big data pipelines, but not building the data specific pipelines.
  * Data visualization developer may be focused on building visualizations using BI tools, but this is a subset of 
    the data analyst role.
  * Larger organizations tend to have more focused job roles
  * <b>In smaller organizations, a single person may take on the role of data engineer, data scientist, and data 
    analyst.</b>


<h3>The benefits of using the cloud when building big data analytic solutions</h3>

* Cloud computing enables scalability, cost efficiency, security, and automation that most companies find impossible 
  to achieve within their own data centers, and this applies to the area of data analytics as well.
* <b>Successful data engineers need to understand the tools available in the cloud for building out complex data 
  anlytic projects and understand which set of tools is best to achieve the outcome needed for their project. In 
  this book, we'll learn more about AWS services for working with big data, and will gain hands-on experience in 
  developing a data engineering pipeline in AWS.</b>


* Refer to chapter 1 hands-on activity notes: Creating and accessing AWS account
