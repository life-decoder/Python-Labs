# using queue.Queue

from queue import Queue
queue = Queue(maxsize=3)
print("Initial size:", queue.qsize())

queue.put(1)
queue.put(2)
queue.put(3)
print("iFull? ", queue.full())

print("deQueue:", queue.get())
print("deQueue:", queue.get())
print("deQueue:", queue.get())
print("isEmpty?", queue.empty())