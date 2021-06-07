
## Course 1: Data Architecture Foundations
In this course, you will learn about the principles of data architecture. You will begin by learning the characteristics of good data architecture and how to apply them. Next you will move on to data modeling. You will learn to design a data model, normalize data and create a professional ERD. Finally, you will take everything you learned and create a physical database using PostGreSQL.

### Project 1 Designing an HR Database
 
In this project, you will design, build, and populate a database for the Human Resources (HR) Department at the imaginary Tech ABC Corp, a video game company. This project will start with a request from the HR Manager. From there, you will need to design a database using the foundational principles of data architecture that is best suited to the department’s needs. You will go through the steps of database architecture, creating database proposals, database entity relationship diagrams, and finally creating the
database itself. This project is a scaled-down simulation of the kind of real-world assignments data architects work on every day.



### LESSON ONE What is Data Architecture?
 
•	Define data architecture characteristics
•	Define data governance and its role
•	Define scalability and flexibility in database design
 
### LESSON TWO  Database Framework
 
•	Introduction to ERDs
•	Develop a database schema
•	Understand normalization and its use cases
•	Learn to normalize data to the 3rd Normal Form
 


### LESSON THREE Relational Data Design
 
•	Introduction to ERDs
•	Build a conceptual ERD
•	Build a logical ERD
•	Learn about cardinality and Crow’s Foot notation
•	Build a physical ERD
 

### LESSON FOUR	Creating a Physical Database
 
•	Learn about factors that affect database performance
•	Learn about file and data storage solutions
•	Use DDL SQL to create database objects in PostGreSQL
•	Learn about data ingestions methods, including: ETL, Pipelines, APIs and direct feeds
•	Use DML SQL to populate a database with data in PostGreSQL
•	Use CRUD SQL commands to demonstrate proper operation of a database
 


## Course 2: Designing Data Systems
In this course, you will learn to design enterprise data architecture. You will build a cloud based data warehouse with Snowflake. You will evaluate various data assets of an organization and characteristics of these data sources, design a staging area for ingesting varieties of data coming from source systems, and design an Operational Data Store (ODS). Finally, you will learn to design OLAP dimensional data models, design ELT data processing that is capable of moving data from an ODS to a data warehouse, and write SQL queries for the purpose of building reports.

### Project 2 Design a Data Warehouse for
Reporting and OLAP
 
In this project, you will design end to end data architecture, build ingestion of data from Yelp and Climatic source systems, design Operational Data Store and Data warehouse systems, and transform data from staging to ODS and finally from ODS to data warehouse system. Yelp source carries a list of businesses, restaurants, its reviews and ratings. Climatic data source keeps track of temperature and precipitation data. Both of these websites are independent sources and not related to each other. The final objective of this project is to write appropriate SQL to find the impact of weather on restaurant ratings.
 


### LESSON ONE Enterprise Data Architecture
 
•	Understand importance of Data Architecture in any organization
•	Learn the benefits of executing a Data Architecture
•	Learn the business and technical artifacts required
•	Understand business and functional requirements
•	Learn how OLTP, ODS and OLAP models are being designed
 
### LESSON TWO	Staging Data

•	Build staging area for data ingestion
•	Learn to organize data assets based on schemas
•	Design schedules for data processing based on the requirements
•	Learn to manage staging area through metadata

### LESSON THREE	Operational Data

•	Build an integrated ER model connecting distributed data assets
•	Learn to design Data Dictionary and Master Data
•	Apply normalization rules to eliminate redundancies
•	Learn when to use ETL vs ELT techniques
•	Learn to cleanse data anomalies


### LESSON FOUR	Data Warehouse

•	Learn two OLAP modeling designs — Star and Snowflake schemas
•	Learn various dimensional and fact table types
•	Build ELT data processing from ODS to Data warehouse
•	Write SQL queries for the purpose of reporting

