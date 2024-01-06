#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[126]:


df = pd.read_csv("C:\\Users\\SuryaKrishna\\Desktop\\interncareer\\supermarket_sales - Sheet1 (2).csv")
df


# In[127]:


# Handle missing values
df.fillna(method="ffill", inplace=True)
df["Date"] = pd.to_datetime(df["Date"]) 
df["Total Cost"] = df["Quantity"] * df["Unit price"] 


# In[128]:


# Print processed data
print(df.head())


# In[98]:


print(f'There are ')
df.nunique()


# In[135]:


# Calculate summary statistics
df.describe(include=object)  


# In[11]:


df.isnull().sum()


# In[12]:


df.info()


# In[13]:


df['City'].value_counts()


# In[129]:


#remove columns that we dont need
df.drop(columns = ['Invoice ID','Date','Time','cogs','gross margin percentage'],inplace =True)
df


# In[130]:


df.sample(5)


# In[131]:


df['Branch'].unique()


# In[14]:


# Calculate mean of "Total"
total_mean = df["Total"].mean()
print("Mean of Total:", total_mean)
#Calculate median of "Quantity"
quantity_median = df["Quantity"].median()
print("Median of Quantity:", quantity_median)
#Calculate standard deviation of "Unit Price"
unit_price_std = df["Unit price"].std()
print("Standard deviation of Unit Price:", unit_price_std)


# In[102]:


df.max()


# In[136]:


# Calculate the mean, sum, minimum, and maximum of the 'Unit price' for each branch
df.groupby(['Branch']).agg({"Unit price": [np.mean, np.sum, np.min, np.max]})


# In[168]:


# Create a correlation heatmap to visualize the pairwise correlations between numeric columns in the DataFrame
plt.figure(figsize=(10, 10))

# Select only the numeric columns using df.select_dtypes
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix for the numeric columns
correlation_matrix = numeric_df.corr()

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()


# In[183]:


# Pie chart for the distribution of cities
plt.figure(figsize=(10, 4))
df['City'].value_counts().plot.pie(colors=['#1f77b4', '#ff7f0e', '#2ca02c'], autopct='%1.1f%%')
plt.title("Distribution of Cities")
plt.show()


# In[ ]:


#Filtering based 


# In[16]:


filtered_df = df[df["Total"] > 10000]


# In[184]:


# Plot summary statistics
# Histogram of "Total"
plt.figure(figsize=(8, 5))  # Adjust figure size as needed
plt.hist(df["Total"], bins=20, edgecolor="black",color="#008080")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.title("Histogram of Total Sales")
plt.show()


# In[185]:


# Bar chart of branch counts
plt.figure(figsize=(8, 5))
branch_counts = df["Branch"].value_counts()
plt.bar(branch_counts.index, branch_counts.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.xlabel("Branch")
plt.ylabel("Number of Sales")
plt.title("Bar Chart of Branch Sales Counts")
plt.xticks(rotation=45, ha="right")
plt.show()


# In[103]:


# Group the DataFrame by the combination of 'Branch', 'Customer type', and 'Gender' columns
df.groupby(['Branch', 'Customer type', 'Gender']).agg({'Total': 'count'})


# In[143]:


df['Product line'].unique()


# In[144]:


# Group the DataFrame by the 'Product line' column and count the occurrences of each product line in the 'Total' column
df.groupby(['Product line']).agg({'Total': 'count'})


# In[145]:


# Group the DataFrame by the combination of 'Product line' and 'Branch' columns
df.groupby(['Product line', 'Branch']).agg({'Total': 'count'})


# In[137]:


# Filtering data for specific product lines
selected_product_lines = ["Health and beauty", "Home and lifestyle", "Electronic accessories", "Fashion accessories","Sports and travel"]
filtered_df_product_line = df[df["Product line"].isin(selected_product_lines)]


# In[138]:


# Bar chart of product line sales counts
plt.figure(figsize=(15, 6))
product_line_counts = filtered_df_product_line["Product line"].value_counts()
plt.bar(product_line_counts.index, product_line_counts.values)
plt.xlabel("Product Line")
plt.ylabel("Number of Sales")
plt.title("Sales Count for Each Product Line in Filtered Dataset")
plt.xticks(rotation=45, ha="right")
plt.show()


# In[139]:


filtered_df_product_line = df[
    (df["Product line"].isin(["Health and beauty", "Home and lifestyle", "Electronic accessories", "Fashion accessories"])) &
    (df["gross income"]) &
    (df["Rating"])
]


# In[134]:


print(filtered_df_product_line)


# In[65]:


filtered_df_rating = filtered_df[(filtered_df['Rating'] == '7-8') | (filtered_df['Rating'] == '8-9')]


# In[167]:


# Box plot of "Total Sales" for each branch
plt.figure(figsize=(10, 7))
sns.boxplot(x='Branch', y='Total', data=df)
plt.title('Box Plot of Total Sales for Each Branch')
plt.show()


# In[92]:


# Pair plot for selected numeric columns
selected_numeric_cols = ['Total', 'Quantity', 'Unit price', 'Total Cost']
sns.pairplot(df[selected_numeric_cols])
plt.suptitle('Pair Plot of Numeric Columns', y=1.02)
plt.show()


# In[193]:


# Grouped bar chart for payment methods by branch
cash = (110, 104, 126)
credit_card = (110, 109, 113)
ewallet = (124, 98, 106)
X = np.arange(3) 
width = 0.15 
plt.bar(X, cash, width, label='A_Yangon', color="#e377c2")
plt.bar(X + width, credit_card, width, label='B_Mandalay', color="#9467bd")
plt.bar(X + 2*width, ewallet, width, label='C_Naypyitaw', color="#d62728")
plt.xticks(X + width / 2, ("Cash", "Credit card", "Ewallet"))
plt.legend(loc='best')
plt.title("Payment Methods by Branch")
plt.show()


# In[195]:


# Scatterplot for "Rating" vs "Gross Income"
plt.figure(figsize=(10, 10))
sns.scatterplot(x='Rating', y='gross income', color="#1f77b4", data=df)
plt.title("Scatter Plot of Rating vs Gross Income")
plt.show()


# In[146]:


# Save the processed data to a new CSV file
df.to_csv("processed_supermarket_data.csv", index=False)
print("Processed data saved to processed_supermarket_data.csv")


# In[164]:


df.head()

