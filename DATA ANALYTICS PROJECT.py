#!/usr/bin/env python
# coding: utf-8

# # EDA PROJECT BY BISWARUP

# In[316]:


# In this Project we have used top 1000 company's dataset from Kaggle and did Exploratory Data Analysis on it. 
# The main moto was to clean the data and to answer these following questions

# 1. Top 10 companies with highest revenue.
# 2. Top 10 Companies with highest profit.
# 3. Top 10 Companies with highest assets.
# 4. Top 5 Companies with highest employees.
# 5. Top 10 Companies with lowest revenue.
# 6. Top 10 Companies with lowest profit.
# 7. Top 10 Companies with lowest assets.
# 8. Top 5 Companies with lowest employees.

#We plotted all these graphs as well. 


# In[3]:


#First we will import all the libraries that's necessary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# Now lets import the csv that we will be working with

df = pd.read_csv(r"E:\Pandas\Fortune 1000 Companies by Revenue.csv")


# In[5]:


# to view the csv file

df


# In[13]:


# to see all the rows 

pd.set_option('display.max.rows',999)


# In[14]:


df.info()


# In[18]:


df.dtypes


# In[47]:


df['assets'] = df['assets'].str.replace('$','')
df['assets'] = df['assets'].str.replace(',','')
df['assets'] = df['assets'].str.replace('.','')

df['assets'] = df['assets'].astype('int')


# In[40]:


df.head(999)


# In[61]:


#changed the column names for better understanding

df = df.rename(columns={'revenues ': 'Revenue_$Million', 'rank ': 'Rank', 'name ': 'Name', 'revenue_percent_change': 'Revenue_%Change', 'profits ': 'Profits_$Million', 'assets': 'Assets_$Million', 'profits_percent_change': 'Profit_%Change', 'market_value ': 'MarketValue_$Million', 'employees ': 'Employees' })


# In[62]:


df


# In[65]:


#here we dropped the unnecessary column

df = df.drop('change_in_rank',axis = 1)


# In[66]:


df


# In[67]:


# Now lets see how the data looks

df.info()


# In[68]:


# Now we need to change the rank, revenue, profits, market value and employee to integer


# In[69]:


#but before that we have to clean the strings


# In[70]:


df['Revenue_$Million'] = df['Revenue_$Million'].str.replace('$','')
df['Revenue_$Million'] = df['Revenue_$Million'].str.replace(',','')
df['Revenue_$Million'] = df['Revenue_$Million'].str.replace('.','')


# In[71]:


df


# In[72]:


df['Profits_$Million'] = df['Profits_$Million'].str.replace('$','')
df['Profits_$Million'] = df['Profits_$Million'].str.replace(',','')
df['Profits_$Million'] = df['Profits_$Million'].str.replace('.','')
df['MarketValue_$Million'] = df['MarketValue_$Million'].str.replace('$','')
df['MarketValue_$Million'] = df['MarketValue_$Million'].str.replace(',','')
df['MarketValue_$Million'] = df['MarketValue_$Million'].str.replace('.','')
df['Employees'] = df['Employees'].str.replace(',','')


# In[73]:


df


# In[74]:


df['Rank'] = df['Rank'].str.replace(',','')


# In[86]:


df['Profits_$Million'] = df['Profits_$Million'].str.replace('(','')
df['Profits_$Million'] = df['Profits_$Million'].str.replace(')','')
df['Revenue_%Change'] = df['Revenue_%Change'].str.replace('%','')
df['Profit_%Change'] = df['Profit_%Change'].str.replace('%','')


# In[89]:


df.head(999)


# In[124]:


# No we dropped all the null values

df = df.dropna(axis=1)


# In[126]:


df.info()


# In[133]:


df


# In[139]:


#changed the data type
df['Profits_$Million'] = df['Profits_$Million'].astype('int')
df['Assets_$Million'] = df['Assets_$Million'].astype('int')
df['Rank'] = df['Rank'].astype('int')
df['Employees'] = df['Employees'].astype('int')


# In[162]:


df.info()


# In[ ]:





# In[148]:


df.dropna(axis=0)


# In[149]:


#we used this loop to drop all the rows with null Market Values

for x in df.index:
    if df.loc[x,'MarketValue_$Million'] == '-':
        df.drop(x,inplace = True)
df


# In[171]:


#dropped % revenue change and % profit change as we don't need them

