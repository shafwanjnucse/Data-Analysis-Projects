#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv('drugaddictiondata.csv')


# In[4]:


df.head(5)


# In[5]:


df.tail(5)


# In[6]:


df.info()


# In[7]:


print(df.isnull().sum())


# In[8]:


df.describe()


# In[9]:


#converting all columns to integer values
col=df.columns
for i in col:
    df[i]=(df[i].values.astype(int))


# In[10]:


#printing all the unique values
for i in col:
    print(i,df[i].unique())


# In[12]:


drug_taken=df.groupby('Age')['If chance given to taste drugs'].sum().reset_index()


# In[14]:


plt.figure(figsize=(10,6))
sns.barplot(data=drug_taken, x='Age', y='If chance given to taste drugs', palette='viridis')
plt.xlabel('Age',fontsize=10,color='Green')
plt.ylabel('If chance given to take drugs',fontsize=8,color='Red')
plt.title("Had the opportunity to taste drugs (per age)")
plt.show()


# In[21]:


def lowerupper(col):
    q1 = np.quantile(col, .25)
    q3 = np.quantile(col, .75)
    inter = q3 - q1
    lowerbound = q1 - (inter * 1.5)
    upperbound = q3 + (inter * 1.5)
    outlier = []
    
    for x in col:
        if (x > upperbound) or (x < lowerbound):
            outlier.append(x)
    
    return outlier


# In[22]:


for i in col:
    outlier=lowerupper(df[i].values)
    print(len(outlier),"Outliers are present in ",i)


# In[49]:


correlation=df['Class'].corr(df['Suicidal thoughts'])
print("Correlation value between Addiction Level & Suicidal Thoughts", correlation)


# In[51]:


correlation2=df['Class'].corr(df['Addicted person in family'])
print("Correlation between Addiction Level and Addicted Person in Family: ",correlation2)


# In[52]:


correlation3=df['Class'].corr(df['Failure in life'])
print("Correlation between Addiction Level and Failure in Life: ", correlation3)


# In[57]:


failure_class=df.groupby('Class')['Failure in life'].sum().reset_index()


# In[59]:


plt.figure(figsize=(10,6))
sns.scatterplot(data=failure_class,x='Class',y='Failure in life',palette='viridis' )
plt.xlabel("Addiction Level")
plt.ylabel("Failure in Life")
plt.title("Addicition level vs Failure in Life")
plt.show()


# In[54]:


correlation4=df['Class'].corr(df['Smoking'])
print("Correlation between Addiction Level and Smoking: ", correlation4)


# In[55]:


smoking_class=df.groupby('Class')['Smoking'].sum().reset_index()


# In[56]:


plt.figure(figsize=(10,6))
sns.scatterplot(data=smoking_class,x='Class',y="Smoking", palette='viridis')
plt.xlabel("Addiction Level")
plt.ylabel("Smoking")
plt.title("Relation between Addiction Level and Smoking")
plt.show()


# In[37]:


ge_counts = df.groupby('Age').size()
label_age = age_counts.index
explode = [0.1] * len(age_counts)
plt.title("Age")
plt.subplot(1, 1, 1)
plt.pie(age_counts, labels=label_age, autopct='%1.1f%%', explode=explode)
plt.show()


# In[39]:


label_fl=[1 ,2]
plt.title("Failure in life")
plt.pie(df.groupby(df["Failure in life"]).size(),labels=label_fl)


# In[41]:


label_mp=[1, 2, 3, 5, 4]
plt.title("Mental/emotional problem")
plt.pie(df.groupby(df["Mental/emotional problem"]).size(),labels=label_mp)


# In[42]:


label_af=[2, 3, 1]
plt.title("Addicted person in family")
plt.pie(df.groupby(df["Addicted person in family"]).size(),labels=label_af)


# In[43]:


plt.subplots_adjust(left=0,right=2,bottom=1,top=2,wspace=0.2,hspace=0.4)
label_st=[1 ,2]
plt.title("Suicidal thoughts")
plt.pie(df.groupby(df["Suicidal thoughts"]).size(),labels=label_st)


# In[45]:


influence=df.groupby('Age')['Friends influence'].sum().reset_index()


# In[46]:


plt.figure(figsize=(10,6))
sns.barplot(data=influence,x='Age', y= 'Friends influence' ,palette='viridis')
plt.xlabel('Age Range',fontsize=15,color='Green')
plt.ylabel('Influenced by friends',fontsize=10, color='Red')
plt.title("Distribution of different age group people being influenced to take drugs")
plt.show()


# In[47]:


suicide_class=df.groupby('Class')['Suicidal thoughts'].sum().reset_index()


# In[48]:


plt.figure(figsize=(10,6))
sns.scatterplot(data=suicide_class, x='Class',y='Suicidal thoughts', palette='viridis')
plt.xlabel("Addiction Level", fontsize=15, color="Yellow")
plt.ylabel("Suicidal Thoughts",fontsize=20,color="Red")
plt.title("Relation Between Addiction Level and Suicidal Thoughts")
plt.show()

