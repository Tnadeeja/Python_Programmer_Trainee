# ---------------------------------------------
# 1. Creating Tuples
# ---------------------------------------------

tuple_1 = ('a', 'b', 20, 4.1)   # Using parentheses
print(tuple_1)
print(type(tuple_1))            # <class 'tuple'>

tuple_2 = 'a', 'b', 20, 4.1     # Parentheses optional
print(tuple_2)
print(type(tuple_2))

# Single-element tuple
tuple_3 = ('a')                 # NOT a tuple → string
print(type(tuple_3))

tuple_4 = ('a',)                # Correct single-element tuple
print(type(tuple_4))


# ---------------------------------------------
# 2. Accessing Values (Indexing)
# ---------------------------------------------

my_tuple = (15, 20, 96, 32, 17)

print(my_tuple[0])     # First element → 15
print(my_tuple[4])     # Fifth element → 17

# Negative indexing
print(my_tuple[-1])    # Last element → 17
print(my_tuple[-3])    # Third from end → 96


# ---------------------------------------------
# 3. Slicing
# ---------------------------------------------

print(my_tuple[0:3])   # (15, 20, 96)
print(my_tuple[2:4])   # (96, 32)


# ---------------------------------------------
# 4. Nested Tuples
# ---------------------------------------------

nested = ((1, 2), ('a', 'b'))

print(nested[0][1])    # Access 2
print(nested[1])       # ('a', 'b')


# ---------------------------------------------
# 5. Tuple Packing / Unpacking
# ---------------------------------------------

my_pack = ('car', 'pen', 'ice')   # Packing

a, b, c = my_pack                 # Unpacking
print(b)                          # 'pen'

# NOTE: Variables must match number of items
# a, b = my_pack  → ERROR


# ---------------------------------------------
# 6. Tuple Immutability
# ---------------------------------------------

# Tuples cannot be changed
# my_tuple[0] = 8   → ERROR
# TypeError: 'tuple' object does not support item assignment


# ---------------------------------------------
# 7. Lists vs Tuples (Memory)
# ---------------------------------------------

import sys
my_list = [1,2,3,4,5]
my_tuple2 = (1,2,3,4,5)

print(sys.getsizeof(my_list))   # More memory
print(sys.getsizeof(my_tuple2)) # Less memory


# ---------------------------------------------
# 8. Tuple Operations
# ---------------------------------------------

# Length
print(len((1,2,3)))     # 3

# Concatenation
a = (1,2,3)
b = (4,5,6)
print(a + b)            # (1,2,3,4,5,6)

# Repetition
print(('Hi',) * 4)      # ('Hi','Hi','Hi','Hi')

# Membership
print(3 in (1,2,3))     # True
print(10 in (1,2,3))    # False

# Iteration
for x in (1,2,3):
    print(x)
