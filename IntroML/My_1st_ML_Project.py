# =============================================================
# YOUR FIRST MACHINE LEARNING PROJECT (IRIS DATASET)
# Part 1: Data Loading & Exploration
# Part 2: Model Building, Evaluation & Saving
# =============================================================

# -----------------------------
# 1. IMPORT REQUIRED LIBRARIES
# -----------------------------
# Numerical computations
import numpy as np

# Data handling and analysis
import pandas as pd

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette('husl')

# -----------------------------
# 2. LOAD THE IRIS DATASET
# -----------------------------
# Publicly available Iris dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'

# Column names for the dataset
col_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# Load data into a Pandas DataFrame
dataset = pd.read_csv(url, names=col_name)

# -----------------------------
# 3. EXPLORE THE DATA (PART 1)
# -----------------------------

# Print dataset shape (rows, columns)
print("Dataset Shape:")
print(dataset.shape)

# View first 5 rows
print("\nFirst 5 rows:")
print(dataset.head())

# Summary statistics
print("\nSummary Statistics:")
print(dataset.describe())

# Data types and memory usage
print("\nDataset Info:")
print(dataset.info())

# Number of samples per class
print("\nClass Distribution:")
print(dataset['class'].value_counts())

# -----------------------------
# 4. DATA VISUALIZATION (PART 1)
# -----------------------------

# Violin plots to understand feature distributions
sns.violinplot(y='class', x='sepal-length', data=dataset, inner='quartile')
plt.show()

sns.violinplot(y='class', x='sepal-width', data=dataset, inner='quartile')
plt.show()

sns.violinplot(y='class', x='petal-length', data=dataset, inner='quartile')
plt.show()

sns.violinplot(y='class', x='petal-width', data=dataset, inner='quartile')
plt.show()

# Pair plot to see relationships between features
sns.pairplot(dataset, hue='class', markers='+')
plt.show()

# Correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(dataset.corr(), annot=True, cmap='jet')
plt.show()

# =============================================================
# PART 2: BUILDING THE MACHINE LEARNING MODEL
# =============================================================

# -----------------------------
# 5. SPLIT DATA INTO FEATURES & LABELS
# -----------------------------

# X = features (remove class column)
X = dataset.drop(['class'], axis=1)

# y = labels
y = dataset['class']

print(f'X shape: {X.shape} | y shape: {y.shape}')

# -----------------------------
# 6. TRAIN-TEST SPLIT
# -----------------------------
from sklearn.model_selection import train_test_split

# 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=1
)

# -----------------------------
# 7. TRAIN THE ML MODEL (SVM)
# -----------------------------
from sklearn.svm import SVC

# Create Support Vector Machine classifier
svn = SVC()

# Train the model using training data
svn.fit(X_train, y_train)

# -----------------------------
# 8. MODEL EVALUATION
# -----------------------------

# Predict labels for test data
predictions = svn.predict(X_test)

# Calculate accuracy
from sklearn.metrics import accuracy_score
print("\nModel Accuracy:")
print(accuracy_score(y_test, predictions))

# Detailed evaluation report
from sklearn.metrics import classification_report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# -----------------------------
# 9. CONFUSION MATRIX
# -----------------------------
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, predictions, labels=svn.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svn.classes_)
disp.plot()
plt.show()

# -----------------------------
# 10. SAVE THE TRAINED MODEL
# -----------------------------
import pickle

# Save model to a file
with open('SVM.pickle', 'wb') as f:
    pickle.dump(svn, f)

print("\nModel saved as SVM.pickle")

# -----------------------------
# 11. LOAD & USE SAVED MODEL
# -----------------------------
with open('SVM.pickle', 'rb') as f:
    loaded_model = pickle.load(f)

# Predict again using loaded model
loaded_predictions = loaded_model.predict(X_test)
print("\nPredictions using loaded model:")
print(loaded_predictions)

# =============================================================
# END OF IRIS MACHINE LEARNING PROJECT (PART 1 + PART 2)
# =============================================================
