""" 
Dijkstra’s algorithm is the classic "greedy" solution for finding the shortest path from a starting node to all other nodes in a graph with non-negative edge weights.
"""
import heapq

def dijkstra(graph, start):
    # Dictionary to store the shortest distance to each node
    # Initialize with infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Greedily pick the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we found a longer path already in the queue, skip it
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found, "relax" the edge
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Example Graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'B': 1, 'D': 3, 'E': 7},
    'D': {'E': 1},
    'E': {}
}

print(dijkstra(graph, 'A'))