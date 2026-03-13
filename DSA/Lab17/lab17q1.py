""" 
Implement a class Graph to represent and store a graph using an:
    a. Adjacency matrix
    b. Adjacency list

Hint: You may assume that the nodes will be labelled with a single character (A to Z).
Display vertices as a list of characters and edges as a list of tuples (u, v) where u and v are vertices.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple


# This module provides two graph implementations:
#  - MatrixGraph: adjacency-matrix based (indexed vertices)
#  - ListGraph: adjacency-list based (indexed vertices)

class MatrixGraph:
    """Graph represented using an adjacency matrix."""

    def __init__(self) -> None:
        self._vertices: List[str] = []
        # Store matrix as a dict of (i, j) -> 1 for undirected edges.
        self._adjMat: Dict[Tuple[int, int], int] = {}

    def nVertices(self) -> int:
        """Return number of vertices."""
        return len(self._vertices)

    def nEdges(self) -> int:
        """Return number of undirected edges."""
        return len(self._adjMat) // 2

    def addVertex(self, vertex: str) -> None:
        """Add a new vertex to the graph."""
        if vertex in self._vertices:
            return
        self._vertices.append(vertex)

    def validIndex(self, n: int) -> bool:
        """Return True if n is a valid vertex index; otherwise raise."""
        if n < 0 or self.nVertices() <= n:
            raise IndexError("Vertex index out of range")
        return True

    def getVertex(self, n: int) -> str:
        """Get the nth vertex label."""
        if self.validIndex(n):
            return self._vertices[n]

    def addEdge(self, A: int, B: int) -> None:
        """Add an undirected edge between vertices A and B (by index)."""
        self.validIndex(A)
        self.validIndex(B)
        if A == B:
            raise ValueError("Self-loops are not allowed")

        self._adjMat[(A, B)] = 1
        self._adjMat[(B, A)] = 1

    def hasEdge(self, A: int, B: int) -> bool:
        """Return True if an edge exists between A and B."""
        self.validIndex(A)
        self.validIndex(B)
        return bool(self._adjMat.get((A, B), False))

    def vertices_list(self) -> List[str]:
        """Return the list of vertex labels."""
        return list(self._vertices)

    def edges_list(self) -> List[Tuple[str, str]]:
        """Return the list of undirected edges as (u, v) tuples."""
        edges: List[Tuple[str, str]] = []
        for (u, v), val in self._adjMat.items():
            if not val:
                continue
            if u <= v:  # avoid duplicates for undirected graph
                edges.append((self._vertices[u], self._vertices[v]))
        return edges

    def display(self) -> None:
        """Print vertices, edges, and the adjacency matrix."""
        print("Vertices:", self.vertices_list())
        print("Edges:", self.edges_list())
        print("\nAdjacency Matrix:")
        self._print_matrix()

    def _print_matrix(self) -> None:
        header = "  " + " ".join(self._vertices)
        print(header)
        for i, u in enumerate(self._vertices):
            row = " ".join(
                str(int(self._adjMat.get((i, j), 0))) for j in range(self.nVertices())
            )
            print(f"{u} {row}")


class ListGraph:
    """Graph represented using an adjacency list."""

    def __init__(self) -> None:
        self._vertices: List[str] = []
        self._adjList: Dict[int, List[int]] = {}

    def nVertices(self) -> int:
        """Return number of vertices."""
        return len(self._vertices)

    def nEdges(self) -> int:
        """Return number of undirected edges."""
        # Each edge is stored twice (u->v and v->u)
        return sum(len(neighbors) for neighbors in self._adjList.values()) // 2

    def addVertex(self, vertex: str) -> None:
        """Add a new vertex to the graph."""
        if vertex in self._vertices:
            return
        self._vertices.append(vertex)
        self._adjList[len(self._vertices) - 1] = []

    def validIndex(self, n: int) -> bool:
        """Return True if n is a valid vertex index; otherwise raise."""
        if n < 0 or self.nVertices() <= n:
            raise IndexError("Vertex index out of range")
        return True

    def getVertex(self, n: int) -> str:
        """Get the nth vertex label."""
        if self.validIndex(n):
            return self._vertices[n]

    def addEdge(self, A: int, B: int) -> None:
        """Add an undirected edge between vertices A and B (by index)."""
        self.validIndex(A)
        self.validIndex(B)
        if A == B:
            raise ValueError("Self-loops are not allowed")

        if B not in self._adjList[A]:
            self._adjList[A].append(B)
        if A not in self._adjList[B]:
            self._adjList[B].append(A)

    def add_edge_by_label(self, u: str, v: str) -> None:
        """Add an edge between vertices given by labels, adding missing vertices."""
        # Ensure vertices exist
        if u not in self._vertices:
            self.addVertex(u)
        if v not in self._vertices:
            self.addVertex(v)

        ui = self._vertices.index(u)
        vi = self._vertices.index(v)
        self.addEdge(ui, vi)

    def hasEdge(self, A: int, B: int) -> bool:
        """Return True if an edge exists between A and B."""
        self.validIndex(A)
        self.validIndex(B)
        return B in self._adjList.get(A, [])

    def vertices_list(self) -> List[str]:
        """Return the list of vertex labels."""
        return list(self._vertices)

    def edges_list(self) -> List[Tuple[str, str]]:
        """Return the list of undirected edges as (u, v) tuples."""
        edges: List[Tuple[str, str]] = []
        for u, neighbors in self._adjList.items():
            for v in neighbors:
                if u <= v:  # avoid duplicates
                    edges.append((self._vertices[u], self._vertices[v]))
        return edges

    def neighbors(self, vertex: str) -> List[str]:
        """Return neighbors of a vertex label."""
        if vertex not in self._vertices:
            return []
        idx = self._vertices.index(vertex)
        return [self._vertices[n] for n in self._adjList.get(idx, [])]

    def display(self) -> None:
        """Print vertices, edges, and the adjacency list."""
        print("Vertices:", self.vertices_list())
        print("Edges:", self.edges_list())
        print("\nAdjacency List:")
        for u in range(self.nVertices()):
            print(f"  {self._vertices[u]}: {[self._vertices[v] for v in self._adjList[u]]}")