## Course 3: Big Data Systems
In this course, you will learn about how to help organizations with massive amounts of data, including identification of Big Data problems and how to design Big Data solutions. You will learn about the internal architecture of many of the Big Data tools such as HDFS, MapReduce, Hive and Spark, and how these tools work internally to provide distributed storage, distributed processing capabilities, fault tolerance and scalability. Next, you will learn how to evaluate NoSQL databases, their use cases and dive deep into creating and updating a NOSQL database with Amazon DynamoDB. Finally, you will learn how to implement Data Lake design patterns and how to enable transactional capabilities in a Data Lake.

### Project 3 Design an Enterprise Data Lake System
 
In this project, you will act as a Big Data Architect and work on a real world use case faced by a Medical Data Processing Company. The project requires you to analyze the current architecture of the company, understand technical and business requirements and propose a new Data Lake based solution to both technical and executive audiences. For technical audiences, you will develop
a design document outlining your solution with rationale, and for the executive audience you will record a short presentation
pitching your solution. This is a real world scenario where you will act as an expert data infrastructure consultant to the company and solve the challenges the company is facing today. You will also hone your presentation skills and learn to articulate complex technical terminologies as easy to understand and value driven objectives to company leadership.

### LESSON ONE Characteristics of Big Data
 
•	Explain what is big data
•	Articulate the business value of big data
•	Describe the characteristics of big data
•	Distinguish between horizontal scaling vs vertical scaling
•	Describe the components of a big data ecosystem
 


### LESSON TWO Ingestion, Storage and Processing Frameworks
 
•	Explain how distributed storage works in HDFS
•	Explain how distributed processing works
•	Explain how resources are managed in a Hadoop cluster
•	Distinguish between different distributed processing frameworks
•	Apply frameworks to appropriate use cases
 


### LESSON THREE NoSQL Databases
 
•	Explain difference between SQL and NoSQL Databases
•	Differentiate between ACID and CAP properties of SQL and NoSQL databases
•	Implement, create, read, write, update NoSQL DB operations with DynamoDB
•	Create simple NoSQL data model
 

### LESSON FOUR Scalable Data Lake Architecture
 
•	Explain what is a data lake and it’s business value
•	Distinguish between different data formats and their application
•	Articulate Data Lake design patterns and challenges
•	Explain how to enable transactional capabilities in Data Lake
 


## Course 4: Data Governance
In this course you will learn how to design a data governance solution that meets your company’s needs. First, you will learn about the different types of metadata and how to build a Metadata Management System, Enterprise Data Model and Enterprise Data Catalog. Next, you will learn how to perform data profiling using various techniques including data quality dimensions, how to identify remediation options for data quality issues, and how to measure and monitor data quality using data quality scores, thresholds, dashboards, exception and trend reports. Finally, you will learn the concepts of Master Data and golden record, different types of Master Data Management Architectures, as well as the golden record creation and master data governance processes.

### Project 4 Data Governance at SneakerPark
 
In this project, you will be implementing data governance solutions for an online shoe reseller SneakerPark to better manage their data now and in the future. First, you will create an Enterprise Data Model that provides a holistic view of all the data in their systems. Next you will document the metadata in an Enterprise Data Catalog and profile the data in their systems to identify data quality issues, suggest remediation strategies for each of these issues, and design a data quality dashboard. Finally, you will sketch out a proposed MDM implementation architecture, define a set of matching rules for the creation of customer and item master data, and define the data governance roles and responsibilities that are necessary to oversee this data governance initiative.

### LESSON ONE Introduction to Data Governance
 
•	Understand what is Data Governance and its importance
•	Learn about the different disciplines of Data Governance
•	Understand the different stakeholders involved in Data Governance projects
 
### LESSON TWO Metadata Management
 
•	Understand the different types of metadata
•	Understand the components and capabilities of Metadata Management System
•	Create conceptual and logical Enterprise Data Models
•	Create an Enterprise Data Catalog
 
### LESSON THREE Data Quality Management  

• Perform data profiling using various techniques using data quality dimensions
• Identify remediation options for data quality issues
• Measure data quality using data quality scores and thresholds
• Monitor data quality using dashboards, exception and trend reports

### LESSON FOUR  Master Data Management
 
•	Understand the concepts of master data and golden record
•	Understand different types of Master Data Management Architectures
•	Create a golden record using various match and merge techniques
•	Understand data governance processes for authoring, monitoring and approval of master data

