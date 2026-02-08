''' Python list '''
'''
myList = [1, "Hello", 1.2, 3+4j]
myList.append(2)  # Add an integer to the end
print(myList)
'''

''' Numpy array '''

import numpy as np
myArray = np.array([1, 2, 3, 4])

# element-wise operations
print(myArray * 2)  

# multi-dimensional array
matrix = np.array([[1, 2], [3, 4]])
print(matrix * 2)

''' Python array '''
'''
import array as arr

# array(data_type, value_list) 
# datatype can be:
#  - 'i' for signed integers, 
#  - 'I' for unsigned integers,
#  - 'f' for single-precision float (typically 4 bytes)
#  - 'd' for double-precision float (typically 8 bytes) 
#  - 'b' for characters
#  - 'u' for strings

myArray = arr.array('i', [1, 2, 3])     

# accessing First Araay
print(myArray[0])

# adding element to array
myArray.append(5)
print(myArray)
'''