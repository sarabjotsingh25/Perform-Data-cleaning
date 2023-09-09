import pandas as pd
import numpy as np
# Replace 'your_dataset.csv' with the actual path to your dataset file.

df = pd.read_csv('data.csv')
# Check for missing values in the dataset

missing_values = df.isnull().sum()
print(missing_values)
# Remove rows with any missing values

df_cleaned = df.dropna()
# Replace missing values with the mean of the column

df['column_name'].fillna(df['column_name'].mean(), inplace=True)
# Calculate the IQR for a specific column

Q1 = df['column_name'].quantile(0.25)
Q3 = df['column_name'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find the outliers

outliers = df[(df['column_name'] < lower_bound) | (df['column_name'] > upper_bound)]
# Remove outliers from the DataFrame

df_no_outliers = df[(df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound)]
# Save the cleaned dataset to a new CSV file

df_cleaned.to_csv('cleaned_data.csv', index=False)
