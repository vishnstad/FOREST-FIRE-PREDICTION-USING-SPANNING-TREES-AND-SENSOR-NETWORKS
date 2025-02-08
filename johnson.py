from Module1_v2 import Graph
from minheap import minheap

class BellmanFord:
    def __init__(self, graph, source, use_adj_list=True):
        self.graph = graph
        self.source = source
        self.use_adj_list = use_adj_list
        self.distances = {}
        self.predecessors = {}
        self.initialize_single_source()

    def initialize_single_source(self):
        vertices = self.get_vertices() if self.use_adj_list else range(1, len(self.graph.G_AM))
        for vertex in vertices:
            self.distances[vertex] = float('inf')
            self.predecessors[vertex] = None
        self.distances[self.source] = 0

    def relax(self):
        if self.use_adj_list:
            for _ in range(len(self.graph.G_AL) - 1):
                for u in self.graph.G_AL:
                    for v, weight in self.graph.G_AL[u]:
                        if self.distances[u] != float('inf') and weight is not None and self.distances[u] + weight < self.distances.get(v, float('inf')):
                            self.distances[v] = self.distances[u] + weight
                            self.predecessors[v] = u
        else:
            for _ in range(len(self.graph.G_AM) - 1):
                for u in range(1, len(self.graph.G_AM)):
                    for v in range(1, len(self.graph.G_AM)):
                        weight = self.graph.G_AM[u][v]
                        if weight != float('inf') and self.distances[u] != float('inf') and self.distances[u] + weight < self.distances.get(v, float('inf')):
                            self.distances[v] = self.distances[u] + weight
                            self.predecessors[v] = u

    def find_shortest_paths(self):
        self.relax()
        return True

    def get_vertices(self):
        return self.graph.G_AL.keys()


class Dijkstra:
    def __init__(self, graph, source, use_adj_list=True):
        self.graph = graph
        self.source = source
        self.use_adj_list = use_adj_list
        self.distances = {}
        self.predecessors = {}
        self.initialize_single_source()

    def initialize_single_source(self):
        vertices = self.get_vertices() if self.use_adj_list else range(1, len(self.graph.G_AM))
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
    def get_vertices(self):
        return self.graph.G_AL.keys()


class Johnson:
    def __init__(self, graph):
        self.graph = graph
        self.modified_weights = {}
        self.distance_matrix = {}
        self.h = {}

    def reweight_edges(self):
        
        self.graph.ALaddvert('s', None, None)
        for vertex in self.graph.G_AL:
            if vertex != 's':
                self.graph.ALaddedge('s', vertex, 0)


        bf = BellmanFord(self.graph, 's', use_adj_list=True)
        if bf.find_shortest_paths():
            self.h = bf.distances

            self.graph.ALremovevert('s')
            for u in self.graph.G_AL:
                self.modified_weights[u] = []
                for v, weight in self.graph.G_AL[u]:
                    if v in self.h and u in self.h:
                        adjusted_weight = weight + self.h[u] - self.h[v]
                        self.modified_weights[u].append((v, adjusted_weight))
            return True
        else:
            print("Negative-weight cycle detected. Johnson's algorithm cannot proceed.")
            return False

    def johnson_algorithm(self):
        if not self.reweight_edges():
            return None

        vertices = [v for v in self.graph.G_AL]
        for u in vertices:
            dijkstra = Dijkstra(self.graph, u, use_adj_list=True)
            dijkstra.graph.G_AL = self.modified_weights
            if dijkstra.find_shortest_paths():
                self.distance_matrix[u] = {
                    v: dijkstra.distances[v] + self.h[v] - self.h[u]
                    for v in dijkstra.distances
                }
        return self.distance_matrix
    def get_path_list(self, src, dest, use_adj_list):
        dijkstra = Dijkstra(self.graph, src, use_adj_list=use_adj_list)
        dijkstra.graph.G_AL = self.modified_weights
        if dijkstra.find_shortest_paths():
            return dijkstra.get_path(dest)
        return []
