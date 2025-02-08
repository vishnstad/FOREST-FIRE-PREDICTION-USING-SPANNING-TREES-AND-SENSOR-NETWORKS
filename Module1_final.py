class Graph:
    def __init__(self):
        self.G_AL = {}  # Adjacency List
        self.G_AM = []  # Adjacency Matrix
    def create_graph(self):
        num_vertices = int(input("Enter the number of vertices: "))
        num_edges = int(input("Enter the number of edges: "))
        self.G_AM = [[float("inf")] * (num_vertices + 1) for _ in range(num_vertices + 1)]
        for _ in range(1,num_edges+1):
            source, destination, weight = map(int, input("Enter each edge as 'source destination weight': ").split())
            # Adjacency List
            if source not in self.G_AL:
                self.G_AL[source] = []
            self.G_AL[source].append((destination, weight))
            # Adjacency Matrix
            self.G_AM[source][destination] = weight  
######################################ADJACENCY LIST############################################################################
    
    def ALaddvert(self, u, v, w):
        if u not in self.G_AL:
            self.G_AL[u] = []
        self.G_AL[u].append([v, w])

    def ALaddedge(self,u,v,w):
        if u not in self.G_AL:
            self.G_AL[u] = []
        self.G_AL[u].append([v, w])
    def ALremovevert(self,u):
        self.G_AL.pop(u)

        for i in self.G_AL:
            new_edges = []
            for j in self.G_AL[i]:
                if j and j[0] != u:
                    new_edges.append(j)
            self.G_AL[i] = new_edges 
    def ALremoveedge(self,u,v,w):
        if u in self.G_AL:
            new_edges = []
            for j in self.G_AL[u]:
                if not (j[0] == v and j[1] == w):
                    new_edges.append(j)
            self.G_AL[u] = new_edges 
    def printG_AL(self):
        for i in self.G_AL:
            print(f"{i}:{self.G_AL[i]}")
######################################ADJACENCY MATRIX############################################################################
    
    def addvert_AM(self, u, v, w):
        for i in self.G_AM:
            i.append(0)
        self.G_AM.append([0] * (len(self.G_AM) + 1))
        self.G_AM[u][v] = w
    def addedge_AM(self,u,v,w):
        self.G_AM[u][v] = w
    
    def removedge_AM(self,u,v):
        self.G_AM[u][v] = 0
    def removevertex_AM(self,v):
        if v >= len(self.G_AM):
            print(f"Vertex {v} does not exist.")
            return
        self.G_AM.pop(v)
        for row in self.G_AM:
            row.pop(v)
    def print_AM(self):
        for i in self.G_AM:
            for j in i:
                if j == float('inf'):
                    print("inf", end=" ")
                else:
                    print(f"{j:3}", end=" ")  
            print()
    def returnAL(self):
        return self.G_AL
    def returnAM(self):
        return self.G_AM  
    def get_vertices(self):
        if self.G_AL:
            return list(self.G_AL.keys())
        elif self.G_AM:
            return list(range(len(self.G_AM)))
        else:
            return []
    
 
###########################################################################################################################################

