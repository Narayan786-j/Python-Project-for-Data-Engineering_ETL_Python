#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


# In[9]:


# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[3]
print(df)


# In[10]:


# Replace the column headers with column numbers
df.columns = range(df.shape[1])
print(df)


# In[11]:


# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]
print(df)


# In[12]:


# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11,:]
print(df)


# In[13]:


# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']
print(df)


# In[14]:


# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
print(df)


# In[15]:


# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000
print(df)


# In[16]:


df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']],2)
print(df)


# In[23]:


df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})
print(df)


# In[25]:


df.to_csv('./economics.csv')


# In[28]:


import requests
from bs4 import BeautifulSoup

x = "https://en.wikipedia.org/wiki/IBM"
# In[33]:


response = requests.get(x)


# In[ ]:




