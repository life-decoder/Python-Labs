""" 
The Bin Packing Problem is a classic optimization puzzle: given a set of items with different weights and a set of bins with a fixed capacity, what is the minimum number of bins required to hold all the items?
"""

def bin_packing_ffd(items, capacity):
    # Step 1: Sort items in descending order
    items.sort(reverse=True)
    
    # List of bins; each bin stores the sum of its current items
    bins = []

    for item in items:
        if item > capacity:
            raise ValueError(f"Item {item} exceeds bin capacity {capacity}")
            
        placed = False
        # Step 2: Try to find the first bin that can fit the item
        for i in range(len(bins)):
            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break
        
        # Step 3: If it doesn't fit in any bin, create a new one
        if not placed:
            bins.append(item)
            
    return len(bins), bins

# Example Usage:
item_weights = [4, 8, 1, 4, 2, 1]
bin_cap = 10

count, distribution = bin_packing_ffd(item_weights, bin_cap)

print(f"Items: {item_weights}")
print(f"Bins used: {count}")
print(f"Final bin weights: {distribution}")