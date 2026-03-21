from __future__ import annotations
class Graph:

    def __init__(self, vertices: set[str] = None, edges: set[tuple[str, str, int]] = None):
        self.adjList: dict[str, list[tuple[str, int]]] = {}
        if vertices:
            for v in vertices:
                self.adjList[v] = []
        
        if edges:
            for (u, v, w) in edges:
                self.adjList[u].append((v, w))
                self.adjList[v].append((u, w))

    def add_node(self, node):
        if self.adjList.get(node):
            print("Node already exists")
        else:
            try:
                self.adjList[node] = []
            except KeyError:
                print("Node not found: Could not add edge")

    def add_edge(self, u, v, w):
        try:
            self.adjList[u].append((v, w))
            self.adjList[v].append((u, w))
        except KeyError:
            print("Node not found: Could not add edge")

    def __str__(self):
        return str(self.adjList)

if __name__ == "__main__":
    g = Graph({'A', 'B', 'C', 'D'}, {('A', 'B', 2), ('B','C', 1), ('B', 'D', 3), ('D', 'A', 2)})
    print(g)
