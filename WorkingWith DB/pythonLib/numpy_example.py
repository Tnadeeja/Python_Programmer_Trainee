import numpy as np                     # Import NumPy library and give it alias 'np'

print(np.__version__)                  # Print the installed NumPy version

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])  # Create a 1D NumPy array with values 1 to 12
print(arr)                             # Display the array
print(type(arr))                       # Show the type (will be <class 'numpy.ndarray'>)

newArr = arr.reshape(4,3)              # Reshape the 1D array into a 2D array (4 rows, 3 columns)
print(newArr)                          # Print the reshaped 2D array

print(arr[1:8:2])                      # Slice array from index 1 to 7, taking every 2nd element

print(newArr[0,0:2])                   # From first row, get elements from column index 0 to 1
print(newArr[0:3,0])                   # Get first column values from row index 0 to 2
print(newArr[::2,::2])                 # Get every 2nd row and every 2nd column

arr2 = np.array([1,2,1,3,2,1,1,4,2,5,3,4,6,2,3,1,4,5])  # Create another NumPy array
print("Original Array: ", arr2)        # Print original array

a = np.where(arr2==1)                  # Find indexes where value is equal to 1
print("Indexes of element 1: ", a)     # Display the indexes of element 1

b = [True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False]
                                        # Boolean list for filtering elements
c = arr2[b]                            # Filter elements where condition is True
print("Filtered arra: ", c)            # Print filtered array

d = np.sort(arr2)                      # Sort the array in ascending order
print("Sorted array: ", d)             # Display sorted array
