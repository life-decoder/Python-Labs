import heapq


def dijkstra(graph, source):
	distances = {vertex: float("inf") for vertex in graph}
	predecessors = {vertex: None for vertex in graph}
	distances[source] = 0

	priority_queue = [(0, source)]

	while priority_queue:
		current_distance, current_vertex = heapq.heappop(priority_queue)

		if current_distance > distances[current_vertex]:
			continue

		for neighbor, weight in graph[current_vertex]:
			new_distance = current_distance + weight
			if new_distance < distances[neighbor]:
				distances[neighbor] = new_distance
				predecessors[neighbor] = current_vertex
				heapq.heappush(priority_queue, (new_distance, neighbor))

	return distances, predecessors

def dijkstra2(graph, source):
	distances = {vertex: float("inf") for vertex in graph}
	predecessors = {vertex: None for vertex in graph}
	distances[source] = 0

	priority_queue = [(0, source)]

	while priority_queue:
		current_distance, current_vertex = heapq.heappop(priority_queue)

		if current_distance > distances[current_vertex]:
			continue

		for neighbor, weight in graph[current_vertex]:
			new_distance = current_distance + weight
			if new_distance < distances[neighbor]:
				distances[neighbor] = new_distance
				predecessors[neighbor] = current_vertex
				heapq.heappush(priority_queue, (new_distance, neighbor))

	return distances, predecessors


def build_path(predecessors, source, destination):
	path = []
	current_vertex = destination

	while current_vertex is not None:
		path.append(current_vertex)
		if current_vertex == source:
			break
		current_vertex = predecessors[current_vertex]

	path.reverse()
	return path if path and path[0] == source else []


if __name__ == "__main__":
	graph = {
		"A": [("B", 4), ("C", 1)],
		"B": [("A", 4), ("C", 2), ("D", 5)],
		"C": [("A", 1), ("B", 2), ("D", 8), ("E", 10)],
		"D": [("B", 5), ("C", 8), ("E", 2)],
		"E": [("C", 10), ("D", 2)],
	}

	source_vertex = "A"
	distances, predecessors = dijkstra(graph, source_vertex)

	print("Vertex  Distance from A  Predecessor")
	for vertex in graph:
		distance = distances[vertex]
		distance_text = "∞" if distance == float("inf") else str(distance)
		predecessor_text = predecessors[vertex] if predecessors[vertex] is not None else "-"
		print(f"{vertex:<7} {distance_text:<15} {predecessor_text}")

	shortest_path = build_path(predecessors, source_vertex, "E")
	print()
	print("Shortest path from A to E:", " -> ".join(shortest_path))