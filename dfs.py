#DFS
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list=[[] for _ in range(vertices)]
        self.visited= [-1] * self.vertices

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_graph(self):
        for i in range(self.vertices):
            for j in self.adj_list[i]:
                print(f"{i}->{j}")
                print()

    def dfs(self,v):
        self.visited[v]=1
        print(f"{v}",end=" ")
        for i in self.adj_list[v]:
            if self.visited[i]==-1:
                self.dfs(i)

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    g.display_graph()

    g.dfs(0)
