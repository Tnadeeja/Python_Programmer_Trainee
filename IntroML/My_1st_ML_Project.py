# ==========================================
# STEP 1: Import required libraries
# ==========================================

import numpy as np                    # Numerical computations
import pandas as pd                   # Data handling using DataFrames
import seaborn as sns                 # Statistical data visualization
import matplotlib.pyplot as plt       # Plotting graphs

sns.set_palette('husl')               # Set color palette for plots

# (This line is used only in Jupyter / Colab notebooks)
# %matplotlib inline


# ==========================================
# STEP 2: Load the Iris dataset
# ==========================================

# Dataset URL
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'

# Column names for the dataset
col_name = [
    'sepal-length',
    'sepal-width',
    'petal-length',
    'petal-width',
    'class'
]

# Load dataset into a Pandas DataFrame
dataset = pd.read_csv(url, names=col_name)


# ==========================================
# STEP 3: Basic inspection of the dataset
# ==========================================

# Print dataset dimensions (rows, columns)
print(dataset.shape)

# Display first 5 rows of the dataset
print(dataset.head())


# ==========================================
# STEP 4: Summary statistics
# ==========================================

# Display statistical summary of numerical columns
print(dataset.describe())


# ==========================================
# STEP 5: Dataset information
# ==========================================

# Display data types and memory usage
print(dataset.info())


# ==========================================
# STEP 6: Class distribution
# ==========================================

# Count number of samples in each class
print(dataset['class'].value_counts())


# ==========================================
# STEP 7: Data visualization – Violin plots
# ==========================================

# Violin plot for Sepal Length
sns.violinplot(y='class', x='sepal-length', data=dataset, inner='quartile')
plt.show()

# Violin plot for Sepal Width
sns.violinplot(y='class', x='sepal-width', data=dataset, inner='quartile')
plt.show()

# Violin plot for Petal Length
sns.violinplot(y='class', x='petal-length', data=dataset, inner='quartile')
plt.show()

# Violin plot for Petal Width
sns.violinplot(y='class', x='petal-width', data=dataset, inner='quartile')
plt.show()


# ==========================================
# STEP 8: Pair plot (Bivariate analysis)
# ==========================================

# Pair plot showing relationships between attributes
sns.pairplot(dataset, hue='class', markers='+')
plt.show()


# ==========================================
# STEP 9: Correlation heatmap
# ==========================================

# Set figure size
plt.figure(figsize=(7, 5))

# Plot correlation heatmap
sns.heatmap(dataset.corr(), annot=True, cmap='jet')

plt.show()
