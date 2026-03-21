""" 
Define a function that implements Prim's algorithm. Your function must return the list of edges
that form part of the MST (in the order that they are chosen), and the total weight of the MST.
Write a program to evaluate your function. You can use the graph below:
V = {A, B, C, D, E, F}
E = {(A, B, 4), (A, C, 3), (B, C, 1), (B, D, 2), (C, D, 4), (C, E, 5), (D, E, 1), (D, F, 6), (E, F, 2)}
The set of edges E is a set of triples (u,v,w), where u and v are vertices and w is the weight.
"""

import heapq

def prim_mst(vertices, edges, start_node):
    # 1. Create an adjacency list: {node: [(weight, neighbor), ...]}
    adj = {v: [] for v in vertices}
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))

    # 2. Initialize tracking variables
    mst_edges = []
    total_weight = 0
    visited = set()
    
    # 3. Priority Queue stores (weight, to_node, from_node)
    # We start with the starting node with 0 weight
    min_heap = [(0, start_node, None)]

    while min_heap and len(visited) < len(vertices):
        weight, u, prev_node = heapq.heappop(min_heap)

        if u in visited:
            continue

        # Add to MST
        visited.add(u)
        total_weight += weight
        if prev_node is not None:
            mst_edges.append((prev_node, u, weight))

        # 4. Push all edges from the new vertex to the heap
        for edge_weight, v in adj[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_weight, v, u))

    return mst_edges, total_weight

# --- Example Usage ---
""" nodes = ['A', 'B', 'C', 'D']
graph_edges = [
    ('A', 'B', 1),
    ('B', 'C', 3),
    ('A', 'C', 4),
    ('C', 'D', 2)
]

mst, weight = prims_mst(nodes, graph_edges, 'A')

print(f"MST Edges: {mst}")
print(f"Total Weight: {weight}")
 """
if __name__ == "__main__":
    V = ["A", "B", "C", "D", "E", "F"]
    E = [
        ("A", "B", 4),
        ("A", "C", 3),
        ("B", "C", 1),
        ("B", "D", 2),
        ("C", "D", 4),
        ("C", "E", 5),
        ("D", "E", 1),
        ("D", "F", 6),
        ("E", "F", 2),
    ]

    mst_edges, total = prim_mst(V, E, "A")

    print("MST edges in selection order:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} : {w}")
    print("Total MST weight:", total)
