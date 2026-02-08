class Node:
    """Node class for circular linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Circular Linked List implementation"""
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the list"""
        new_node = Node(data)
        
        if self.is_empty():
            new_node.next = new_node  # Point to itself
            self.head = new_node
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a node at the end of the list"""
        new_node = Node(data)
        
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
    
    def insert_at_position(self, data, position):
        """Insert a node at a specific position (0-indexed)"""
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for i in range(position - 1):
            if current.next == self.head:
                print("Position out of bounds")
                return
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        """Delete the first node"""
        if self.is_empty():
            print("List is empty")
            return
        
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = self.head.next
            self.head = self.head.next
    
    def delete_at_end(self):
        """Delete the last node"""
        if self.is_empty():
            print("List is empty")
            return
        
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            
            current.next = self.head
    
    def delete_by_value(self, value):
        """Delete a node with specific value"""
        if self.is_empty():
            print("List is empty")
            return
        
        # If head node holds the value
        if self.head.data == value:
            self.delete_at_beginning()
            return
        
        current = self.head
        while current.next != self.head:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        
        print(f"Value {value} not found in the list")
    
    def search(self, value):
        """Search for a value in the list"""
        if self.is_empty():
            return False
        
        current = self.head
        while True:
            if current.data == value:
                return True
            current = current.next
            if current == self.head:
                break
        
        return False
    
    def length(self):
        """Return the length of the list"""
        if self.is_empty():
            return 0
        
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        
        return count
    
    def display(self):
        """Display the circular linked list"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        elements = []
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        
        print(" -> ".join(elements) + " -> (back to head)")


# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    # Insert elements
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_beginning(5)
    
    print("Circular Linked List:")
    cll.display()
    
    print(f"\nLength: {cll.length()}")
    
    # Search
    print(f"Search 20: {cll.search(20)}")
    print(f"Search 100: {cll.search(100)}")
    
    # Insert at position
    cll.insert_at_position(15, 2)
    print("\nAfter inserting 15 at position 2:")
    cll.display()
    
    # Delete operations
    cll.delete_at_beginning()
    print("\nAfter deleting at beginning:")
    cll.display()
    
    cll.delete_by_value(20)
    print("\nAfter deleting value 20:")
    cll.display()
