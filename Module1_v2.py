class Graph:
    def __init__(self):
        self.G_AL = {
    1: [(2, 3), (4, 5)],  # Vertex 1 connects to 2 with weight 3 and to 4 with weight 5
    2: [(1, 3), (3, 4)],  # Vertex 2 connects to 1 with weight 3 and to 3 with weight 4
    3: [(2, 4), (4, 2)],  # Vertex 3 connects to 2 with weight 4 and to 4 with weight 2
    4: [(1, 5), (3, 2), (5, 6)],  # Vertex 4 connects to 1 with weight 5, to 3 with weight 2, and to 5 with weight 6
    5: [(4, 6)]           # Vertex 5 connects to 4 with weight 6
}
        self.G_AM = [
            [0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],  # Row for 0-index (unused)
            [float('inf'), 0, 3, float('inf'), 5, float('inf')],
            [float('inf'), 3, 0, 4, float('inf'), float('inf')],
            [float('inf'), float('inf'), 4, 0, 2, float('inf')],
            [float('inf'), 5, float('inf'), 2, 0, 6],
            [float('inf'), float('inf'), float('inf'), float('inf'), 6, 0]
        ]
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
##################################################################################################################
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
