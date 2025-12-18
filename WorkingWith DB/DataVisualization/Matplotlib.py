# ================================
# DATA VISUALIZATION USING MATPLOTLIB
# ================================

# Matplotlib is a low-level plotting library in Python
# It gives full control over plots (manual but powerful)

import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# Sample Dataset (T-shirt stock)
# -------------------------------
data = {
    "Size": ["S", "M", "L", "XL", "S", "M", "L", "XL", "M", "L"],
    "Quantity": [10, 20, 15, 5, 8, 12, 18, 7, 25, 22],
    "Price": [1200, 1300, 1400, 1500, 1200, 1300, 1400, 1500, 1300, 1400]
}

df = pd.DataFrame(data)
print(df)

# -------------------------------
# UNIVARIATE VISUALIZATION
# (Single variable)
# -------------------------------

# PIE CHART – Stock percentage by Size
size_count = df.groupby("Size")["Quantity"].sum()

plt.figure()
plt.pie(size_count, labels=size_count.index, autopct='%1.1f%%')
plt.title("T-Shirt Stock Percentage by Size")
plt.show()

# -------------------------------
# BAR CHART – Quantity by Size
# -------------------------------
plt.figure()
plt.bar(size_count.index, size_count.values)
plt.xlabel("Size")
plt.ylabel("Total Quantity")
plt.title("Total T-Shirts by Size")
plt.show()

# -------------------------------
# BIVARIATE VISUALIZATION
# (Two variables)
# -------------------------------

# SCATTER PLOT – Price vs Quantity
plt.figure()
plt.scatter(df["Price"], df["Quantity"])
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.title("Price vs Quantity")
plt.show()

# -------------------------------
# GROUPED BAR CHART
# -------------------------------
grouped = df.groupby(["Size"]).sum()

plt.figure()
plt.bar(grouped.index, grouped["Quantity"])
plt.bar(grouped.index, grouped["Price"], bottom=grouped["Quantity"])
plt.xlabel("Size")
plt.ylabel("Value")
plt.title("Stacked Bar Chart (Quantity + Price)")
plt.show()

# -------------------------------
# SUBPLOTS (Multiple charts)
# -------------------------------
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.bar(size_count.index, size_count.values)
plt.title("Bar Chart")

plt.subplot(1,2,2)
plt.pie(size_count, labels=size_count.index, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.show()
