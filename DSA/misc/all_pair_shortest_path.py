def floyd_warshall(graph, num_vertices):
    # Initialize the distance matrix with the input graph values
    # dist[i][j] will be the shortest distance from i to j
    dist = [list(row) for row in graph]

    # Iterate through all vertices as an intermediate point
    for k in range(num_vertices):
        # Pick all vertices as source one by one
        for i in range(num_vertices):
            # Pick all vertices as destination for the above picked source
            for j in range(num_vertices):
                # If vertex k is on the shortest path from i to j, 
                # then update the value of dist[i][j]
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example Usage:
INF = float('inf')
# Representation of a graph (4 nodes)
# 0 means distance to self, INF means no direct edge
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

num_v = 4
result = floyd_warshall(graph, num_v)

print("Shortest distance matrix:")
for row in result:
    print(row)