'''
While Python lists can be used as stacks, creating a dedicated Stack class provides better 
encapsulation and additional functionality
'''

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if self.isEmpty(): 
            raise IndexError("Cannot peek from empty stack!")
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty(): 
            raise IndexError("Cannot pop from empty stack!")
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        '''
        list(map(str,[1,2,3])) => ['1', '2', '3']
        ",".join(['1', '2', '3']) => '1,2,3'
        '''
        if self.isEmpty(): return "Stack: is empty!"
        return "Stack: " + ", " . join(map(str, self.stack)) + " (top)"
    
def main():
    myStack = Stack()
    print(myStack)
    # print(myStack.peek())

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