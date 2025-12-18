# =====================================================
# Python Notes: Introduction to JSON
# =====================================================

# JSON (JavaScript Object Notation) is a text-based data format used
# for exchanging information between web clients and web servers.
# Although inspired by JavaScript, JSON is widely used in many programming languages.

# -----------------------------------------------------
# XML vs JSON
# -----------------------------------------------------
# Both XML and JSON are structured data formats.
# Example comparison:
#
# XML:
# <vehicle>
#     <registration_no>CBB1456</registration_no>
#     <make>Toyota</make>
#     <model>Premio</model>
# </vehicle>
#
# JSON:
# {
#     "vehicle": {
#         "registration_no": "CBB1456",
#         "make": "Toyota",
#         "model": "Premio"
#     }
# }

# -----------------------------------------------------
# JSON Syntax
# -----------------------------------------------------
# - Data is hierarchical (nested)
# - Curly braces {} hold objects (key-value pairs)
# - Colon : separates key and value
# - Comma , separates multiple key-value pairs
# - Square brackets [] hold arrays (lists)
# - Whitespace (spaces, tabs, newlines) is ignored
# - No syntax for comments in JSON

# Example JSON:
example_json = {
    "name": "Amal",
    "age": 25,
    "is_student": True,
    "grades": [90, 85, 92],
    "address": {"city": "Colombo", "country": "Sri Lanka"},
    "phone": None
}

# -----------------------------------------------------
# JSON Data Types
# -----------------------------------------------------
# 1. Number: 123, 3.14
# 2. String: "Hello"
# 3. Boolean: true / false
# 4. Array: [1, 2, 3]
# 5. Object: {"key": "value"}
# 6. Null: null

# -----------------------------------------------------
# Using JSON with Python
# -----------------------------------------------------
# Python has a built-in 'json' library for working with JSON.
# It supports automatic conversion between JSON and Python types:

# JSON -> Python
# object  -> dict
# array   -> list
# string  -> str
# number  -> int / float
# true    -> True
# false   -> False
# null    -> None

import json

# Example Python dictionary (Python object)
vehicle_entity = {
    "motorvehicles": {
        "vehicle": {
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

# -----------------------------------------------------
# Serializing JSON (Python object -> JSON string)
# -----------------------------------------------------
# Use json.dumps() to convert a Python object into a JSON string
serialized = json.dumps(vehicle_entity)
print("Serialized JSON:")
print(serialized)

# You can customize serialization with parameters:
# - indent: pretty printing with indentation
# - sort_keys: sort keys alphabetically
# - separators: control item and key-value separators
pretty_json = json.dumps(vehicle_entity, indent=4, sort_keys=True)
print("\nPretty JSON:")
print(pretty_json)

compact_json = json.dumps([1, 2, 3, {"4": 5, "6": 7}], separators=(',', ':'))
print("\nCompact JSON:")
print(compact_json)

# -----------------------------------------------------
# Deserializing JSON (JSON string -> Python object)
# -----------------------------------------------------
# Use json.loads() to convert a JSON string back into a Python object
restored = json.loads(serialized)
print("\nRestored Python object:")
print(restored)

# -----------------------------------------------------
# Similarities between XML and JSON
# -----------------------------------------------------
# - Used for data exchange
# - Human-readable
# - Supported by most programming languages

# -----------------------------------------------------
# Differences between XML and JSON
# -----------------------------------------------------
# - JSON is lighter and simpler than XML
# - JSON is less verbose
# - XML provides more advanced features (attributes, namespaces)
# - Choice depends on project requirements

# =====================================================
# End of JSON Notes
# =====================================================
