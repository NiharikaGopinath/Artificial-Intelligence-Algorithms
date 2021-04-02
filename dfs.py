# Python Program to detect cycle in an undirected graph 
from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
	
		# No. of vertices 
		self.V= vertices #No. of vertices 
		
		# Default dictionary to store graph 
		self.graph = defaultdict(list) 


	# Function to add an edge to graph 
	def addEdge(self,v,w): 
		
		self.graph[v].append(w) 
		
		#Add v to w_s list 
		self.graph[w].append(v) 
 
	def isCyclicUtil(self,v,visited,parent): 

		# Mark the current node as visited 
		visited[v]= True

		# Recur for all the vertices 
		# adjacent to this vertex 
		for i in self.graph[v]: 
			
			# If the node is not 
			# visited then recurse on it 
			if visited[i]==False : 
				if(self.isCyclicUtil(i,visited,v)): 
					return True
			
			elif parent!=i: 
				return True
		
		return False
		

	def isCyclic(self): 
		
		visited =[False]*(self.V) 
		
		for i in range(self.V): 
			
			if visited[i] ==False: 
				if(self.isCyclicUtil 
					(i,visited,-1)) == True: 
					return True
		
		return False


g = Graph(5) 
g.addEdge(1, 0) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 

if g.isCyclic(): 
	print ("Graph contains cycle")
else : 
	print ("Graph does not contain cycle ")
g1 = Graph(3) 
g1.addEdge(0,1) 
g1.addEdge(1,2) 


if g1.isCyclic(): 
	print ("Graph contains cycle")
else : 
	print ("Graph does not contain cycle ")


