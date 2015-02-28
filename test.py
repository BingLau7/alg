import sys
import random
import copy

'''
This is written from suijian's code. The idea is too beautiful.
'''

#We create a class to hold the node and its adjecent nodes.
class Adj :
	def __init__( self, node, edge ) :
		self.node = node
		self.edge = edge
		
	#contraction is from this obeject to a passed Adj object
	#It is like merging two vertex in a graph, but keep all the non self links
	def contract( self, other ) : 
		#First we need to merge the nodes
		self.node += other.node
		#now we need to merge the edges; edges are just nodes in the edges list
		#ie all nodes not in self.node & other.node ( we already merged these lists above )
		self.edge = [n for n in self.edge + other.edge if n not in self.node] 
		
#Note this is a recursive funtion
#Graph is just a list of Adj objects
def cut( graph ) :
	if len( graph ) == 2 : #this is the base case for the recurtion
		return graph 
		
	#more than two vertices; We need contract two. but which edge
	#Choose randomly two connected nodes
	rand_node  = random.choice( graph ) #this is an Adj onject
	#Ok now we need another node connected to it
	r = random.choice( rand_node.edge ) #this is just a number/label
	#we need to find the Adj obj with this node
	edge_node = [ a for a in graph if r in a.node ][0] #we only need one.
	
	#Now contact
	rand_node.contract( edge_node )
	
	#remove the contracted node from graph
	graph.remove( edge_node )
	
	#Now recurse
	return cut( graph )
	
	
	
def find_min_cut( graph ) :
	#first we make a copy of the graph
	graph2 = copy.deepcopy(graph)
	#now cut this
	cut_graph = cut( graph2 )

	#length is the number of edges from first node to scond
	return len( cut_graph[0].edge )
	

if __name__ == "__main__":
	#random.seed(1)
	if len(sys.argv) > 1:
		f = open(sys.argv[1])
	else:
		f = sys.stdin	
	
	G = [] #this is the graph
	for line in f :
		if line.strip() :
			nodes = [ int(x) for x in line.split() ] #conver the line to a list
			#print nodes
			tail = nodes.pop(0) #take the fist one.
			
			G.append( Adj( [tail], nodes ) ) #0:1 is the first node, 1: are the rest of the edges
				
	print find_min_cut(G)
