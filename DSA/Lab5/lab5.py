'''Divide and Conquer Labsheet Solutions'''
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

def q3():
    def find_peak(arr, left=0, right=None):
        """Finds a peak element in the array and returns its index.
        A peak element is greater than or equal to its neighbors."""
        if right is None:
            right = len(arr) - 1
        
        # Base case: single element
        if left == right:
            return left
        
        mid = (left + right) // 2
        
        # Check if mid is a peak (greater than or equal to neighbors)
        is_peak = True
        
        # Compare with left neighbor
        if mid > 0 and arr[mid] < arr[mid - 1]:
            is_peak = False
        
        # Compare with right neighbor
        if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            is_peak = False
        
        if is_peak:
            return mid
        
        # If right neighbor is greater, search right half (guaranteed to find peak)
        if mid < len(arr) - 1 and arr[mid + 1] > arr[mid]:
            return find_peak(arr, mid + 1, right)
        # Otherwise, search left half
        else:
            return find_peak(arr, left, mid - 1)
    
    # Test cases
    test_cases = [
        [10, 12, 15, 5, 7, 8],
        [7, 12, 15, 18, 25],
        [25, 8, 5, 4, 3, 1]
    ]
    
    for arr in test_cases:
        peak_index = find_peak(arr)
        print(f"Input: {arr}")
        print(f"Output: The peak element is {arr[peak_index]} at index {peak_index}\n")

def q2():
    def count_alt(nums, key, left=0, right = None):
        if right is None:
            right = len(nums) - 1
        if left > right:
            return 0
        mid = (left + right) // 2
        if key > nums[mid]:
            return count_alt(nums, key, mid + 1, right)
        elif key < nums[mid]:
            return count_alt(nums, key, left, mid - 1)
        else:
            return 1 + count_alt(nums, key, left, mid - 1) + count_alt(nums, key, mid + 1, right)

    
    def count(nums, num):
        if len(nums) < 1:
            return 0
        
        mid = len(nums) // 2

        if num > nums[mid]:
            return count(nums[mid+1:], num)
        elif num < nums[mid]:
            return count(nums[:mid], num)
        else:
            return 1 + count(nums[:mid], num) + count(nums[mid+1:], num)

    nums = [1, 1, 2,2,2,2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10]
    num = int(input("Enter a number to count: "))
    #print(f"The number {num} appears {count(nums, num)} times in the list.")
    print(f"The number {num} appears {count_alt(nums, num)} times in the list.")

def q1a():
    def max_min(arr, left=0, right=None):
        '''Calculates the maximum and minimum values in an array'''
        if right is None:
            right = len(arr) - 1
        
        # Base case: single element
        if left == right:
            return arr[left], arr[left]
        
        # Base case: two elements
        if right == left + 1:
            return max(arr[left], arr[right]), min(arr[left], arr[right])
        
        mid = (left + right) // 2
        
        left_max, left_min = max_min(arr, left, mid)
        right_max, right_min = max_min(arr, mid + 1, right)
        
        return max(left_max, right_max), min(left_min, right_min)

    # Test cases
    test_cases = [
        [3, 5, 1, 8, 2, 7],
        [10, 20, 30, 40, 50],    
        [5, 4, 3, 2, 1]
    ]
    for arr in test_cases:
        maximum, minimum = max_min(arr)
        print(f"Input: {arr}")
        print(f"Output: Maximum = {maximum}, Minimum = {minimum}\n")
    def q1b():
    def power(base, exp):
        '''Returns base raised to the power of exp'''
        if exp < 0:
            return 1 / power(base, -exp)
        if exp == 0:
            return 1
        if exp == 1:
            return base
        
        half_power = power(base, exp // 2)

        if exp % 2 == 0:
            return half_power * half_power
        else:
            return base * half_power * half_power

    # Test cases
    test_cases = [(2, 10),(3, -3),(5, 0)]

    for base, exp in test_cases:
        result = power(base, exp)
        print(f"Input: base = {base}, exponent = {exp}")
        print(f"Output: {base}^{exp} = {result}\n")
def q1c():
    def strassen_matrix_mult(A, B):
        '''Multiplies two nxn matrices A and B using Strassen's algorithm (assumes n is a power of 2)'''
        n = len(A)
        
        # Base case: 1x1 matrix
        if n == 1:
            return [[A[0][0] * B[0][0]]]
        
        # Divide matrices into quadrants
        mid = n // 2
        
        A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
        A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
        A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
        A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
        
        B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
        B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
        B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
        B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
        
        # Helper functions for matrix operations
        def add(X, Y):
            return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
        
        def subtract(X, Y):
            return [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
        
        # Calculate 7 products (Strassen's formulas)
        M1 = strassen_matrix_mult(add(A11, A22), add(B11, B22))
        M2 = strassen_matrix_mult(add(A21, A22), B11)
        M3 = strassen_matrix_mult(A11, subtract(B12, B22))
        M4 = strassen_matrix_mult(A22, subtract(B21, B11))
        M5 = strassen_matrix_mult(add(A11, A12), B22)
        M6 = strassen_matrix_mult(subtract(A21, A11), add(B11, B12))
        M7 = strassen_matrix_mult(subtract(A12, A22), add(B21, B22))
        
        # Combine results
        C11 = add(subtract(add(M1, M4), M5), M7)
        C12 = add(M3, M5)
        C21 = add(M2, M4)
        C22 = add(subtract(add(M1, M3), M2), M6)
        
        # Combine quadrants
        C = [[0] * n for _ in range(n)]
        for i in range(mid):
            for j in range(mid):
                C[i][j] = C11[i][j]
                C[i][j + mid] = C12[i][j]
                C[i + mid][j] = C21[i][j]
                C[i + mid][j + mid] = C22[i][j]
        
        return C
    
    # Test cases
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = strassen_matrix_mult(A, B)
    print("Matrix A:")
    for row in A:
        print(row)
    print("\nMatrix B:")
    for row in B:
        print(row)
    print("\nResult A x B:")
    for row in result:
        print(row)
    print()
    
if __name__ == "__main__":
    #q1a()
    #q1b()
    q1c()