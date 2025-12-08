'''fruits = {'apple', 'mango', 'orange'}
print(fruits)

fruits = set(['apple', 'mango', 'orange'])
print(fruits)

print(len(fruits))

for i in fruits:
    print(i)

fruits.add('banana')
print(fruits)

fruits.update(['pineapple', 'mangus'])
print(fruits)

fruits.remove('banana')
fruits.discard('pineapple')
print(fruits)

fruits.pop()
print(fruits)'''

#-----------------------------------------#
A=[1,2,3,4,5,6,7]
B=set([5,6,7,8,9])

print(A)
print(B)

# A is a list and B is a set. Use set(A) to convert A to a set before using | (union).
print(set(A) | B)
print(set(A).union(B))

print(set(A) & B)
print(set(A).intersection(B))

print(set(A) - B)
print(set(A).difference(B))