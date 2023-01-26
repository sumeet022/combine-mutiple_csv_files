#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob


# In[2]:


get_ipython().system('pip install glob2')


# In[3]:


data_files = sorted(glob.glob(r'C:\Users\sumeet\Desktop\BRIDGELABZ\month_wise_sheets\2022-sheets\Mastersheet*.csv'))
data_files


# In[20]:



for name in glob.glob(r'C:\Users\sumeet\Desktop\BRIDGELABZ\month_wise_sheets\Mastersheet*.csv'): 
    print(name)


# In[4]:


merged_data = pd.concat(pd.read_csv(datafile)
                        for datafile in data_files)


# In[5]:


merged_data


# In[6]:


merged_data.head()


# In[8]:


merged_data.isna().sum()


# In[16]:


merged_data = merged_data.drop(['Unnamed: 7','Stream','Year of Passing','State','Role','Total Exp','Date','Source','Funnel' , 'college','% in IT' ,'Source code','Funnel.1','Unnamed: 18' ],axis=1)


# In[33]:


import mysql.connector as msql
from mysql.connector import Error


# In[109]:


try:
    conn = msql.connect(host='localhost', user='root',  
                        password='root',auth_plugin='mysql_native_password' , database='email')
    if conn.is_connected():
        cursor = conn.cursor()
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


# In[85]:


a = merged_data['Email']


# In[91]:


a.to_csv(r'C:\Users\sumeet\Desktop\BRIDGELABZ\bridgeLabz\email_list.csv')


# In[88]:


merged_data.to_csv(r'C:\Users\sumeet\Desktop\BRIDGELABZ\bridgeLabz/new_one.csv')


# In[121]:


conn.commit()


# In[119]:


cursor.execute("select count(*) from email.email_list limit 10;")


# In[120]:


cursor.fetchall()


# In[ ]:


#It takes time to reflect on the dataset
for row in csv_data:
    print(row)
    cursor.execute('insert into email_list(MyUnknownColumn,Email) VALUES (%s,%s)',row)

