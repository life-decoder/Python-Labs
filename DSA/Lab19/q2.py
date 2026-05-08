"""
Consider the following undirected graph:
V = {A, B, C, D, E}
E = {(A, B), (A, C), (B, C), (B, D), (C, E)}

A vertex cover is a set of vertices such that every edge has at least one
endpoint in the set.

This program finds a vertex cover using the 2-approximation algorithm and
prints the selected edge, the vertices added to the cover, and the remaining
edges at each step.
"""


def normalize_edge(edge):
	return tuple(sorted(edge))


def extract_edges(graph):
	edges = []
	seen = set()

	for vertex, neighbors in graph.items():
		for neighbor in neighbors:
			edge = normalize_edge((vertex, neighbor))
			if edge not in seen:
				seen.add(edge)
				edges.append(edge)

	return edges


def format_edges(edges):
	if not edges:
		return "{}"
	return "{" + ", ".join(f"({u}, {v})" for u, v in edges) + "}"


def two_approx_vertex_cover(graph):
	vertices = list(graph.keys())
	remaining_edges = extract_edges(graph)
	vertex_cover = []
	step = 1

	print("2-Approximation Vertex Cover")
	print("Initial edges:", format_edges(remaining_edges))
	print()

	while remaining_edges:
		selected_edge = remaining_edges[0]
		u, v = selected_edge

		if u not in vertex_cover:
			vertex_cover.append(u)
		if v not in vertex_cover:
			vertex_cover.append(v)

		remaining_edges = [
			edge
			for edge in remaining_edges
			if u not in edge and v not in edge
		]

		print(f"Step {step}:")
		print(f"Selected edge: ({u}, {v})")
		print(f"Vertices added to cover: {u}, {v}")
		print(f"Remaining edges: {format_edges(remaining_edges)}")
		print()
		step += 1

	ordered_cover = [vertex for vertex in vertices if vertex in vertex_cover]
	return ordered_cover


if __name__ == "__main__":
	graph = {
		"A": ["B", "C"],
		"B": ["A", "C", "D"],
		"C": ["A", "B", "E"],
		"D": ["B"],
		"E": ["C"],
	}

	cover = two_approx_vertex_cover(graph)

	print("Final vertex cover:", "{" + ", ".join(cover) + "}")