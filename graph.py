import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        """Add an edge to the graph."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start):
        """Perform Dijkstra's algorithm to find the shortest path from the start node."""
        queue = []
        distances = {vertex: float('infinity') for vertex in self.adj_list}
        distances[start] = 0
        heapq.heappush(queue, (0, start))

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            # Nodes can only get added once with the shortest distance
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances
