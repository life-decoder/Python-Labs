""" Define a function that implements Kruskal's algorithm. Your function must return the list of edges
that form part of the MST (in the order that they are chosen), and the total weight of the MST.
Write a program to evaluate your function. You can use the graph below:
V = {A, B, C, D, E, F}
E = {(A, B, 4), (A, C, 3), (B, C, 1), (B, D, 2), (C, D, 4), (C, E, 5), (D, E, 1), (D, F, 6), (E, F, 2)}
The set of edges E is a set of triples (u,v,w), where u and v are vertices and w is the weight.
"""


def kruskal_mst(vertices, edges):
    """Return (mst_edges, total_weight) where mst_edges are added in order."""
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return False
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
        return True

    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst_edges = []
    total_weight = 0

    for u, v, w in sorted_edges:
        if union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == len(vertices) - 1:
                break

    return mst_edges, total_weight

def kruskal_mst_v2(nodes, edges):
    # 1. Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    parent = {node: node for node in nodes}
    
    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i]) # Path compression
        return parent[i]

    mst = []
    total_weight=0
    for u, v, weight in edges:
        root_u = find(u)
        root_v = find(v)
        
        # 2. If roots are different, no cycle is formed
        if root_u != root_v:
            parent[root_u] = root_v # Simple union
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

if __name__ == '__main__':
    V = ['A', 'B', 'C', 'D', 'E', 'F']
    E = [
        ('A', 'B', 4),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 2),
        ('C', 'D', 4),
        ('C', 'E', 5),
        ('D', 'E', 1),
        ('D', 'F', 6),
        ('E', 'F', 2),
    ]

    mst, weight = kruskal_mst(V, E)
    #mst, weight = kruskal_mst_v2(V, E)
    print('MST edges in chosen order:')
    for edge in mst:
        print(edge)
    print('Total MST weight:', weight)


