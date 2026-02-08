# Using a Python list as a stack
# append() = push, pop() = pop

stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)

# peek
topElement = stack[-1]
print("peek:", topElement)
print("Stack after peek:", stack)

# pop
poppedElement = stack.pop()
print("Popped element:", poppedElement)
print("Stack after pop:", stack)

# isEmpty
isEmpty = len(stack) == 0 # not bool(stack)           # bool([]) = False; bool([1,2,3]) = True
print("Empty?", isEmpty)

#size
print("Stack size:", len(stack))