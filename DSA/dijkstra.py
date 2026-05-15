import heapq

def dijkstra(graph, start):
    # Dictionary to store the shortest distance from start to each node
    # Initialized to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to track nodes to visit: (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we found a longer path than what we've already processed, skip it
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Example Usage:
# Representing the graph as an adjacency list (dictionary of dictionaries)
example_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 3},
    'C': {'B': 1, 'D': 5},
    'D': {}
}

shortest_paths = dijkstra(example_graph, 'A')
print(shortest_paths)
# Output: {'A': 0, 'B': 3, 'C': 2, 'D': 6}