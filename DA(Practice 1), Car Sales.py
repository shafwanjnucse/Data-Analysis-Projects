#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv('CarSales.csv')


# In[6]:


df.head(10)


# In[7]:


print(df.info())


# In[8]:


print(df.describe())


# In[11]:


df=df.dropna()


# In[12]:


print(df.isnull().sum())


# In[17]:


plt.figure(figsize=(10,6))
sns.histplot(df['selling_price'], kde=True)
plt.title('Distribution of Selling Price')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show ()


# In[18]:


name_counts=df['name'].value_counts()


# In[32]:


df["name_2"] = df.name.apply(lambda x : ' '.join(x.split(' ')[:1]))
df['name_2']


# In[33]:


df.name_2.value_counts()


# In[34]:


sns.countplot(data=df,x="name_2",palette="CMRmap")
plt.xticks(rotation=90)
plt.xlabel("Name",fontsize=10,color="black")
plt.ylabel("Name",fontsize=10,color="black")
plt.title("NAME COUNT",color="black")
plt.show()


# In[38]:


labels=df['name_2'][:30].value_counts().index
sizes=df['name_2'][:30].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"pink","yellow"]
plt.figure(figsize=(10,6))
plt.pie(sizes, labels=labels,autopct='%1.1f%%',colors=colors,shadow=True, startangle=45)
plt.title('Pie Chart of the Number of Different Cars')
plt.show()


# In[42]:


labels = df["year"][:40].value_counts().index
sizes = df["year"][:40].value_counts()
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"pink","yellow"]
plt.figure(figsize = (8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%',colors=colors,shadow=True, startangle=45)
plt.title('Car Selling Percentage in Each Year',color = 'red',fontsize = 15)
plt.show()


# In[49]:


recent_years = df[df['year'] >= df['year'].max() - 5]


# In[50]:


total_sales=recent_years.groupby('year')['selling_price'].sum().reset_index()


# In[55]:


plt.figure(figsize=(10, 6))
sns.barplot(data=total_sales, x='year', y='selling_price', palette='viridis')
plt.title('Total Sales for Recent Four Years')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()


# In[ ]:




