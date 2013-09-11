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


import sys
sys.setrecursionlimit(3000)
from jzHeap import jzHeap

class Node:
    def __init__(self,id,key,edge,isX,index=9999):
        self.id = id
        self.key = key
        self.edge = edge
        self.isX = isX
        self.index = index
        
    #reload > sign
    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False

    def __repr__(self):
        return str("id\t"+str(self.id)+"\nkey\t"+str(self.key)+"\nedge\t"+str(self.edge)+"\nisInX\t"+str(self.isX) + "\nindex\t"+str(self.index))

def computeKey(node):
    costs = []
    edgesOfNode = node.edge
    for edgeNo in edgesOfNode:
        edge = edges[edgeNo]
        end1 = edge[0]
        end2 = edge[1]
        cost = edge[2]
        if nodes[end1].isX or nodes[end2].isX:
            costs.append(cost)
    return min(costs) if costs else 9999

#Initialization
nodeFile = open('edges.txt','r')
lines = nodeFile.readlines()
numberOfNodes = int(lines[0].split()[0])
numberOfEdges = int(lines[0].split()[1])
lines = lines[1:]
edges = []#edges starts from 0
nodes = [None for i in range(numberOfNodes+1)]#nodes starts from 1,to 500. so nodes[500] is OK
lineNumber = 0#Indicate which line id being executed

for line in lines:
    end1 = int(line.split()[0])
    end2 = int(line.split()[1])
    cost = int(line.split()[2])
    edges.append([end1,end2,cost])#write into the edges list
    #if vertex end1/2 not in the nodeList,insert it,else, append the line into the node
    if nodes[end1] == None:
        newNode = Node(end1,9999,[lineNumber],False)
        nodes[end1] = newNode
    else:
        nodes[end1].edge.append(lineNumber)
    if nodes[end2] == None:
        newNode = Node(end2,9999,[lineNumber],False)
        nodes[end2] = newNode
    else:
        nodes[end2].edge.append(lineNumber)
    lineNumber += 1

#Initialize X
X = [nodes[1]]
nodes[1].isX = True
nodes[1].key = 0

#Initialize V-X
V_X = jzHeap()
for node in nodes[2:]:
    node.key = computeKey(node)
    V_X.push(node)

while V_X.heapList:
    minItem = V_X.getMin()
    if len(V_X.heapList) == 1:
        pass
    minItem.isX = True
    X.append(minItem)
    end1s = [edges[edgeIndex][0] for edgeIndex in minItem.edge]
    end2s = [edges[edgeIndex][1] for edgeIndex in minItem.edge]
    ends = end1s + end2s
    for nodeIndex in ends:
        theNode =nodes[nodeIndex]
        if not theNode.isX:
            V_X.deleteItem(theNode.index)
            theNode.key = computeKey(theNode)
            V_X.push(theNode)
                    
    
    
print("Overall cost of a minimum spanning tree"+str(sum([x.key for x in X])))
    