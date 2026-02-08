# using Python list
queue = []

queue.append(1)
queue.append(2)
queue.append(3)

# peek
frontElement = queue[0]
print("Peek: ", frontElement)

print("Queue after peek: ", queue)

# dequeue
frontElement = queue.pop(0)
print("Dequeue: ", frontElement)
print("Queue after dequeue: ", queue)

# isEmpty
isEmpty = len(queue) == 0 # not bool(queue)           # bool([]) = False; bool([1,2,3]) = True

print("Empty? ", isEmpty)

# size
print("Size: ", len(queue))
