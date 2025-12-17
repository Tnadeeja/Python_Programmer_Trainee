import pandas as pd
import numpy as np

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

# Create a dictionary
a_dict = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5, '6th':6, '7th':7, '8th':8}
print("Original dictionary:")
print(a_dict)

# Create a pandas Series from the dictionary
ser = pd.Series(a_dict)
print("\nPandas Series:")
print(ser)

# Accessing elements by position (integer-based indexing)
print("\n1. First 3 elements (using integer position - iloc):")
print(ser.iloc[0:3])  # Gets elements at positions 0, 1, and 2

# Accessing elements by label
print("\n2. Elements from '1st' to '3rd' (using label - loc):")
print(ser.loc['1st':'3rd'])  # Note: This is inclusive of the end label

# Using direct indexing (behaves like loc for labels)
print("\n3. Elements from '1st' to '3rd' (using direct indexing):")
print(ser['1st':'3rd'])  # Same as loc for label-based access

# Getting values by position using .values
print("\n4. First 3 values (using .values and array indexing):")
print(ser.values[0:3])  # Returns a numpy array of the first 3 values
# This won't work as expected with string indices
# print(ser[0:3])  # This would raise a KeyError

