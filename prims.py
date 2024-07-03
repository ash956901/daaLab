#Prims
import heapq

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list=[[] for _ in range(vertices)]
        self.visited=[False]*vertices
    
    def add_edge(self,u,v,w):
        self.adj_list[u].append((v,w))
        self.adj_list[v].append((u,w))

    
    def display_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}:", end="")
            for (j, weight) in self.adj_list[i]:
                print(f" -> {j} (weight {weight})", end="")
            print()

    def prims_mst(self,start):
        mst=[]
        min_heap=[(0,start,-1)]

        while min_heap:
            weight,node,parent=heapq.heappop(min_heap)

            if(not self.visited[node]):
                self.visited[node]=1
                if(parent!=-1):
                    mst.append((parent,node,weight))
                for neighbour,w in self.adj_list[node]:
                    if not self.visited[neighbour]:
                        heapq.heappush(min_heap,(w,neighbour,node))
   

        return mst
    
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 3)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 6)

    print("Graph:")
    g.display_graph()

    start_node = 0
    mst = g.prims_mst(start_node)
    print("\nMinimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]}: {edge[2]}")
