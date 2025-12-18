"""
# 5.1 Introduction to Machine Learning (Exam‑Focused Notes)

---

## 5.1.1 What is Machine Learning?

**Machine Learning (ML)** is the process of developing systems that can **learn patterns from data** and perform tasks **without being explicitly programmed with rules**.

### Traditional Programming vs Machine Learning

**Traditional Programming**

* We write rules (if–else logic)
* Input data is given
* Program produces output

**Machine Learning**

* We give **data + correct answers (labels)**
* The algorithm learns rules automatically
* A **model** is created
* Model is used to make predictions on new data

**Example (Rain Prediction)**

* Features: Temperature, Humidity, Cloud Cover
* Label: Rain / No Rain
* Instead of writing rules manually, the system learns from past weather data

👉 ML is like learning from solved examples and applying that knowledge to new problems.

---

## 5.1.2 Applications of Machine Learning

Major application areas include:

* **Object Classification** – Cat vs Dog, good vs faulty products
* **Prediction (Regression)** – Temperature, stock prices, exchange rates
* **Recommender Systems** – Facebook, YouTube, Netflix suggestions
* **Transport** – Traffic prediction, self‑driving cars
* **Healthcare** – Disease detection, medical image analysis
* **Finance** – Fraud detection, credit scoring
* **Retail & Entertainment** – Customer behavior analysis

---

## 5.1.3 Why Do We Need Machine Learning?

* Writing rules manually is **difficult and error‑prone**
* Real‑world scenarios change frequently
* Rule‑based systems fail with new or unseen cases
* Large amounts of data are available

✅ ML allows computers to **learn directly from data** and adapt to new situations

---

## 5.1.4 Key Definitions in Machine Learning

| Term          | Description                                           |
| ------------- | ----------------------------------------------------- |
| **Label**     | The output or class to predict (e.g., Rain / No Rain) |
| **Features**  | Input attributes (temperature, humidity, cloud cover) |
| **Examples**  | Labeled data samples                                  |
| **Model**     | Learned system mapping features → labels              |
| **Training**  | Process of building the model using labeled data      |
| **Inference** | Using the trained model to predict new outcomes       |

---

## 5.1.5 Types of Machine Learning

### 1. Supervised Learning

* Data is **labeled**
* Used for **classification & regression**
* Example: Apple vs Orange classification

### 2. Unsupervised Learning

* Data has **no labels**
* Algorithm finds patterns or groups
* Example: Customer segmentation

### 3. Reinforcement Learning

* Learning through **rewards and punishments**
* Agent interacts with environment
* Example: Training a dog, game playing AI

---

## 5.1.6 Machine Learning with Python

Python is ideal for ML because:

* Easy to learn and flexible
* Large ecosystem of ML libraries
* Works well with data
* Supports scripting and large applications

Python allows:

* Quick experimentation
* Repeated model improvements
* Easy visualization and documentation

---

## 5.1.7 Python Libraries and Tools for ML

### Jupyter Notebooks

* Interactive coding in browser
* Combine **code, text, equations, and plots**
* Ideal for experimentation and learning

---

### Scikit‑Learn

* Most popular ML library
* Contains ready‑to‑use ML algorithms
* Simple API
* Built on NumPy and SciPy

---

### NumPy

* Numerical computing library
* Multi‑dimensional arrays
* Linear algebra, random numbers, math operations

---

### SciPy

* Advanced scientific computing
* Optimization, statistics, signal processing
* Used internally by Scikit‑Learn

---

### Pandas

* Data manipulation using **DataFrames**
* Similar to spreadsheets
* Supports CSV, SQL, Excel
* First step in most ML projects

---

### Matplotlib

* Data visualization library
* Create graphs and plots easily
* Supports Jupyter Notebooks

---

### Deep Learning Libraries

* Used for Neural Networks
* Applied in self‑driving cars, NLP, image recognition
* Example use cases: Speech recognition, vision systems

---

## 5.1.8 Summary

* ML allows systems to **learn from data**
* Used widely across industries
* Python makes ML development fast and simple
* Understanding ML basics helps full‑stack developers use ML APIs

ML will **support developers**, not replace them.

---

## 5.1.9 Example: Distance‑Based Classification

### Idea

* Given known data points labeled as **rain** or **no rain**
* Compare a new unknown point to known points
* Assign label of the **closest group**

### Manhattan Distance

```
|x1 − x2| + |y1 − y2|
```

### Euclidean Distance

```
√((x1 − x2)² + (y1 − y2)²)
```

Note:

* Square root can be ignored when only comparing distances
* ML libraries do this automatically via API calls

---

✅ End of Introduction to Machine Learning Notes

"""