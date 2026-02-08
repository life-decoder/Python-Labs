from queue import LifoQueue

# Creating a stack --- set the maximum number of elements of the stack using maxsize
stack = LifoQueue(maxsize=3)

# check if stack is empty
print("Empty?", stack.empty())

print("Size of stack:", stack.qsize())

# check if there are maxsize items in the stack
print("Full?", stack.full())

print("Pushing elements onto the stack")
stack.put_nowait(10)
stack.put_nowait(20)
stack.put_nowait(30)

print("Full?", stack.full())

print('Elements popped from the stack')
print(stack.get_nowait())
print(stack.get_nowait())
print(stack.get_nowait())

print("Empty?", stack.empty())