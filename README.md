# Bodake_Dattatray_DebtCollectionETL
ETL (Extract, Transform, Load) process on a CSV file containing borrower data, load it into a SQL database, and conduct simple analysis for debt collection purposes.

# Debt Collection ETL Project

## Overview

This project involves performing an ETL (Extract, Transform, Load) process on a CSV file containing borrower data, loading it into a MySQL database, and conducting basic analysis for debt collection purposes.

## Project Structure

- `etl_script.py`: Python script for the ETL process, including data extraction, transformation, and loading.
- `analysis_queries.sql`: SQL script containing queries for basic analysis.
- `analysis_results.txt`: Text file with the results of the analysis.
- `README.md`: This file, containing instructions and project details.

## Python ETL Script (`etl_script.py`)

### Libraries Used

- `pandas`: For data manipulation.
- `mysql-connector-python`: For MySQL database interaction.

### Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DattatrayBodake25/Bodake_Dattatray_DebtCollectionETL.git
    cd Bodake_Dattatray_DebtCollectionETL
    ```

2. Install the required Python libraries:
    ```bash
    pip install pandas mysql-connector-python
    ```

### Running the ETL Script

1. Download the CSV file from the provided URL:
    ```bash
    wget "https://drive.google.com/uc?id=1asq7yzvFpkmDUMZQtK7AJ16_XZbQCZmc" -O borrowers.csv
    ```

2. Open `etl_script.py` in your preferred text editor and ensure the following configurations are set correctly:
    - MySQL connection parameters (`db_config` dictionary).
    - Path to the downloaded `borrowers.csv` file (`file_path` variable).

3. Run the ETL script:
    ```bash
    python etl_script.py
    ```

### Code Explanation

- The script reads data from a CSV file (`borrowers.csv`) using pandas, cleans and transforms the data, and then loads it into a MySQL database named `debt_collection` under a table named `borrowers`.
- It handles basic data cleaning such as removing NaN values and standardizing column names.
- MySQL connection parameters (`db_config`) are provided for connecting to the database.
- Error handling is implemented using `try-except` blocks to catch and print any exceptions during the data loading process.

### Performing Basic Analysis

1. Open `analysis_queries.sql` in your preferred SQL client and run the queries to get the analysis results.

2. The results can be found in `analysis_results.txt`.

Thank You!
