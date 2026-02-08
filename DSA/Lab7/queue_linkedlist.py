class Node:
    """Node class for doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    """Queue implementation using doubly linked list"""
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.length = 0
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def enqueue(self, data):
        """Add element to the rear of the queue"""
        new_node = Node(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.length += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Remove and return element from the front of the queue"""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        
        data = self.front.data
        
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.length -= 1
        print(f"Dequeued: {data}")
        return data
    
    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.front.data
    
    def size(self):
        """Return the number of elements in the queue"""
        return self.length
    
    def display(self):
        """Display all elements in the queue"""
        if self.is_empty():
            print("Queue is empty!")
            return
        
        print("Queue (Front -> Rear): ", end="")
        current = self.front
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next


# Example usage
if __name__ == "__main__":
    q = Queue()
    
    print("=== Queue Operations ===")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    
    print(f"\nQueue size: {q.size()}")
    q.display()
    
    print(f"\nFront element: {q.peek()}")
    
    print("\nDequeuing elements:")
    q.dequeue()
    q.dequeue()
    
    q.display()
    print(f"Queue size: {q.size()}")
    
    print("\nAdding more elements:")
    q.enqueue(50)
    q.enqueue(60)
    q.display()
    
    print("\nDequeuing all elements:")
    while not q.is_empty():
        q.dequeue()
    
    q.display()
