# Data Warehouses

- Centralized systems or repositories that store data from various sources
- Examples include transactional database systems, APIs, ERP systems, and CRM systems
- Support business intelligence in a consistent format
- Track historical information

# Data Lakes

- Flexible and scalabale data storage systems storing both struct and unstruc data
- Does not require predefined schema or structure
- Easier for end users to access raw data

# Data Lakehouse

- Moder versions of data lakes with an extra layer
- Adds the benefit of querying the data in a structured format
- Example: Apache Hive

# Summary

- Databases provide transactional efficiency
- Data warehouses are optimized for complex analytical queries from various sources
- Data lakes offer scalability and flexibility
- Data lakehouses

# Data Quality

"Data quality checks and validation with SQL":

- Importance of Data Quality: Ensuring data quality, completeness, and correctness is crucial as data moves through the ETL process to avoid truncation, loss, or corruption.
- Common Checks: Methods include counting rows and columns, checking for nulls, empty rows, duplicates, and default values.
- Freshness Checks: Implementing freshness checks to ensure data is up-to-date, such as agreeing on data warehouse SLAs.
- Practical Example: Demonstrated how to compare row counts between the source and the data warehouse using SQL and pandas to ensure data accuracy.
