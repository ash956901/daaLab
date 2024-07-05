class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        
    def bellman_ford(self, src):
        distances = [float('inf')] * self.vertices
        distances[src] = 0
        
        for i in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w


        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                return False 

        return distances


g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

result = g.bellman_ford(0)
print(result)  
