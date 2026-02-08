class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty(): 
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        '''
        list(map(str,[1,2,3])) => ['1', '2', '3']
        ",".join(['1', '2', '3']) => '1,2,3'
        '''
        if self.isEmpty(): return "Queue: is empty!"
        return "Queue: (front) " + ", " . join(map(str, self.queue)) + " (rear)"
    
def main():
    myQueue = Queue()

    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)

    print("Queue: ", myQueue)
    print("Peek: ", myQueue.peek())
    print("dequeue: ", myQueue.dequeue())
    print("Queue after Dequeue: ", myQueue)
    print("Empty? ", myQueue.isEmpty())
    print("Size: ", myQueue.size())

if __name__ == "__main__":
    main()