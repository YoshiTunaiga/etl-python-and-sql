# ETL in Python and SQL

## Data Warehouses

- Centralized systems or repositories that store data from various sources
- Examples include transactional database systems, APIs, ERP systems, and CRM systems
- Support business intelligence in a consistent format
- Track historical information

## Data Lakes

- Flexible and scalabale data storage systems storing both struct and unstruc data
- Does not require predefined schema or structure
- Easier for end users to access raw data

## Data Lakehouse

- Moder versions of data lakes with an extra layer
- Adds the benefit of querying the data in a structured format
- Example: Apache Hive

## Summary

- Databases provide transactional efficiency
- Data warehouses are optimized for complex analytical queries from various sources
- Data lakes offer scalability and flexibility
- Data lakehouses

## Data Quality Checks and Validation with SQL

As data moves, it is important to ensure data quality, completeness, and correctness.

Data Pipeline:

1. Collection
2. Ingestion
3. Preparation
4. Computation
5. Presentation

Data Accuracy Checks

- Completeness
- Uniqueness
- Consistency
- Current

Data integrity Checks

- Duplicates detection
- Freshness
- Timeliness

# Questions

- Tarek is a data analyst who needs to ensure the integrity and consistency of data before it is analyzed. Which step in the ETL process should he focus on? Transform; it cleans and standardizes the data.

- Why is it crucial to consider data volume and velocity when designing an ETL process? to account for and manage scalability and performance of the pipeline

- What is the purpose of using pandas DataFrames in the ETL process with Python? It provides out of the box and easy to use easy-to-use functions and methods for working with data

- How does understanding the structure and quality of your data influence the ETL process before transformation and warehousing? You can apply business logic correctly.

- What is the significance of using pandas to read data from a CSV file in Python? It simplifies data manipulation tasks.

- Why is it important to use the shape attribute when reading a CSV file in Python? It identifies the structure of the dataset.

- How can the choice of data source and format impact the ETL process in terms of data loading and transformation? by ensuring efficient processing

- Jordana needs to extract data from an Excel file into her Python script. What is the correct method and parameter she should use with pandas to accomplish this task? pd.read_excel with filepath_or_buffer

- For global sales reporting, Hideko needs to ensure consistency in currency across sales data recorded in different currencies. Which data transformation technique should he use? data cleaning and standardization

- Arrigo is tasked with transferring customer data through a filter to check for duplicates. Which pandas method should he use to identify and handle duplicates? DataFrame.duplicated()

- How can someone effectively transform data in a DataFrame using pandas by removing specific columns? by using the pandas method df.drop() to drop irrelevant columns and reduce the complexity and focus on relevant data

- Why is it necessary to specify the sheet name when loading data from an Excel file using pandas? to ensure the correct data is loaded from the sheet if it has multiple sheets

- What is the purpose of specifying the if_exists parameter in the to_sql function when loading data into a database using pandas? to indicate how to handle existing tables

- Why is data quality checks essential in the ETL process? to ensure that data has not been lost during the ETL process

- What is the purpose of using the to_sql function in pandas when loading data into a database? to insert data from the DataFrame into the specified database table

- Zendayo is working on a project that involves storing Unstructured data from social media. Which data storage system is most suitable for her project? Data Lakehouse

- James needs to load customer data from a Jupyter Notebook into a PostgreSQL database for further analysis. Which method should he use to accomplish this task? pandas method DataFrame.to_sql()

- How can querying data from a database using SQL contribute to making informed business decisions? by getting informed decisions based on data insights and identifying trends and patterns in customer behavior

- As a data engineer, Katelyn must ensure timely updates for her team's sales reports before their daily 8:00 AM meeting. Which platform should she use to streamline this process? a scheduler like Apache Airflow, SSIS, or Oozie

- How does encapsulating ETL logic in Python files enhance workflow efficiency? by consolidating logic into reusable functions

- What is the primary objective of using Airflow in the context of data-processing challenges? to automate the scheduling of data tasks

- What role does the PythonOperator play in the Airflow DAG for automating data tasks? It executes the python function that contains the logic for the data task.

- How does implementing incremental ETL loads contribute to data-processing efficiency? by disregarding changes in source data over time and by reducing processing time and resource utilization
