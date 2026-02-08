
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def push(self, data):
        newNode = Node(data)
        if not self.isEmpty():
            newNode.next = self.top
        self.top = newNode
        self.size += 1

    def peek(self):
        if self.isEmpty(): return None
        return str(self.top)

    def pop(self):
        if self.isEmpty(): return None
        poppedElement = self.top
        self.top = self.top.next
        self.size -= 1
        return poppedElement
    
    # def size(self):
    #     return self.size
    
    def __str__(self):
        if self.isEmpty():
            return "Stack is empty!"
        
        result = "Stack: (top) "
        current = self.top
        while current:
            result += str(current.data) + ", "
            current = current.next
        return result[:-2] # ignore the last ", "

def main():
    myStack = Stack()
    print(myStack)
    print(myStack.peek())

    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack)

    topElement = myStack.peek()
    print("Peek:", topElement)
    print(myStack)

    topElement = myStack.pop()
    print("Pop:", topElement)
    print(myStack)

if __name__ == "__main__":
    main()