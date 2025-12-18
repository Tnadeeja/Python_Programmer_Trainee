"""
## What is Web Scraping?

**Web Scraping** is the process of **extracting specific information from web pages**.
Web pages are written in **HTML**, which can be complex and difficult to read directly.

To understand a web page structure:

* Use **Browser Inspect Tool**

  * Right Click → Inspect
  * Or press **Ctrl + Shift + I**
  * Use **Ctrl + Shift + C** to select elements

This helps identify:

* HTML tags (`h3`, `a`, `div`, etc.)
* Attributes (`class`, `id`, `href`)

---

## BeautifulSoup4

**BeautifulSoup** is a Python library used to:

* Parse HTML documents
* Navigate the DOM tree
* Search and extract tags easily

Official documentation:
[https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Installation

```bash
pip install beautifulsoup4
```

### Import

```python
from bs4 import BeautifulSoup
```

---

## Creating a BeautifulSoup Object

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
```

* `html_doc` → HTML content as string/bytes
* `'html.parser'` → built-in Python HTML parser

The **BeautifulSoup object** represents the page as a **nested data structure**.

---

## Basic Navigation Examples

```python
print(soup.title)              # Prints the <title> tag
print(soup.title.name)         # Tag name: title
print(soup.title.string)       # Text inside the tag
print(soup.title.parent.name)  # Parent tag name

print(soup.p)                  # First <p> tag
print(soup.p['class'])         # Class attribute of <p>

print(soup.a)                  # First <a> tag
```

---

## Finding Multiple Tags

```python
links = soup.find_all('a')     # Find all anchor tags

for link in links:
    print(link)
```

---

## Finding by ID

```python
print(soup.find(id="link3"))
```

---

## Navigating the DOM Tree

### Children of a Tag

```python
children = soup.p.parent.children
for child in children:
    print('Child:', child)
```

### Sibling Navigation

```python
print('Sibling:', soup.p.next_sibling.next_sibling)
```

---

## Web Scraping with Requests + BeautifulSoup

### Step 1: Fetch Web Page

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=Sri+Lanka'
html = requests.get(url).content
```

### Step 2: Parse HTML

```python
soup = BeautifulSoup(html, 'html.parser')
```

---

## Extracting Google Search Results (Titles & Links)

After inspecting the page:

* Search result titles are inside **`<h3>` tags**
* Links are near the title in parent elements

```python
# Get all heading tags
headings = soup('h3')

for heading in headings:
    # Extract title text
    print(heading.find('div').text)
    
    # Extract related link
    print(heading.parent.get('href'))
    print("\n")
```

✔ Extracts **search result title**
✔ Extracts **corresponding URL**

---

## Important Notes (Exams)

* Web scraping involves **HTML parsing**
* Use **Inspect Tool** to find correct tags
* `requests` → fetch page
* `BeautifulSoup` → parse & navigate
* `find()` → first match
* `find_all()` → all matches
* Google results usually load dynamically (may change)

⚠️ Excessive scraping may violate website terms

---

## Limitation

* Only retrieves **first page** of results
* For next pages, additional **GET parameters** are needed (e.g., `start=10`)

---

✅ End of Web Scraping in Python (One Sheet)
"""