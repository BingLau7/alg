
# This algorithm is from the Princeton Algorithms Class
# Used here for this homework. It is almost the same. 
#
import sys


class Digraph :
	def __init__(self, vertices=0, edges=0 ) : 
		self.V = vertices
		self.E = edges
		self.adj = [[] for i in range(vertices) ] #create empty adjecent list sets for each vertex		
		
	def addEdge(self, v, w ): #edge from v to w
		#print v, w
		if len(self.adj) <= v :
			n = v - len(self.adj) + 1  #we need all this just to add more space to self.adj list.
			for i in range(n) :
				self.adj.append([])   
			
			self.V += n
			
		#print self.adj
		#print self.V
		self.adj[v].append(w)
		self.E += 1
			
	def reverse(self) : #returns a new graph with edges reversed
		R = Digraph(self.V, self.E)
		for i in range(self.V) :
			for j in self.adj[i] : #link from i to j
				R.addEdge(j,i)     #link from j to i				
		return R
			
	def printf(self) :
		for i in self.adj :
			print i
			


class DepthFirstOrder :
	def __init__(self, G) :
		self.marked = [False] * G.V 
		self.postorder  = []
		self.preorder   = []
		for i in range(G.V) :
			if not self.marked[i] :
				self.dfs( G, i )
		#self.dfs( G, 5 )
				
	def _dfs(self, G, v) :	#recursive implementation
		self.marked[v] = True
		self.preorder.append(v)
		for u in G.adj[v] :
			if not self.marked[u] :
				self._dfs( G, u ) 	
		self.postorder.append(v)
		
	def dfs(self, G, top) :	#NON recursive implementation		
		to_visit_stack = [ top ]
		while to_visit_stack :
			#print to_visit_stack
			v = to_visit_stack[-1]
			self.marked[v] = True
			children = [u for u in G.adj[v] if not self.marked[u] ]			
			if not children : #leaf node or all childeren processed already.
				self.postorder.append(v)
				to_visit_stack.pop()
			else :
				for u in children :
					self.marked[u] = True
				to_visit_stack += children 

	def reversePost(self) :
		for i in reversed(self.postorder) :
			yield i		

#Almost the same as the CC class
class KosarajuSharirSCC :
	def __init__(self, G) :
		self.marked = [False] * G.V 
		self.id     = [None]  * G.V	#each connected group is given an id
		self.count  = 0 # count of groups; to increment the ids
		df = DepthFirstOrder( G.reverse() )  #Refer book. 
		#print list(df.reversePost())
		for i in df.reversePost() :          #Refer book. Need study to understand this step.
			if not self.marked[i] :
				self.dfs( G, i ) #this will find all the vertices of i's group and fill the ids
				self.count += 1
			#now the marked array must have chaged because of the dfs
			#but we need to continue checking to fill all the disconnected components.
	
	#we shall start from v and mark all the vertex reachable from here with self.count.
	def _dfs(self, G, v) :
		#print v
		self.marked[v] = True
		self.id[v] = self.count
		for u in G.adj[v] :
			if not self.marked[u] :				
				self.id[u] = self.count
				self.dfs( G, u )
	
	def dfs(self, G, top) :	#NON recursive implementation		
		to_visit_stack = [ top ]
		while to_visit_stack :
			#print to_visit_stack
			v = to_visit_stack[-1]
			self.marked[v] = True
			self.id[v] = self.count
			children = [u for u in G.adj[v] if not self.marked[u] ]			
			if not children : #leaf node or all childeren processed already.
				#self.postorder.append(v)
				to_visit_stack.pop()
			else :
				for u in children :
					self.marked[u] = True
					self.id[u] = self.count
				to_visit_stack += children 

	
	def stronglyConnected(self, u, v ) : # we check if u and v are connected by checking their ids
		return self.id[u] == self.id[v] #return true if they are equal 
	



if __name__ == "__main__":		
	filename = sys.argv[1]		
	with open(filename) as f:
		count = 1
		for data in f:
			if not data.strip() :
				continue
				
			if count == 1 :
				G = Digraph()

			e = data.strip().split()
			G.addEdge( int(e[0]) -1 , int(e[1]) -1 ) #-1 because vertices are numbered from 1, but we store in list from 0
			#G.addEdge( int(e[0]), int(e[1]) )
			count += 1
		
		
		s = KosarajuSharirSCC(G)
		
		#For homework answer, we need to find the number of nodes in the 5 largest components.
		from collections import Counter
		z = Counter( s.id )
		c = sorted(z.values())
		for i in range(5) : #we need the last 5 values.
			print c[-1-i]
			 
		
			
		

		
