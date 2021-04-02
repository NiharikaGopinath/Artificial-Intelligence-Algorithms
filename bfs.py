from collections import deque
 
 
# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 

def BFS(graph, src, N):
 
    discovered = [False] * N
 
    
    discovered[src] = True
 
    # create a queue for doing BFS
    q = deque()
 
    # enqueue source vertex and its parent info
    q.append((src, -1))
 
    
    while q:
 
        # dequeue front node and print it
        (v, parent) = q.popleft()
 
        # do for every edge `v —> u`
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it as discovered
                discovered[u] = True
 
                
                q.append((u, v))
 
            
            elif u != parent:
               
                return True
 
   
    return False
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12), (6, 10)
        # edge `6 —> 10` introduces a cycle in the graph
    ]
 
    # total number of nodes in the graph
    N = 13
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # Perform BFS traversal in connected components of a graph
    if BFS(graph, 1, N):
        print("The graph contains a cycle")
    else:
        print("The graph doesn't contain any cycle")
 

