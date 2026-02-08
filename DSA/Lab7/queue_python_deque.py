# using collections.deque
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print("Queue:", queue)

print("deQueue: ", queue.popleft())

print("Queue after deQueue: ", queue)