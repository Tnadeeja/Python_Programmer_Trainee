# TCP Sockets & HTTP (One Sheet – Exam Ready)

---

## Introduction to HTTP

**HTTP (Hyper Text Transfer Protocol)** is an **application-layer protocol** used for communication between **web browsers (clients)** and **web servers**.
It works **on top of TCP**, usually on:

* **Port 80** → HTTP
* **Port 443** → HTTPS (HTTP over TLS)

HTTP follows a **request–response model**:

* Client sends a request
* Server sends a response

Common HTTP methods:

* **GET** – request data from server
* **POST** – send data to server
* **PUT** – update data
* **DELETE** – remove data
* **OPTIONS** – check allowed methods

---

## HTTP GET Method

The **GET method** is used to **request resources** from a server.
A GET request is a **plain text string** sent over a TCP socket.

### Basic GET Request Format

```
GET / HTTP/1.1
Host: example.com
Connection: close


```

### Explanation (First Line)

* **GET** → HTTP method
* **/** → requested resource (usually index.html)
* **HTTP/1.1** → protocol version

⚠️ There must be **exactly one space** between parts.
⚠️ Request must end with **two newline characters (\n\n)**.

---

## GET Method with Parameters

GET requests can send parameters via the URL.

### Example URL

```
https://www.google.com/search?q=Sri+Lanka&hl=SI
```

### Components

* `?` → start of parameters
* `q=Sri+Lanka` → search query
* `hl=SI` → language
* `&` → separator for multiple parameters

### Equivalent HTTP GET Request

```
GET /search?q=Sri+Lanka&hl=SI HTTP/2
Host: www.google.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive
```

---

## HTTP Response Status Codes

Common HTTP status codes:

* **200 OK** → request successful
* **301 Moved Permanently** → resource moved
* **302 Found** → temporary redirect
* **403 Forbidden** → access denied
* **404 Not Found** → resource not found
* **451 Unavailable** → unavailable for legal reasons

Status codes indicate **result of the request**.

---

## HTTP POST Method

The **POST method** is used to **send data to the server**.

### Basic POST Request

```
POST / HTTP/1.1
Host: example.com
Content-Length: 0
Connection: close

[payload data]
```

### POST Payload

* Sent **after headers**
* Can include:

  * username & password
  * form data
  * JSON
  * files or images

---

## HTTP over TCP Socket (Python Example)

### GET Request using TCP Socket

```python
import socket

host = "example.com"
port = 80

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to web server
s.connect((host, port))

# HTTP GET request
request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"

# Send request
s.send(request.encode())

# Receive response
response = s.recv(4096)
print(response.decode())

# Close connection
s.close()
```

✔ Shows HTTP running **on top of TCP**
✔ Useful for exams and low-level understanding

---

## TCP vs HTTP (Quick View)

| Feature     | TCP            | HTTP                 |
| ----------- | -------------- | -------------------- |
| Layer       | Transport      | Application          |
| Reliable    | Yes            | Uses TCP reliability |
| Connection  | Stateful       | Stateless            |
| Data Format | Raw bytes      | Text-based protocol  |
| Usage       | Data transport | Web communication    |

---

## Key Exam Points

* HTTP is an **application-layer protocol**
* HTTP works **on top of TCP sockets**
* GET sends data via **URL parameters**
* POST sends data via **request body**
* HTTP is **stateless**
* Status codes indicate request result

---

✅ End of One-Sheet HTTP Note
