#Dijsktras
import heapq
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list=[[] for _ in range(vertices)]

    def add_edge(self,u,v,w):
        self.adj_list[u].append((v,w))
        self.adj_list[v].append((u,w))

    def display_graph(self):
        for i in range(self.vertices):
            print(f"Vertex {i}:", end="")
            for (j, weight) in self.adj_list[i]:
                print(f" -> {j} (weight {weight})", end="")
            print()

    def dijkstra(self,start):
        distances=[float('inf')] * self.vertices
        distances[start]=0
        min_heap=[(0,start)]
        while min_heap:
            current_distance,current_vertex=heapq.heappop(min_heap) 

            if(current_distance>distances[current_vertex]):
                continue

            for n,d in self.adj_list[current_vertex]:
                distance=current_distance+d 
                if(distance<distances[n]):
                    distances[n]=distance
                    heapq.heappush(min_heap,(distance,n))

        return distances
      
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 0, 7)
    g.add_edge(3, 2, 6)
    g.add_edge(4, 1, 3)
    g.add_edge(4, 2, 9)
    g.add_edge(4, 3, 2)

    print("Graph:")
    g.display_graph()

    start_node = 0
    distances = g.dijkstra(start_node)
    print("\nShortest distances from node", start_node)
    for i in range(len(distances)):
        print(f"Distance to node {i}: {distances[i]}")
