from Module1_v2 import Graph
from minheap import minheap

class Algorithms:
    def __init__(self, graph):
        self.graph = graph
    class Dijkstra:
        def __init__(self, algorithms, source, use_adj_list=True):
            self.graph = algorithms.graph
            self.source = source
            self.use_adj_list = use_adj_list
            self.distances = {}
            self.predecessors = {}
            self.initialize_single_source()

        def initialize_single_source(self):
            vertices = self.graph.get_vertices() if self.use_adj_list else range(1, len(self.graph.G_AM))
            for vertex in vertices:
                self.distances[vertex] = float('inf')
                self.predecessors[vertex] = None
            self.distances[self.source] = 0

        def relax(self):
            min_heap = minheap()
            min_heap.insert((0, self.source))

            if self.use_adj_list:
                while len(min_heap.heap) > 0:
                    current_distance, u = min_heap.extract_min()
                    for v, weight in self.graph.G_AL.get(u, []):
                        if current_distance + weight < self.distances[v]:
                            self.distances[v] = current_distance + weight
                            self.predecessors[v] = u
                            min_heap.insert((self.distances[v], v))
            else:
                while len(min_heap.heap) > 0:
                    current_distance, u = min_heap.extract_min()
                    for v in range(1, len(self.graph.G_AM)):
                        weight = self.graph.G_AM[u][v]
                        if weight != float('inf') and current_distance + weight < self.distances[v]:
                            self.distances[v] = current_distance + weight
                            self.predecessors[v] = u
                            min_heap.insert((self.distances[v], v))

        def find_shortest_paths(self):
            self.relax()
            return True

        def get_shortest_distance(self, destination):
            return self.distances.get(destination, float('inf'))

        def get_path(self, destination):
            path = []
            while destination is not None:
                path.append(destination)
                destination = self.predecessors.get(destination)
            return path[::-1]  # Reverse the path
        
    class BellmanFord:
        def __init__(self, algorithms, source, use_adj_list=True):
            self.graph = algorithms.graph
            self.source = source
            self.use_adj_list = use_adj_list
            self.distances = {}
            self.predecessors = {}
            self.initialize_single_source()

        def initialize_single_source(self):
                vertices = self.graph.get_vertices() if self.use_adj_list else range(1, len(self.graph.G_AM))
                for vertex in vertices:
                    self.distances[vertex] = float('inf')
                    self.predecessors[vertex] = None
                self.distances[self.source] = 0


        def relax(self):
            if self.use_adj_list:
                for _ in range(len(self.graph.G_AL) - 1):
                    for u in self.graph.G_AL:
                        for v, weight in self.graph.G_AL[u]:
                            if self.distances[u] + weight < self.distances[v]:
                                self.distances[v] = self.distances[u] + weight
                                self.predecessors[v] = u
            else:
                for _ in range(len(self.graph.G_AM) - 1):
                    for u in range(1, len(self.graph.G_AM)):
                        for v in range(1, len(self.graph.G_AM)):
                            weight = self.graph.G_AM[u][v]
                            if weight != float('inf') and self.distances[u] + weight < self.distances[v]:
                                self.distances[v] = self.distances[u] + weight
                                self.predecessors[v] = u

        def find_shortest_paths(self):
            self.relax()
            return True

        def get_shortest_distance(self, destination):
            return self.distances.get(destination, float('inf'))

        def get_path(self, destination):
            path = []
            while destination is not None:
                path.append(destination)
                destination = self.predecessors.get(destination)
            return path[::-1]  # Reverse the path
    class FloydWarshall:
        def __init__(self, algorithms, use_adj_list=True):
            self.graph = algorithms.graph
            self.use_adj_list = use_adj_list
            self.distances = {}
            self.predecessors = {}
            self.initialize_distances()

        def initialize_distances(self):
            if self.use_adj_list:
                vertices = self.graph.get_vertices()
                self.distances = {u: {v: float('inf') for v in vertices} for u in vertices}
                self.predecessors = {u: {v: None for v in vertices} for u in vertices}
                for u in vertices:
                    self.distances[u][u] = 0
                    for v, weight in self.graph.G_AL[u]:
                        self.distances[u][v] = weight
                        self.predecessors[u][v] = u
            else:
                V = len(self.graph.G_AM)
                self.distances = [[float('inf')] * V for _ in range(V)]
                self.predecessors = [[None] * V for _ in range(V)]
                for i in range(V):
                    self.distances[i][i] = 0  # Ensure self-loops are 0
                    for j in range(V):
                        if self.graph.G_AM[i][j] != float("inf"):
                            self.distances[i][j] = self.graph.G_AM[i][j]
                            self.predecessors[i][j] = i

        def floyd_warshall(self):
            if self.use_adj_list:
                vertices = self.graph.get_vertices()
                for k in vertices:
                    for i in vertices:
                        for j in vertices:
                            if self.distances[i][k] + self.distances[k][j] < self.distances[i][j]:
                                self.distances[i][j] = self.distances[i][k] + self.distances[k][j]
                                self.predecessors[i][j] = self.predecessors[k][j]
            else:
                V = len(self.graph.G_AM)
                for k in range(V):
                    for i in range(V):
                        for j in range(V):
                            if self.distances[i][k] + self.distances[k][j] < self.distances[i][j]:
                                self.distances[i][j] = self.distances[i][k] + self.distances[k][j]
                                self.predecessors[i][j] = self.predecessors[k][j]

        def get_shortest_distance(self, u, v):
            if self.use_adj_list:
                return self.distances.get(u, {}).get(v, float('inf'))
            else:
                return self.distances[u][v]

        def get_path(self, u, v):
            path = []
            seen = set()  
            while v is not None and v not in seen:
                path.insert(0, v)
                seen.add(v)
                v = self.predecessors[u][v]
            return path if path and path[0] == u else []

    