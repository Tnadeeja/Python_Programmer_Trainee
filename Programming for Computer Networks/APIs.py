# =====================================================
# Python Notes: Accessing APIs with Python
# =====================================================

# -----------------------------------------------------
# What is an API?
# -----------------------------------------------------
# API (Application Programming Interface) allows communication
# between two software systems. In web development, this is often
# between a web client (like a browser) and a web server.
# APIs allow sending, retrieving, and modifying data on a server.

# -----------------------------------------------------
# RESTful APIs
# -----------------------------------------------------
# REST APIs (Representational State Transfer) are widely used APIs
# that work over HTTP. You interact with REST APIs by sending HTTP requests.

# Common HTTP methods:
# - GET    : Retrieve existing data
# - POST   : Add new data
# - PUT    : Update existing data
# - PATCH  : Partially update existing data
# - DELETE : Delete data

# -----------------------------------------------------
# Response Codes
# -----------------------------------------------------
# APIs respond with HTTP status codes:
# 1xx: Informational
# 2xx: Success
# 3xx: Redirection
# 4xx: Client error
# 5xx: Server error

# -----------------------------------------------------
# API Endpoints
# -----------------------------------------------------
# Endpoints are public URLs exposed by an API server.
# Example: Vehicle API at base URL https://vehicleapi.com
# - GET /vehicles         : Get all vehicles
# - GET /vehicles/{reg_no}: Get specific vehicle
# - POST /vehicles        : Add new vehicle
# - PUT /vehicles/{reg_no}: Update vehicle completely
# - PATCH /vehicles/{reg_no}: Update vehicle partially
# - DELETE /vehicles/{reg_no}: Delete a vehicle

# -----------------------------------------------------
# Accessing REST APIs with Python Requests
# -----------------------------------------------------
# Install requests library if not already installed:
# pip install requests

import requests

# Base URL for our example API
BASE_URL = "https://vehicleapi.com"

# -----------------------------------------------------
# GET Request (Retrieve Data)
# -----------------------------------------------------
# Example: Get all vehicles
response = requests.get(f"{BASE_URL}/vehicles")
print("GET all vehicles:")
print(response.status_code)  # HTTP status code
# If the API returns JSON, we can use .json() to parse it
# print(response.json())  

# Example: Get a specific vehicle by registration number
reg_no = "CBA4476"
response = requests.get(f"{BASE_URL}/vehicles/{reg_no}")
print("\nGET specific vehicle:")
print(response.status_code)
# print(response.json())

# -----------------------------------------------------
# POST Request (Create Data)
# -----------------------------------------------------
# Add a new vehicle to the API server
vehicle_entity = {
    "motorvehicles": {
        "vehicle": {
            "type": "car",
            "registration_no": "CBB1456",
            "make": "Toyota",
            "model": "Premio"
        },
        "owner": {
            "first_name": "Amal",
            "last_name": "Perera",
            "nic": "900324770V"
        }
    }
}

response = requests.post(f"{BASE_URL}/vehicles", json=vehicle_entity)
print("\nPOST new vehicle:")
print(response.status_code)
# print(response.json())

# -----------------------------------------------------
# PUT Request (Update Entire Record)
# -----------------------------------------------------
# Replace an existing record completely
updated_entity = {
    "motorvehicles": {
        "vehicle": {
            "type": "car",
            "registration_no": "CBB1456",
            "make": "Toyota",
            "model": "Axio"
        },
        "owner": {
            "first_name": "Amal",
            "last_name": "Perera",
            "nic": "900324770V"
        }
    }
}

response = requests.put(f"{BASE_URL}/vehicles/CBB1456", json=updated_entity)
print("\nPUT update vehicle:")
print(response.status_code)
# print(response.json())

# -----------------------------------------------------
# PATCH Request (Partial Update)
# -----------------------------------------------------
# Update only part of an existing record
partial_update = {
    "owner": {
        "first_name": "Marlon",
        "last_name": "Samuels",
        "nic": "870124770V"
    }
}

response = requests.patch(f"{BASE_URL}/vehicles/CBB1456", json=partial_update)
print("\nPATCH partial update vehicle:")
print(response.status_code)
# print(response.json())

# -----------------------------------------------------
# DELETE Request (Delete Data)
# -----------------------------------------------------
# Delete a vehicle record
response = requests.delete(f"{BASE_URL}/vehicles/CBB1456")
print("\nDELETE vehicle:")
print(response.status_code)
# print(response.json())

# =====================================================
# End of Notes: Accessing APIs with Python
# =====================================================
