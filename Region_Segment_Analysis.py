#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pymysql
import pandas as pd

# Connection parameters
endpoint = "127.0.0.1"      # Usually localhost
username = "root"           # DB username
password = "Sakshi@123"     # DB password
database = "mini_project"   # Database name
port = 3306

# Create connection
try:
    connection = pymysql.connect(
        host=endpoint,
        user=username,
        password=password,
        database=database,
        port=port,
        charset='utf8mb4'
    )
    print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)


# In[101]:


# Show all tables in the database
query = "SHOW TABLES;"
tables = pd.read_sql(query, connection)
print("Tables in database:", tables)


# In[102]:


query = "SELECT * FROM order_items LIMIT 5;"
df = pd.read_sql(query, connection)
print(df)


# In[103]:


import pymysql

endpoint = "127.0.0.1"
username = "root"
password = "Sakshi@123"
database = "mini_project"
port = 3306

connection = pymysql.connect(
    host=endpoint,
    user=username,
    password=password,
    database=database,
    port=port,
    charset='utf8mb4'
)


# In[104]:


import pandas as pd

query = """
SELECT 
    l.region,
    c.segment,
    SUM(oi.sales) AS total_sales,
    SUM(oi.profit) AS total_profit,
    COUNT(DISTINCT o.order_id) AS order_count,
    COUNT(DISTINCT c.customer_id) AS customer_count,
    AVG(oi.sales) AS avg_order_value
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
JOIN locations l ON o.location_id = l.location_id
GROUP BY l.region, c.segment
ORDER BY l.region, c.segment
"""

df = pd.read_sql(query, connection)
print(df.head())  
print(df.shape)   


# In[105]:


# Check all databases
query = "SHOW DATABASES;"
dbs = pd.read_sql(query, connection)
print(dbs)


# In[106]:


# Check tables in mini_project
query = "SHOW TABLES;"
tables = pd.read_sql(query, connection)
print(tables)


# In[107]:


query = "SELECT * FROM orders LIMIT 5;"
df = pd.read_sql(query, connection)
print(df)


# In[108]:


import os
print(os.listdir())


# In[109]:


import os
print(os.getcwd())


# In[110]:


import pandas as pd

orders = pd.read_sql("SELECT * FROM orders", connection)
customers = pd.read_sql("SELECT * FROM customers", connection)
order_items = pd.read_sql("SELECT * FROM order_items", connection)
locations = pd.read_sql("SELECT * FROM locations", connection)
products = pd.read_sql("SELECT * FROM products", connection)


# In[111]:


import os
print(os.getcwd())


# import os
# print(os.listdir())
# 

# """
# 
# Datasets Used
# 
#  1. Orders
# - Order ID
# - Order Date
# - Customer ID
# - Region
# 
#  2. Customers
# - Customer ID
# - Customer Name
# - Segment
# 
#  3. Order Items
# - Order ID
# - Product ID
# - Sales
# - Quantity
# - Profit
# 
# """

# In[112]:


"""
Business Questions:

1. Which region generates the highest sales?
2. Which customer segment contributes most revenue?
3. Which region-segment combination performs best?
4. What are the profit trends across segments?
5. Are there low performing regions needing attention?
"""

