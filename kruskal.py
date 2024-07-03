#Kruskal
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]

    def add_edge(self,u,v,w):
        self.edges.append((w,u,v))

    def find(self,i,parent):
        if(parent[i]==i):
            return i
        return self.find(parent[i],parent)
    
    def union(self,u,v,parent,rank):
        root_x=self.find(u,parent)
        root_y=self.find(v,parent)

        if(rank[root_x]<rank[root_y]):
            parent[root_x]=root_x
        elif(rank[root_y]<rank[root_x]):
            parent[root_y]=root_x
        else:
            parent[root_y]=root_x
            rank[root_x]+=1

    def kruskal_mst(self):
        mst=[]
        parent=[]
        rank=[]

        #sort here
        self.edges.sort()

        #initialise parent and rank
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        i=0
        e=0

        while e < self.vertices-1:
            weight,u,v=self.edges[i]
            i+=1

            x=self.find(u,parent)
            y=self.find(v,parent)

            if(x!=y):
                mst.append((u,v,weight))
                e+=1
                self.union(u,v,parent,rank)
            
        return mst
    
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 3)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 6)

   

    mst = g.kruskal_mst()
    print("\nMinimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]}: {edge[2]}")
