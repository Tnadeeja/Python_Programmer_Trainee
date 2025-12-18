"""
# HTTP Requests in Python (One Sheet – Exam Ready)

---

## Introduction

In Python, the **`requests`** library is the most popular and easiest way to work with **HTTP requests**.
It allows Python programs to act as **HTTP clients**, similar to a web browser.

Using `requests`, we can:

* Send **GET** requests
* Send **POST** requests
* Pass **query parameters**
* Read **response content**, headers, and status codes

---

## Installing and Importing Requests

```bash
pip install requests
```

```python
import requests
```

---

## HTTP GET Request with Parameters (Example)

Below is your **original code**, updated with **clear comments for every line** (code logic NOT changed).

```python
import requests                 # Import the requests library to work with HTTP

# Dictionary containing query parameters for the GET request
# 'q' is the search query parameter used by Google
payload = {'q': 'sri+lanka'}

# Send an HTTP GET request to Google Search
# params=payload automatically appends parameters to the URL
r = requests.get('https://www.google.com/search?', params=payload)

# Print the final URL after parameters are encoded and attached
print(r.url)

# Print the response body (HTML content of the page)
print(r.text)
```

---

## What Happens Internally?

1. Python creates an **HTTP GET request**
2. Query parameters are appended to the URL
3. Request is sent over **TCP (port 443 – HTTPS)**
4. Google server processes the request
5. Server sends an HTTP response
6. Response is stored inside object `r`

---

## Generated URL Example

```text
https://www.google.com/search?q=sri%2Blanka
```

✔ `%2B` is the URL-encoded form of `+`
✔ URL encoding is handled automatically by `requests`

---

## Commonly Used Response Attributes

```python
r.status_code     # HTTP status code (e.g., 200, 404)
r.text            # Response body as text (HTML)
r.content         # Response body as bytes
r.headers         # Response headers
```

---

## HTTP Status Code Example

```python
print(r.status_code)
```

* **200** → Request successful
* **404** → Page not found
* **403** → Access forbidden

---

## Why Use `requests` Instead of Sockets?

| Feature       | socket    | requests   |
| ------------- | --------- | ---------- |
| Level         | Low-level | High-level |
| Ease of use   | Hard      | Easy       |
| HTTP handling | Manual    | Automatic  |
| Headers       | Manual    | Automatic  |
| SSL           | Manual    | Automatic  |

✔ `requests` is preferred for **real applications**
✔ `socket` is preferred for **learning protocols & exams**

---

## Key Exam Points

* `requests` is a **high-level HTTP client library**
* Automatically handles:

  * URL encoding
  * Headers
  * HTTPS
* GET parameters are passed using `params={}`
* Response is stored in a **Response object**

---

✅ End of HTTP Requests in Python (One Sheet)
"""