#df = df.drop(['Revenue_%Change', 'Profit_%Change'],axis =1)


# In[169]:


df


# In[172]:


df.info()


# In[175]:


#we changed the data type 

df['Revenue_$Million'] = df['Revenue_$Million'].astype('int')
df['MarketValue_$Million'] = df['MarketValue_$Million'].astype('int')


# In[176]:


df.info()


# In[178]:


#The mean, count, std, min, max and % values of each coulmns

df.describe().T


# In[181]:


#we did this to reset the index

df = df.reset_index(drop = True)


# In[182]:


df


# In[190]:


#Now Let's see the top 10 companies by revenue

hrevenue = df.nlargest(10,'Revenue_$Million')
hrevenue


# In[208]:


#Now let's see the bottom 10 companies by revenue

lrevenue = df.nsmallest(10, 'Revenue_$Million')
lrevenue


# In[ ]:


# Top 10 compamnies by Profit


# In[188]:


hprofit= df.nlargest(10, 'Profits_$Million')
hprofit


# In[210]:


lprofit= df.nsmallest(10, 'Profits_$Million')
lprofit


# In[212]:


# just to check the total number of null values

df.isnull().sum()


# In[213]:


df


# In[224]:


#df = df.set_index('Rank')


# In[223]:


df


# In[226]:


#just a normal subplot

df.plot()
df.plot(kind = 'line', subplots = True)


# In[279]:


#PLOT FOR TOP 10 REVENUE BY NAME 

hrevenue.plot.bar(y = 'Revenue_$Million', x= 'Name',figsize =(12,6),ylabel = 'Revenue in $ Million', 
                   title = 'Revenue by name')


# In[246]:


#to see the available themes

print(plt.style.available)


# In[275]:


#Theme that I used 

plt.style.use('seaborn-v0_8-deep')


# In[276]:


#PLOT FOR TOP 10 PROFIT BY NAME 

hprofit.sort_values(by = 'Profits_$Million', ascending = False).plot.bar(y = 'Profits_$Million', x= 'Name', figsize =(12,6), ylabel = 'Profit in $ Million', 
                   title = 'Top 10 Companies with Highest Profit')


# In[277]:


df


# In[278]:


#PLOT FOR LOWEST 10 PROFIT BY NAME 

lprofit.sort_values(by = 'Profits_$Million', ascending = False).plot.bar(y = 'Profits_$Million', x= 'Name', figsize =(12,6), ylabel = 'Profit in $ Million', 
                   title = 'Companies with Lowest Profit')


# In[281]:


#PLOT FOR BOTTOM 10 REVENUES OF COMPANIES

lrevenue.plot.bar(y = 'Revenue_$Million', x= 'Name',figsize =(12,6),ylabel = 'Revenue in $ Million', 
                   title = '10 Companies with Lowest Revenue')


# In[282]:


df


# In[288]:


# Top 10 Companies with highest Assets

hassets = df.nlargest(10, 'Assets_$Million')
hassets


# In[289]:


#TOP 10 COMPANIES WITH HIGEST ASSETS

hassets.plot.bar(y = 'Assets_$Million', x= 'Name',figsize =(12,6),ylabel = 'Assets_$Million', 
                   title = '10 Companies with Highest Assets')


# In[286]:


# Top 10 Companies with Lowest Assets

lassets = df.nsmallest(10, 'Assets_$Million')
lassets


# In[290]:


#Plot for 10 COMPANIES WITH Lowest ASSETS

lassets.plot.bar(y = 'Assets_$Million', x= 'Name',figsize =(12,6),ylabel = 'Assets_$Million', 
                   title = '10 Companies with Lowest Assets')


# In[297]:


df.describe().T


# In[301]:


# TOP 5 Companies with highest number of employees

lemployees = df.nlargest(10, 'Employees')
lemployees


# In[310]:


# Plot

lemployees.plot.bar(y = 'Employees', x= 'Name', ylabel = 'Total Employees', title = 'Top 10 Companies with Highest Employees')


# In[302]:


# 5 Companies with lowest employees

semployees = df.nsmallest(10, 'Employees')
semployees


# In[314]:


#Plot

semployees.sort_values(by = 'Employees', ascending = False).plot.bar(y = 'Employees', x= 'Name', ylabel = 'Total Employees', title = 'Top 10 Companies with Lowest Employees')


# In[315]:


# Final Data Frame

df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




