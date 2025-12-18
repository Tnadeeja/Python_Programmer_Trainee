# ================================
# DATA VISUALIZATION USING SEABORN
# ================================

# Seaborn is built on top of Matplotlib
# It is high-level, cleaner, and best for statistical visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# Sample Dataset (Same T-shirt data)
# -------------------------------
data = {
    "Size": ["S", "M", "L", "XL", "S", "M", "L", "XL", "M", "L"],
    "Quantity": [10, 20, 15, 5, 8, 12, 18, 7, 25, 22],
    "Price": [1200, 1300, 1400, 1500, 1200, 1300, 1400, 1500, 1300, 1400]
}

df = pd.DataFrame(data)

# Set seaborn style
sns.set(style="whitegrid")

# -------------------------------
# UNIVARIATE VISUALIZATION
# -------------------------------

# COUNT PLOT – Count of T-shirts by Size
sns.countplot(x="Size", data=df)
plt.title("Count of T-Shirts by Size")
plt.show()

# HISTOGRAM – Distribution of Quantity
sns.histplot(df["Quantity"], bins=5, kde=True)
plt.title("Quantity Distribution")
plt.show()

# -------------------------------
# BIVARIATE VISUALIZATION
# -------------------------------

# SCATTER PLOT – Price vs Quantity
sns.scatterplot(x="Price", y="Quantity", hue="Size", data=df)
plt.title("Price vs Quantity by Size")
plt.show()

# BOX PLOT – Quantity by Size
sns.boxplot(x="Size", y="Quantity", data=df)
plt.title("Quantity Spread by Size")
plt.show()

# -------------------------------
# MULTIVARIATE VISUALIZATION
# -------------------------------

# PAIR PLOT – Multiple relationships at once
sns.pairplot(df, hue="Size")
plt.show()

# -------------------------------
# HEATMAP – Correlation Matrix
# -------------------------------
corr = df[["Quantity", "Price"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
