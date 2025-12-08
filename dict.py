# ---------------------------------------------
# 📘 DICTIONARY IN PYTHON
# A dictionary stores data in key–value pairs.
# Example: {"name": "Nadeeja", "age": 22}
# ---------------------------------------------

# ---------------------------------------------
# 1️⃣ Creating Dictionaries
# ---------------------------------------------

# Method 1: Using curly braces
student = {"name": "Nadeeja", "age": 22, "city": "Colombo"}
print(student)

# Method 2: Using dict()
student2 = dict(name="Kamal", age=25, city="Galle")
print(student2)


# ---------------------------------------------
# 2️⃣ Accessing Values (by key)
# ---------------------------------------------

print(student["name"])   # prints "Nadeeja"
print(student.get("city"))  # prints "Colombo" (safe method – avoids errors)


# ---------------------------------------------
# 3️⃣ Adding & Updating Values
# ---------------------------------------------

student["age"] = 23       # update value
student["email"] = "test@gmail.com"  # add new key-value pair
print(student)


# ---------------------------------------------
# 4️⃣ Removing Items
# ---------------------------------------------

student.pop("city")       # removes key = city
print(student)

student.popitem()         # removes last inserted item
print(student)

del student["age"]        # delete key using del
print(student)

student.clear()           # removes ALL key-value pairs
print(student)            # now becomes empty {}


# ---------------------------------------------
# 5️⃣ Looping Through a Dictionary
# ---------------------------------------------

person = {"name": "Alex", "age": 30, "country": "UK"}

# Loop keys
for key in person:
    print(key)

# Loop values
for value in person.values():
    print(value)

# Loop both key and value
for key, value in person.items():
    print(key, "=", value)


# ---------------------------------------------
# 6️⃣ Dictionary Functions
# ---------------------------------------------

my_dict = {"a": 1, "b": 2, "c": 3}

print(len(my_dict))        # number of items
print(my_dict.keys())      # returns all keys
print(my_dict.values())    # returns all values
print(my_dict.items())     # returns key-value pairs as tuples


# ---------------------------------------------
# 7️⃣ Dictionary with Lists (Nested Data)
# ---------------------------------------------

grades = {
    "John": [85, 90, 88],
    "Mala": [75, 80, 82]
}

print(grades["John"])      # prints John's list
print(grades["Mala"][1])   # print 2nd mark of Mala


# ---------------------------------------------
# 8️⃣ Dictionary Inside Dictionary (Nested Dict)
# ---------------------------------------------

students = {
    "s1": {"name": "Nimal", "age": 20},
    "s2": {"name": "Sunil", "age": 22}
}

print(students["s1"]["name"])   # prints "Nimal"
print(students["s2"]["age"])    # prints 22


# ---------------------------------------------
# 9️⃣ Check if Key Exists
# ---------------------------------------------

colors = {"red": 1, "blue": 2}

print("red" in colors)     # True
print("green" in colors)   # False


# ---------------------------------------------
# 🔟 Copying a Dictionary
# ---------------------------------------------

copy_dict = colors.copy()
print(copy_dict)
