#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install mysql-connector-python


# ## Importing Libraries

# In[3]:


# Import pandas library for data manipulation
import pandas as pd            

# Import datetime class from datetime module for date handling
from datetime import datetime   

# Import MySQL Connector Python module for MySQL database interaction
import mysql.connector

# Import Error class from MySQL Connector module for error handling
from mysql.connector import Error


# ## Data Extraction

# In[5]:


# Data Extraction from given url
csv_file_url = 'https://drive.google.com/uc?id=1asq7yzvFpkmDUMZQtK7AJ16_XZbQCZmc'

try:
    # read csv file using pandas library
    data = pd.read_csv(csv_file_url)
    
except Exception as e:
    # print error
    print(f"Error reading CSV: {e}")
    exit()


# In[6]:


# Display the first five rows of the DataFrame
data.head()


# In[7]:


# Display the last five rows of the DataFrame
data.tail()


# ## Data Understanding

# In[9]:


# Generate descriptive statistics summary for numerical columns in DataFrame
data.describe()


# In[10]:


# Retrieve the column names of the 'data' DataFrame
data.columns


# In[11]:


# Count the number of missing values (NaN) in each column of the 'data' DataFrame
data.isna().sum()


# In[12]:


# Count the number of duplicated rows in the 'data' DataFrame
data.duplicated().sum()


# In[13]:


# Retrieve the data types of each column in the 'data' DataFrame
data.dtypes


# In[14]:


# Convert 'Date of Birth' column to datetime format and then format it to '%Y-%m-%d'
data['Date of Birth'] = pd.to_datetime(data['Date of Birth'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')


# ## Data Transformation

# In[16]:


# Define a function to clean and standardize column names of a DataFrame
def clean_data(data):
    # Drop rows with missing values (NaN)
    data = data.dropna()
    
    # Standardize column names: strip leading/trailing spaces, convert to lowercase, replace spaces with underscores
    data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

    return data

# Clean and standardize data in 'data' DataFrame, and store the result in 'borrowers_data'
borrowers_data = clean_data(data)


# In[17]:


# Display the first few rows of the cleaned and standardized 'borrowers_data' DataFrame
borrowers_data.head()


# ## Data Loading

# In[19]:


# MySQL connection parameters
db_config = {
    'host': 'localhost',    # Hostname of the MySQL server
    'user': 'root',         # Username used to connect to MySQL server
    'password': 'Datta@2505',  # Password used to authenticate the user
    'database': 'debt_collection'  # Name of the database to connect to
}


# In[20]:


# Define a function to load data into MySQL 'borrowers' table
def load_data(data):
    try:
        # Establish connection to MySQL database using db_config parameters
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Insert data into the 'borrowers' table row by row
            for _, row in data.iterrows():
                insert_query = """
                INSERT INTO borrowers (
                    name, date_of_birth, gender, marital_status, phone_number, email_address, mailing_address,
                    language_preference, geographical_location, credit_score, loan_type, loan_amount, loan_term,
                    interest_rate, loan_purpose, emi, ip_address, geolocation, repayment_history, 
                    days_left_to_pay_current_emi, delayed_payment
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, tuple(row))  # Execute insert query for each row

            connection.commit()  # Commit changes to the database
            print("Data loaded successfully.")  # Success message
            
    except Error as e:
        print(f"Error: {e}")  # Print error message if an exception occurs
    
    finally:
        if connection.is_connected():
            cursor.close()      # Close cursor object
            connection.close()  # Close database connection

if __name__ == "__main__":
    # Assuming borrowers_data is already defined
    data = borrowers_data
    load_data(data)  # Call load_data function to load data into MySQL 'borrowers' table

