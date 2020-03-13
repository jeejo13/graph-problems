from collections import defaultdict
class Graph:
  def __init__(self):
    self.graph=defaultdict(list)
  def addEdge(self,u,v):
    self.graph[u].append(v)
  def DFS_traverse(self,visited,v):
    visited[v]=True
    print(v,end=" ")
    for i in self.graph[v]:
      if visited[i]==False:
        self.DFS_traverse(visited,i)
  def DFS(self,v):
    visited=[False] * len(self.graph)
    self.DFS_traverse(visited,v)
  
g=Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.DFS(2)
