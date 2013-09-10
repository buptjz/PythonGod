'''
In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. 
This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 
that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of 
a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's 
algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. 
The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). 
The superior approach stores the unprocessed vertices in the heap, as described in lecture. 
Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
'''
class Node:
    def __init__(self,id,key,edge,isX):
        self.id = id
        self.key = key
        self.edge = edge
        self.isX = isX
        
    #reload >= sign
    def __lt__(self,other):
        if self.key >= other.key:
            return True
        else:
            return False

    def __repr__(self):
        return str("id\t"+str(self.id)+"\nkey\t"+str(self.key)+"\nedge\t"+str(self.edge)+"\nisInX\t"+str(self.isX))

nodeFile = open('edges.txt','r')
lines = nodeFile.readlines()
numberOfNodes = int(lines[0].split()[0])
numberOfEdges = int(lines[0].split()[1])
lines = lines[1:]
edges = []
nodes = [None for i in range(numberOfNodes)]

#Indicate which line id being executed
lineNumber = 0

for line in lines:
    end1 = int(line.split()[0])
    end2 = int(line.split()[1])
    cost = int(line.split()[2])
    
    #write into the edges list
    edges.append([end1,end2,cost])
    
    #if vertex end1/2 not in the nodeList,insert it,else, append the line into the node
    if nodes[end1-1] == None:
        newNode = Node(end1,9999,[lineNumber],False)
        nodes[end1-1] = newNode
    else:
        nodes[end1-1].edge.append(lineNumber)
    if nodes[end2-1] == None:
        newNode = Node(end2,9999,[lineNumber],False)
        nodes[end2-1] = newNode
    else:
        nodes[end2-1].edge.append(lineNumber)
        
    lineNumber += 1

X = [nodes[0]]
nodes[0].isX = True
#V_X = heap()

def computeKey(node):
    costs = []
    edgesOfNode = node.edge
    for edge in edgesOfNode:
        end1 = edge[0]
        end2 = edge[1]
        cost = edge[2]
        if nodes[end1].isX or nodes[end2].isX:
            costs.append[cost]
    return max(costs) if costs else 9999

#initialize the heap
for node in nodes[1:]:
    node.key = computeKey(node)
print(123)
    