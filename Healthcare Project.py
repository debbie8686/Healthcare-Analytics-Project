#!/usr/bin/env python
# coding: utf-8

# # Import Data

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"/Users/jungjungchen/Downloads/healthcare_dataset.csv"  
df = pd.read_csv(file_path)


# In[2]:


print(df.head())


# In[3]:


print(df.info())


# # Data Cleaning

# ### Summary statistics of the numerical columns

# In[4]:


print(df.describe()) 


# ### Summary statistics of the categorical columns

# In[5]:


print(df.describe(include='object'))


# ### Unique values analysis for categorical columns

# In[6]:


for col in df.select_dtypes(include='object').columns:
    print(f"{col} Unique Values: {df[col].nunique()}")
    print(df[col].value_counts(), "\n")


# ### Checking for missing values

# In[7]:


print(df.isnull().sum())


# ### Standardizing the capitalization of names

# In[8]:


df["Name"] = df["Name"].str.title()


# In[9]:


print(df.head())


# ### Fixing misaligned text in hospital column

# In[13]:


df["Hospital"] = (
    df["Hospital"]
    .str.replace(",", " ", regex=True)         
    .str.replace(r"\bAnd\b", "", regex=True)  
    .str.replace(r"\($", "", regex=True)      
    .str.rstrip("'")                           
    .str.replace(r"\s+", " ", regex=True)
    .str.title().str.strip()                   
)


# In[14]:


print(df["Hospital"].unique())


# In[15]:


print(df["Hospital"].head(10)) 


# ### Remove duplicates columns and keep unique columns

# In[16]:


df["Name"] = df["Name"].str.title().str.strip()
df = df.drop_duplicates(subset=["Name", "Date of Admission"], ignore_index=True)


# In[17]:


df["Doctor"] = df["Doctor"].str.title().str.strip()

df["Doctor"].value_counts().head(10)


# In[18]:


df["Hospital"] = df["Hospital"].str.title().str.strip()

df["Hospital"].value_counts().head(10)


# ### Convert admission date and discharge date to datetime

# In[19]:


df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])


# ### Correct discharge dates where is earlier than admission date

# In[20]:


df.loc[df["Discharge Date"] < df["Date of Admission"], "Discharge Date"] = df["Date of Admission"]

df[df["Discharge Date"] < df["Date of Admission"]]


# # Data Visualization

# ### Common medical conditions distribution

# In[21]:


plt.figure(figsize=(8,3))
sns.countplot(y=df["Medical Condition"], order=df["Medical Condition"].value_counts().index, palette=sns.color_palette("coolwarm", 6))
plt.title("Most Common Medical Conditions")
plt.show()


# ### Age distribution

# In[22]:


plt.figure(figsize=(8,4))
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# ### Admission types distribution

# In[23]:


sns.countplot(x="Admission Type", data=df)
plt.title("Types of Patient Admissions")
plt.xticks(rotation=45)
plt.show()


# ### Billing amounts distribution

# In[24]:


plt.figure(figsize=(6,4))
sns.boxplot(x=df["Billing Amount"], palette="pastel")
plt.title("Billing Amount Distribution")
plt.show()


# ### Test results distribution

# In[25]:


df["Test Results"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["skyblue", "lightpink", "lightgreen"])
plt.title("Test Results Distribution")
plt.ylabel(None)
plt.show()


# ### Count test results grouped by medication

# In[26]:


plt.figure(figsize=(8,4))
sns.countplot(x="Test Results", hue="Medication", data=df, palette="pastel")

plt.title("Test Results by Medication")
plt.xlabel("Test Results")
plt.ylabel("Count")
plt.legend(title="Medication")

plt.show()


# ### Test Results Summary by Medical Condition

# In[27]:


test_results_summary = df.pivot_table(
    index="Medical Condition", 
    columns="Test Results", 
    aggfunc="size", 
    fill_value=0
)

test_results_summary.columns.name = "Test Results"
test_results_summary


# ## Save the Cleaned Dataset as a CSV File

# In[28]:


df.to_csv("healthcare_dataset2.csv", index=False)


# In[29]:


df.to_csv(r"/Users/jungjungchen/Downloads/healthcare_dataset2.csv", index=False)


# In[ ]:




