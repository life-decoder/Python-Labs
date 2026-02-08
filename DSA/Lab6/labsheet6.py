def q3():
    def permutations(s: str):
        '''Implement a program, using backtracking, that returns all permutations of a given string.'''
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        
        result = []
        for i in range(len(s)):
            current = s[i]            # Choose current character as first
            remaining = s[:i] + s[i+1:]     # Get remaining characters
            perms = permutations(remaining)     # Generate permutations of remaining characters

            for perm in perms:
                result.append(current + perm)
        return result

    #Example usage
    # test_string = "cbc"
    # print(f"Permutations of '{test_string}':")
    # perms = permutations(test_string)
    # for perm in perms:
    #     print(perm)
    # print(f"Total permutations: {len(perms)}")

    def permutations_v2(s: str):
        '''Generate unique permutations (no duplicates) using character selection'''
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        
        result = []
        used = set()  # Track characters used at this position to avoid duplicates
        for i in range(len(s)):
            # Skip if we've already used this character at this position
            if s[i] in used:
                continue
            used.add(s[i])
            
            # Choose current character as first
            current = s[i]
            # Get remaining characters
            remaining = s[:i] + s[i+1:]
            # Generate permutations of remaining characters
            for perm in permutations_v2(remaining):
                result.append(current + perm)
        return result

    def permutations_alt(s: str):
        '''Generate permutations using swapping method (backtracking)'''
        def backtrack(arr, start, result):
            # Base case: if we've fixed all positions
            if start == len(arr):
                result.append(''.join(arr))
                return
            
            # Try each character in remaining positions
            for i in range(start, len(arr)):
                # Swap current character with start position
                if arr[start] == arr[i] and start != i:
                    continue  # Skip duplicates
                arr[start], arr[i] = arr[i], arr[start]
                # Recursively permute remaining characters
                backtrack(arr, start + 1, result)
                # Backtrack: swap back to restore original state
                arr[start], arr[i] = arr[i], arr[start]
        
        result = []
        backtrack(list(s), 0, result)
        return result
    
    #Test cases
    # test_string = "aba"
    # print(f"\nPermutations of '{test_string}':")
    # print(f"permutations_alt: {permutations_alt(test_string)}")
    
    def permutations_alt_v2(s: str):
        '''Generate unique permutations using swapping method (no duplicates)'''
        def backtrack(arr, start, result):
            # Base case: if we've fixed all positions
            if start == len(arr):
                result.append(''.join(arr))
                return
            
            used = []  # Track characters used at this position
            # Try each character in remaining positions
            for i in range(start, len(arr)):
                # Skip if we've already used this character at this position
                if arr[i] in used:
                    continue
                used.append(arr[i])
                
                # Swap current character with start position
                arr[start], arr[i] = arr[i], arr[start]
                # Recursively permute remaining characters
                backtrack(arr, start + 1, result)
                # Backtrack: swap back to restore original state
                arr[start], arr[i] = arr[i], arr[start]
        
        result = []
        backtrack(list(s), 0, result)
        return result
    
    # Test with duplicates
    test_string2 = "abb"
    print(f"\nPermutations of '{test_string2}' (with duplicates handled):")
    # print(f"permutations_v2: {permutations_v2(test_string2)}")
    print(f"permutations_alt_v2: {permutations_alt_v2(test_string2)}")

def q2():
    def power_set(nums, n = 0, subset = []):
        if len(nums) == 0:
            return []
        if n == len(nums):
            return str(subset)
        else:
            return power_set(nums, n+1, subset + [nums[n]]) + ", " + power_set(nums, n+1, subset)
        
    # print("Power set of [1,2,3]:", power_set([1,2,3]), end="\n\n")
    # print("Power set of []:", power_set([]), end="\n\n")
    # print("Power set of [1]:", power_set([1]), end="\n\n")

    def power_set_v2(nums, size, n = 0, subset = []):
        if len(subset) == size:
            return [subset]
        if n == len(nums):
            return []
        
        return power_set_v2(nums, size, n+1, subset + [nums[n]]) + power_set_v2(nums, size, n+1, subset)
    
    #print("Power set of [1,2,3,4,5] with size 3:", power_set_v2([1,2,3,4,5], 3), end="\n\n")

    def subsetRecursive(i, aSet, subsets, subset, target_size):
        # add subset if it matches the target size
        if len(subset) == target_size:
            subsets.append(list(subset))
            return
        # stop if we've gone through all elements
        if i == len(aSet):
            return
        # include current value and recursively find all subsets
        subset.append(aSet[i])
        subsetRecursive(i + 1, aSet, subsets, subset, target_size)
        # exclude current value and recursively find all subsets
        subset.pop()
        subsetRecursive(i + 1, aSet, subsets, subset, target_size)

    def generateSubset(aSet, size=None):
        subset = [] # store one subset
        subsets = [] # store all subsets
        if size is None:
            # Generate all subsets (original behavior)
            def helper(i):
                if i == len(aSet):
                    subsets.append(list(subset))
                    return
                subset.append(aSet[i])
                helper(i + 1)
                subset.pop()
                helper(i + 1)
            helper(0)
        else:
            # Generate subsets of specific size
            subsetRecursive(0, aSet, subsets, subset, size)
        return subsets

    aSet = [1, 2, 3]
    print("All subsets:", generateSubset(aSet))
    print("Subsets of size 2:", generateSubset(aSet, 2))

def q1():
    def power_set(elements):
        """
        Generate all possible subsets (power set) using brute force approach.
        Time complexity: O(n x 2^n)
        """       
        elements = list(elements)
        n = len(elements)
        
        # Total number of subsets is 2^n
        total_subsets = 2 ** n
        result = []
        
        # Generate all subsets using bit manipulation
        for i in range(total_subsets):
            subset = set()
            # Check each bit position
            for j in range(n):
                # If j-th bit is set, include elements[j] in subset
                if i & (1 << j):
                    subset.add(elements[j])
            result.append(subset)
        
        return result

    # Example usage
    elements = {1, 2, 3}
    print(f"Input set: {elements}")
    subsets = power_set(elements)
    print(f"Power set (total {len(subsets)} subsets):")
    for subset in subsets:
        print(subset)

    return subsets

if __name__ == "__main__":
    #q1()
    #q2()
    q3()