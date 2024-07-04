#Bellman Ford
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]
        self.visited=[False] * self.vertices
        
    def add_edge(self,u,v,w):
        self.edges.append((u,v,w))
        
    def bellman_ford(self,source):
        distances=[float('inf')] * self.vertices
        distances[source]=0
        n=self.vertices
        
        #n-1 times
        for i in range(n-1):
            for u,v,w in self.edges:
                if(distances[v]>distances[u]+w):
                    distances[v]=distances[u]+w
                    
        #nth time
        for u,v,w in self.edges:
            if(distances[v]>distances[u]+w):
                return -1
            
        return distances
    
if __name__ =="__main__":
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)
    
    d=g.bellman_ford(0)
    if d!=-1 :
        print(d)
    else:
        print("Negative Cycle found")
        
        
