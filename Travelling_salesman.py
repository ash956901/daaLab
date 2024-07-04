#Travelling Salesman
class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(self.vertices)]
        self.visited = [False] * self.vertices
        self.count = 0
        self.min_cost = float('inf')
        
    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))
    
    def print_graph(self):
        for u in range(self.vertices):
            print(f"Node: {u}")
            print("Adjacency List:", end=" ")
            for v in self.adj_list[u]:
                print(v, end=" ")
            print()
    
    def tsp(self, src, node, cost):
        if self.count == self.vertices and node == src:
            self.min_cost = min(self.min_cost, cost)
            return
        
        for v, w in self.adj_list[node]:
            if not self.visited[v]:
                self.visited[v] = True
                self.count += 1
                self.tsp(src, v, cost + w)
                self.visited[v] = False
                self.count -= 1
    
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 15)
    g.add_edge(0, 3, 20)
    g.add_edge(1, 2, 35)
    g.add_edge(1, 3, 25)
    g.add_edge(2, 3, 30)
   
    g.print_graph()
    g.tsp(0, 0, 0)
    print(g.min_cost)
