#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Code for ETL operations on Country-GDP data

# Importing the required libraries

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''


# In[15]:


import numpy as np
import pandas as pd


# In[18]:


URL="https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks"


# In[2]:


# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[1]
print(df)


# In[27]:


# Convert the GDP value in Million USD to Billion USD
df['MC_GBP_Billion'] = df['Market cap (US$ billion)']*0.8
df['MC_EUR_Billion'] = df['Market cap (US$ billion)']*0.93
df['MC_INR_Billion'] = df['Market cap (US$ billion)']*82.95
print(df)


# In[26]:


df['MC_INR_Billion'] = df['Market cap (US$ billion)']*82.95
print(df)


# In[28]:


df = df.rename(columns={'Market cap (US$ billion)': 'MC_USD_Billion'})
print(df)


# In[39]:


df.to_csv('C:/Users/NARAYAN1.JHA/Downloads/Largest_banks_data.csv')


# In[40]:


print(df['MC_GBP_Billion'].mean())


# In[47]:


df['MC_GBP_Billion'] = np.round(df['MC_GBP_Billion'],2)


# In[1]:


df['MC_GBP_Billion'] = [np.round(df['MC_GBP_Billion'],2) for x in df['MC_USD_Billion']]
print(df['MC_GBP_Billion'])


# In[ ]:




