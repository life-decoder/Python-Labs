""" 
from sys import *

myList = [] 
size = 10

# add some values to mylist
for i in range(size):
    myList.append(i)  
    # len(l) gives the length of the list
    # getsizeof(l) gives the memory size of the list object
    print("length {}, memory in bytes {}".format(len(myList), getsizeof(myList)))
"""


from sys import getsizeof
from matplotlib import pyplot as plt

myList = [] 
length = []
memory = []
size = 1000

# add some values to mylist
for i in range(size):
    myList.append(i)
    # len(l) gives the length of the list
    # getsizeof(l) gives the memory size of the list object
    length.append(len(myList))
    memory.append(getsizeof(myList))

plt.plot(length, memory)
plt.title("List length v/s memory")
plt.xlabel("Length")
plt.ylabel("Memory (bytes)")
plt.show()
