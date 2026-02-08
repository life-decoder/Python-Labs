'''
Class Node specifies what each node of the linked list will store
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
    
''' 
Class LinkedList implements the linked list. 
It keeps (1) a reference to the head node , and (2) a variable to keep track of the number of nodes in the linked list

'''
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        # checks if the linked list is empty
        return self.head == None
    
    def traverse(self):
        # traverse the linked list, and prints the elements
        current_node = self.head
        while current_node:     # None is considered as False
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("NULL")
    
    def insertBeginning(self, data):
        # add a node at the beginning of the linked list
        new_node = Node(data)       # create a new node
        new_node.next = self.head   # set its next attribute to point to what head is pointing
        self.head = new_node        # set head to point to the new node
        self.size += 1              # increment the size of the linked list
    
    def insertEnd(self, data):
        # add a node at the end of the linked list
        new_node = Node(data)       # create a new node
        
        if self.head is None:       
            # if the linked list is empty, head points to the new node 
            self.head = new_node
        else:
            # if the linked list is not empty, traverse it to find the last node
            tail = self.head
            while not tail.next:
                tail = tail.next
            tail.next = new_node    # set the next attribute of the last node to point to the new node
        self.size += 1              # increment the size of the linked list

    def insertOrder(self, data):
        # add a node with elements of the linked lisu kept in sorted order
        new_node = Node(data)       # create a new node

        if self.head is None:       
            # if the linked list is empty, head points to the new node
            self.head = new_node
            self.size += 1          # increment the size of the linked list
        elif self.head.data > data: 
            # if the first element in list has key value greater than the element to be added, 
            # the new node is added at the beginning
            self.insertBeginning(data)      # call insertAtBeginning from the same class
        else:
            current_node = self.head;
            previous_node = self.head;        
            while current_node is not None and current_node.data < data:
                previous_node = current_node
                current_node = current_node.next
            new_node.next = current_node
            previous_node.next = new_node
            self.size += 1          # increment the size of the linked list

    def removeFirst(self):
        # remove first node of the linked list
        if self.head is None:           # the list is empty
            return  
        self.head = self.head.next      # link out the node to be deleted
        self.size -= 1                  # decrement the size of the linked list

    def removeLast(self):
        # remove last node of the linked list

        if self.head is None:           # the list s empty
            return        
        else: 
            if self.head.next is None:  # there is only one node
                self.head = None
                return

            # traverse to the second to last node
            current_node = self.head
            while current_node.next and current_node.next.next:
                current_node = current_node.next

            current_node.next = None    # set the next attribute of the second to last node to None
            self.size -= 1              # decrement the size of the linked list

    def remove(self, data):
        # remove a node with a specific element from the linked list 
        current_node = self.head

        # if the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.removeFirst()
            return

        # traverse and find the node to be removed
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                self.size -= 1  # decrement the size of the linked list
                return
            current_node = current_node.next

        # if the data was not found
        print("Node with the given data not found")

    def modifyNode(self, old_data, new_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == old_data:
               current_node.data = new_data
               return True
            current_node = current_node.next
        return False

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node is not None:
            result += str(current_node.data) + " -> "
            current_node = current_node.next
        result += "NULL"
        return result


def main():
    # create a new linked list
    myList = LinkedList()

    print("Initially:- isEmpty?", myList.isEmpty())

    # add nodes to the linked list
    # myList.insertBeginning(1)
    # myList.insertBeginning(2)
    # myList.insertEnd(30)
    myList.insertOrder(10)
    myList.insertOrder(60)
    myList.insertOrder(9)
    myList.insertOrder(15)
    myList.insertOrder(90)
    myList.insertOrder(95)

    # print("After insertion:- isEmpty?", myList.isEmpty())
    # myList.traverse()

    print(myList)
    print("Size:", myList.size)

    print("\nRemove first node:")
    myList.removeFirst()
    print(myList)
    print("Size:", myList.size)

    print("\nRemove last node:")
    myList.removeLast()
    print(myList)
    print("Size:", myList.size)

    print("\nRemove node with element 15:")
    myList.remove(15)
    print(myList)
    print("Size:", myList.size)

    print("\nUpdate node with element 60 to 65:")
    myList.modifyNode(60, 65)
    print(myList)

if __name__ == "__main__":
    # code placed here will only run when the script is executed directly
    # this prevents statements in main from running automatically when the file is imported as a module
    main()