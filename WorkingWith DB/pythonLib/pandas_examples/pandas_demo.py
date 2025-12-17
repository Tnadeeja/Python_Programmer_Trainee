"""
import pandas as pd  # Import Pandas library
import numpy as np   # Import NumPy library

# Print library versions for reference
print("Pandas version:", pd.__version__)  # Shows installed pandas version
print("NumPy version:", np.__version__)   # Shows installed numpy version

# -------------------------------
# SERIES: 1D Labeled Array in Pandas
# -------------------------------

# Create a dictionary as sample data
a_dict = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5, '6th':6, '7th':7, '8th':8}
print("Original dictionary:")
print(a_dict)

# Convert dictionary to Pandas Series
ser = pd.Series(a_dict)  # Series = 1D array with labels (index) and values
print("\nPandas Series:")
print(ser)

# Accessing elements by integer-based position (iloc)
print("\n1. First 3 elements (using integer position - iloc):")
print(ser.iloc[0:3])  # iloc = purely integer-based indexing

# Accessing elements by label (loc)
print("\n2. Elements from '1st' to '3rd' (using label - loc):")
print(ser.loc['1st':'3rd'])  # loc = label-based indexing (end label included)

# Direct indexing behaves like loc
print("\n3. Elements from '1st' to '3rd' (using direct indexing):")
print(ser['1st':'3rd'])

# Getting values as a NumPy array
print("\n4. First 3 values (using .values and array indexing):")
print(ser.values[0:3])  # Returns numpy array of values

# -------------------------------
# DATAFRAME: 2D Labeled Data Structure
# -------------------------------

# Create a sample DataFrame using dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "Age": [25, 30, 35, 40, 28, 33, 38],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Duration": [100, 130, 120, 150, 110, 125, 140]
}
df = pd.DataFrame(data)  # DataFrame = 2D table with rows & columns
print("\nSample DataFrame:")
print(df)

# -------------------------------
# Analyzing DataFrames
# -------------------------------
print("\nFirst 5 rows using head():")
print(df.head(5))  # head() = returns top n rows (default 5)

print("\nSummary statistics using describe():")
print(df.describe())  # summarize numeric columns

# -------------------------------
# Cleaning Data
# -------------------------------

# Handling Empty Cells
df.loc[2, "Age"] = np.nan  # Simulate a missing value
print("\nDataFrame with a missing value:")
print(df)

# Remove rows with any missing values
df_cleaned = df.dropna()  # dropna() = remove rows with empty cells
print("\nDataFrame after dropping rows with missing values:")
print(df_cleaned)

# Replace missing values with a default
df.fillna({"Age": 0}, inplace=True)  # fillna() = replace missing values
print("\nDataFrame after filling missing Age with 0:")
print(df)

# -------------------------------
# Fixing Values in DataFrame
# -------------------------------

# Suppose Duration cannot exceed 120, cap values at 120
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print("\nDataFrame after fixing Duration > 120:")
print(df)

# -------------------------------
# Handling Duplicates
# -------------------------------

# Introduce duplicate row
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("\nDataFrame with duplicate row added:")
print(df)

# Detect duplicates
print("\nCheck for duplicate rows (True = duplicate):")
print(df.duplicated())

# Remove duplicates
df.drop_duplicates(inplace=True)
print("\nDataFrame after removing duplicates:")
print(df)

# -------------------------------
# Reading CSV File (Optional)
# -------------------------------
# df_csv = pd.read_csv('data.csv')  # Load CSV file as DataFrame
# print(df_csv.head(10))  # Show first 10 rows
"""
import numpy as np 
a = np.array([1,2,3]) 
print(a)