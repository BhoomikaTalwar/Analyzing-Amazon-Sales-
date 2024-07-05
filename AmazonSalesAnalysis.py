#!/usr/bin/env python
# coding: utf-8

# In[44]:


#importing libraries
import pandas as pd
import numpy as mp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[45]:


#loading csv file
sales=pd.read_csv('Amazon Data.csv')
sales.head(10)


# In[46]:


#number of rows and columns in the dataset
sales.shape


# In[47]:


#columns name
sales.columns


# In[48]:


#getting some info about the data
sales.info()


# #### Data Cleaning

# In[49]:


#checking for missing values
sales.isnull().sum()


# Observation: There is no missing values in the dataset

# In[50]:


#checking the correlation
plt.figure(figsize=(12,8))
sns.heatmap(sales.corr(), annot=True)


# In[51]:


sales.ItemType.value_counts()


# In[52]:


#statistical measures about the data (count,mean,SD etc.)
sales.describe()


# In[53]:


sales[['Unit Price','Unit Cost','Total Revenue','Total Cost','Total Profit']].head(20)


# Observation:
# Total Profit=(Total Revenue-Total Cost)

# In[54]:


#calculate total profit
total_profit=sales["Total Profit"].sum()
print("Total Profit:",total_profit)


# In[55]:


#Convert Order Date to Datetime 
sales["Order Date"] = pd.to_datetime (sales ["Order Date"])


# In[56]:


#extract year and month from order date
sales['Year']=sales['Order Date'].dt.year
sales['Month']=sales['Order Date'].dt.month
sales.head()


# #### Data Visualization

# In[57]:


#year-wise sales
year_sales=sales.groupby('Year')['Total Revenue'].mean()
plt.figure(figsize=(8,3))
sns.barplot (x=year_sales.index,y=year_sales.values)
plt.title('Average Sales By Year')
plt.xlabel('Year')
plt.ylabel('Total Revenue')


# In[58]:


#Pie chart of Total Profit in region wise
plt.figure(figsize=(6,6))
region_TotalRevenue=sales.groupby('Region')['Total Profit'].mean()
plt.pie(region_TotalRevenue, startangle=90, labels=region_TotalRevenue.index, autopct='%1.1f%%')
plt.title('Average Profit in Region wise')


# In[59]:


#group Total Revenue by Item type
TotalRevenue_ItemType=sales.groupby('ItemType') ['Total Revenue'].sum()


# In[60]:


#bar chart for Total Revenue by Item type
plt.figure(figsize=(8,3))
TotalRevenue_ItemType.plot(kind='bar')
plt.xlabel('Item Type')
plt.ylabel('Total Revenue')
plt.title('Average Revenue by Product type')
plt.grid(axis='y')


# In[61]:


#group Total Revenue by Sales Channel
TotalRevenue_SalesChannel=sales.groupby('Sales Channel') ['Total Revenue'].mean()


# In[62]:


#Pie chart of Total Profit in region wise
plt.figure(figsize=(6,6))
plt.tight_layout()
TotalRevenue_SalesChannel.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Total Revenue by Sales Channel')


# In[63]:


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


# In[64]:


#Group Units Sold by Year and Month
YearMonth_UnitsSold=sales.groupby (['Year', 'Month']) ['Units Sold'].sum()


# In[65]:


#Create a Bar Chart for Units Sold by Year and Month
plt.figure(figsize=(9,9))
YearMonth_UnitsSold.plot(kind='bar')
plt.xlabel('Year and Month')
plt.ylabel('Units Sold')
plt.tight_layout()
plt.grid(axis='y')


# In[66]:


#group Total cost by Sales Channel
TotalCost_SalesChannel=sales.groupby('Sales Channel') ['Total Cost'].sum()


# In[67]:


TotalCost_SalesChannel=sales.groupby('Sales Channel') ['Total Cost'].sum()
#bar chart for Total Cost by Sales channel
plt.figure(figsize=(6,6))
TotalCost_SalesChannel.plot(kind='pie', autopct="%1.1f%%", startangle=90) 
plt.title('Total Cost by Sales Channel')
plt.tight_layout()


# In[ ]:




