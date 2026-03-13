"""
Implement the following graph traversal algorithms:
  a. Depth-first search (DFS)
  b. Breadth-first search (BFS)

To test your algorithms, write a program that creates a graph and traverses it using each of the
algorithms. Your program must also display the DFS tree and BFS tree built during the traversals.
"""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Optional, Tuple

from lab17q1 import ListGraph as Graph


def dfs(graph: Graph, start: str) -> Tuple[List[str], List[Tuple[str, str]]]:
    """Perform a depth-first traversal of the graph starting from `start`.

    Returns:
        traversal: list of vertices in the order they were first visited
        tree_edges: list of (parent, child) edges representing the DFS tree
    """

    visited: set[str] = set()
    traversal: List[str] = []
    tree_edges: List[Tuple[str, str]] = []

    def _dfs(u: str) -> None:
        visited.add(u)
        traversal.append(u)
        # Use sorted neighbors for deterministic traversal order
        for v in sorted(graph.neighbors(u)):
            if v not in visited:
                tree_edges.append((u, v))
                _dfs(v)

    if start not in graph.vertices_list():
        return traversal, tree_edges

    _dfs(start)

    # If the graph is disconnected, continue with any remaining vertices
    for u in graph.vertices_list():
        if u not in visited:
            _dfs(u)

    return traversal, tree_edges


def bfs(graph: Graph, start: str) -> Tuple[List[str], List[Tuple[str, str]]]:
    """Perform a breadth-first traversal of the graph starting from `start`.

    Returns:
        traversal: list of vertices in the order they were first visited
        tree_edges: list of (parent, child) edges representing the BFS tree
    """

    visited: set[str] = set()
    traversal: List[str] = []
    tree_edges: List[Tuple[str, str]] = []

    def _bfs_from(source: str) -> None:
        q = deque([source])
        visited.add(source)
        while q:
            u = q.popleft()
            traversal.append(u)
            for v in sorted(graph.neighbors(u)):
                if v not in visited:
                    visited.add(v)
                    tree_edges.append((u, v))
                    q.append(v)

    if start not in graph.vertices_list():
        return traversal, tree_edges

    _bfs_from(start)

    # If the graph is disconnected, traverse remaining components
    for u in graph.vertices_list():
        if u not in visited:
            _bfs_from(u)

    return traversal, tree_edges


def display_traversal(name: str, order: List[str], tree_edges: List[Tuple[str, str]]) -> None:
    print(f"{name} traversal order: {order}")
    print(f"{name} tree edges: {tree_edges}\n")


if __name__ == "__main__":
    # Reuse the same sample graph from lab17q1
    vertices = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]

    g = Graph()
    for v in vertices:
        g.addVertex(v)
    for u, v in edges:
        g.add_edge_by_label(u, v)

    print("Graph (adjacency list):")
    for u in sorted(g.vertices_list()):
        print(f"  {u}: {sorted(g.neighbors(u))}")
    print()

    dfs_order, dfs_tree = dfs(g, start="A")
    bfs_order, bfs_tree = bfs(g, start="A")

    display_traversal("DFS", dfs_order, dfs_tree)
    display_traversal("BFS", bfs_order, bfs_tree)
