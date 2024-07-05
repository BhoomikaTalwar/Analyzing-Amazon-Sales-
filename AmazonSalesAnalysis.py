#!/usr/bin/env python
# coding: utf-8

# In[6]:


#importing libraries
import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[7]:


#loading csv file
sales=pd.read_csv('Data.csv')
sales.head(10)


# In[8]:


#number of rows and columns in the dataset
sales.shape


# In[9]:


#columns name
sales.columns


# In[12]:


#getting some info about the data
sales.info()


# #### Data Cleaning

# In[13]:


#checking for missing values
sales.isnull().sum()


# Observation: There is no missing values in the dataset

# In[16]:


#checking the correlation
plt.figure(figsize=(12,8))
sns.heatmap(sales.corr(), annot=True)


# In[17]:


sales.ItemType.value_counts()


# In[19]:


#statistical measures about the data (count,mean,SD etc.)
sales.describe()


# In[20]:


sales[['Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']].head(20)


# Observation:
# Total Profit=(Total Revenue-Total Cost)

# In[24]:


#calculate total profit
total_profit=sales["Total Profit"].sum()
print("Total Profit:",total_profit)


# In[25]:


#Convert Order Date to Datetime 
sales["Order Date"] = pd.to_datetime (sales ["Order Date"])


# In[26]:


#extract year and month from order date
sales['Year']=sales['Order Date'].dt.year
sales['Month']=sales['Order Date'].dt.month
sales.head()


# #### Data Visualization

# In[30]:


#year-wise sales
year_sales=sales.groupby('Year')['Total Revenue'].mean()
plt.figure(figsize=(8,3))
sns.barplot (x=year_sales.index,y=year_sales.values)
plt.title('Average Sales By Year')
plt.xlabel('Year')
plt.ylabel('Total Revenue')


# In[31]:


#Pie chart of Total Profit in region wise
plt.figure(figsize=(6,6))
region_TotalRevenue=sales.groupby('Region')['Total Profit'].mean()
plt.pie(region_TotalRevenue, startangle=90, labels=region_TotalRevenue.index, autopct='%1.1f%%')
plt.title('Average Profit in Region wise')


# In[33]:


#group Total Revenue by Item type
TotalRevenue_ItemType=sales.groupby('ItemType') ['Total Revenue'].sum()


# In[34]:


#bar chart for Total Revenue by Item type
plt.figure(figsize=(8,3))
TotalRevenue_ItemType.plot(kind='bar')
plt.xlabel('Item Type')
plt.ylabel('Total Revenue')
plt.title('Average Revenue by Product type')
plt.grid(axis='y')


# In[35]:


#group Total Revenue by Sales Channel
TotalRevenue_SalesChannel=sales.groupby('Sales Channel') ['Total Revenue'].mean()


# In[36]:


#Pie chart of Total Profit in region wise
plt.figure(figsize=(6,6))
plt.tight_layout()
TotalRevenue_SalesChannel.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Total Revenue by Sales Channel')


# In[37]:


#Create a Pie chart for a donut chart
Region_UnitSold=sales.groupby('Region') ['Units Sold'].sum()
plt.figure(figsize=(6,6))
Region_UnitSold.plot(kind='pie', labels=Region_UnitSold.index, autopct='%1.1f%%', startangle=90)

#Drow a circle at the centre of the pie Chart
cntr_circle=plt.Circle ((0,0), (0.70), fc='white')
fig = plt.gcf()
fig.gca().add_artist (cntr_circle)

#Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Units Sold by Regions')
plt.axis('equal')


# In[38]:


#Group Units Sold by Year and Month
YearMonth_UnitsSold=sales.groupby (['Year', 'Month']) ['Units Sold'].sum()


# In[39]:


#Create a Bar Chart for Units Sold by Year and Month
plt.figure(figsize=(9,9))
YearMonth_UnitsSold.plot(kind='bar')
plt.xlabel('Year and Month')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.grid(axis='y')


# In[41]:


#group Total cost by Sales Channel
TotalCost_SalesChannel=sales.groupby('Sales Channel') ['Total Cost'].sum()


# In[42]:


TotalCost_SalesChannel=sales.groupby('Sales Channel') ['Total Cost'].sum()
#bar chart for Total Cost by Sales channel
plt.figure(figsize=(6,6))
TotalCost_SalesChannel.plot(kind='pie', autopct="%1.1f%%", startangle=90) 
plt.title('Total Cost by Sales Channel')
plt.tight_layout()


# In[ ]:




