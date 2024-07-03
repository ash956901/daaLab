#Bipartite checking

#DFS
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list=[[] for _ in range(vertices)]
        self.color= [-1] * self.vertices

    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display_graph(self):
        for i in range(self.vertices):
            for j in self.adj_list[i]:
                print(f"{i}->{j}")
                print()

    def bfs_bipartite(self):
        q=[]
        q.append(0)
        self.color[0]=1
        while q:
            current=q.pop(0)
            print(current,end=" ")

            for i in self.adj_list[current]:
                if self.color[i]==-1:
                    self.color[i]=not self.color[current]
                    q.append(i)

        #check
        for i in range(self.vertices):
            current_color=self.color[i]
            for j in self.adj_list[i]:
                if(self.color[j]==current_color):
                    return False
        return True
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    g.display_graph()

    b=g.bfs_bipartite()
    print(b)
