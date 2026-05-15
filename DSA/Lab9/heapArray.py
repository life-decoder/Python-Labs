class PriorityQueueArray:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, element):
        self.queue.append(element)
        self.size += 1
    
    def remove(self):
        highestPriority = 0 # stores index of highest priority element
        if self.isEmpty():
            return -1
        for i in range(1, self.size):
            if self.queue[i] > self.queue[highestPriority]:
                highestPriority = i
        tmp = self.queue[highestPriority]
        self.queue[highestPriority] = self.queue[self.size - 1]
        self.queue.pop()
        self.size -= 1
        return tmp
    
def main():
    myQueue = PriorityQueueArray()
    myQueue.insert(2)
    myQueue.insert(23)
    print("Removed",myQueue.remove())
    myQueue.insert(12)
    myQueue.insert(7)
    myQueue.insert(13)
    myQueue.insert(29)
    myQueue.insert(50)
    myQueue.insert(2)
    myQueue.insert(23)
    print("Removed",myQueue.remove())
    print("Removed",myQueue.remove())
    print("Removed",myQueue.remove())
        
if __name__ == "__main__":
    # code placed here will only run when the script is executed directly
    # this prevents statements in main from running automatically when the file is imported as a module
    main()