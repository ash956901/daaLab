#BFS
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.visited = [-1] * vertices

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}: ", end="")
            for j in self.adj_list[i]:
                print(f"->{j}", end=" ")
            print()

    def bfs(self):
        q=[]
        q.append(0)
        self.visited[0]=1
        while q:
            current=q.pop(0)
            print(current,end=" ")

            for i in self.adj_list[current]:
                if self.visited[i]==-1:
                    self.visited[i]=1
                    q.append(i)

        return 
    
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    g.display_graph()

    g.bfs()
