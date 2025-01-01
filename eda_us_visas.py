
"""EDA on US Visa Applications Dataset

This notebook performs exploratory data analysis on the US visa applications dataset.
The analysis includes data cleaning, visualization, and insights generation.

"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppressing warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv("us_perm_visas.csv")

# Display the first few rows of the dataset
print("Dataset Overview:")
print(df.head())

# Display the shape of the dataset
print(f"Dataset Shape: {df.shape}")

# Display the columns in the dataset
print("Columns in the dataset:")
print(df.columns.values)

# Data Cleaning
# Checking for unique case numbers
print(f"Unique case numbers: {df['case_no'].nunique()}")

# Dropping unnecessary columns
df.drop(['case_no', 'case_number'], axis=1, inplace=True)

# Handling missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Dropping rows with 'Withdrawn' status
df = df[df.case_status != 'Withdrawn']

# Normalizing case status
df.loc[df.case_status == 'Certified-Expired', 'case_status'] = 'Certified'

# Visualizing case status distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='case_status', data=df)
plt.title('Distribution of Case Status')
plt.xlabel('Case Status')
plt.ylabel('Count')
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Year-wise visa status analysis
df['decision_date'] = pd.to_datetime(df['decision_date'])
df['year'] = df['decision_date'].dt.year

plt.figure(figsize=(10, 6))
sns.countplot(x='year', hue='case_status', data=df)
plt.title('Year-wise Visa Status')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Case Status')
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Employer city analysis
df['employer_city'] = df['employer_city'].str.upper()
top_cities = df['employer_city'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.countplot(x='employer_city', data=df, order=top_cities.index)
plt.title('Top Employer Cities')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Job title analysis
df['job_info_job_title'] = df['job_info_job_title'].str.lower().str.split('-').str[0].str.strip()
top_job_titles = df['job_info_job_title'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_job_titles.index, y=top_job_titles.values)
plt.title('Top Job Titles by Visa Applications')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Country of citizenship analysis
top_countries = df['country_of_citizenship'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.countplot(x='country_of_citizenship', hue='case_status', data=df,
              order=top_countries.index)
plt.title('Top Countries of Citizenship')
plt.xlabel('Country of Citizenship')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Case Status')
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Application type analysis
top_application_types = df['application_type'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.countplot(x='application_type', data=df, order=top_application_types.index)
plt.title('Top Application Types')
plt.xlabel('Application Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Education level analysis
top_education_levels = df['foreign_worker_info_education'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.countplot(x='foreign_worker_info_education', data=df,
              order=top_education_levels.index)
plt.title('Top Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()  # Ensures the labels are not cut off
plt.show()

# Final Data Preparation
# Encoding categorical variables
from sklearn.preprocessing import LabelEncoder

for col in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))

# Display the final dataset info
print("Final Dataset Info:")
print(df.info())

# Save the cleaned dataset for future use
df.to_csv("cleaned_us_perm_visas.csv", index=False)
print("Cleaned dataset saved as 'cleaned_us_perm_visas.csv'.")
