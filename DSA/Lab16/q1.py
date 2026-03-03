""" Implement the program for the 0/1 knapsack problem discussed in class using: """
item = ["Portrait of Elvis", "Ring", "Candelabra", "Radio"]
size = [2, 3, 4, 6]
value = [9, 14, 16, 30]

def q1a(capacity):
    """ Dynamic Programming using Tabulation """
    max_value = [0] * (capacity + 1)
    for i in range(1, capacity+1):
        for j in range(len(item)):
            if size[j] <= i:
                max_value[i] = max(max_value[i], max_value[i - size[j]] + value[j])
    print(max_value[capacity])

def q1b(capacity):
    """ DP Using Memoization """
    max_value = {}
    def knapsack(capacity):
        if capacity in max_value:
            return max_value[capacity]
        if capacity == 0:
            return 0
        max_val = 0
        for j in range(len(item)):
            if size[j] <= capacity:
                max_val = max(max_val, knapsack(capacity - size[j]) + value[j])
        max_value[capacity] = max_val
        return max_val
    print(knapsack(capacity))

if __name__ == "__main__":
    capacity = input("Enter the capacity of the knapsack: ")
    capacity = 10 if not capacity else int(capacity)
    q1a(capacity)
    q1b(capacity)
