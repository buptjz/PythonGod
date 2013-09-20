'''
In this question your task is again to run the clustering algorithm from lecture, but on a MUCH bigger graph. 
So big, in fact, that the distances (i.e., edge costs) are only defined implicitly, rather than being provided as an explicit list.

The data set is here. The format is:
[# of nodes] [# of bits for each node's label]
[first bit of node 1] ... [last bit of node 1]
[first bit of node 2] ... [last bit of node 2]
...
For example, the third line of the file "0 1 1 0 0 1 1 0 0 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1" denotes the 24 bits associated with node #2.

The distance between two nodes u and v in this problem is defined as the Hamming distance--- the number of differing bits ---
between the two nodes' labels. For example, the Hamming distance between the 24-bit label of node #2 above and the label 
"0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 1 0 1 0 0 1 0 1" is 3 (since they differ in the 3rd, 7th, and 21st bits).

The question is: what is the largest value of k such that there is a k-clustering with spacing at least 3? 
That is, how many clusters are needed to ensure that no pair of nodes with all but 2 bits in common get split into different clusters?

NOTE: The graph implicitly defined by the data file is so big that you probably can't write it out explicitly, let alone sort the edges by cost. 
So you will have to be a little creative to complete this part of the question. For example, is there some way you can identify the smallest 
distances without explicitly looking at every pair of nodes?
'''
#Algorithms: Design and Analysis, Part 2 
#Q2 of  Programming Assignment #2 
#https://class.coursera.org/algo2-002/forum/thread?thread_id=127
from Union import Union

def changeBit(string,index):
    final = "0" if string[index] == "1" else "1"
    if index == len(string) - 1 :
        return string[:index] + final
    else:
        return string[:index] + final + string[index+1:]
        
def changeBit2(string,index1,index2):
    return changeBit(changeBit(string,index1),index2)

def computeCandidates(bits):
    candidates = []
    for i in range(numberBits):
        candidates.append(changeBit(bits,i))
    for i in range(numberBits):
        for j in range(i+1,numberBits):
            candidates.append(changeBit2(bits,i,j))
    return candidates

#Load Data & Initialize
theFile = open("clustering_big.txt",'r')
lines = theFile.readlines()
theFile.close()
numberNodes = int(lines[0].split()[0])
numberBits = int(lines[0].split()[1])
lines = lines[1:]
nodes = [l.split() for l in lines]


unionOfNodes = Union(numberNodes)

#Put all nodes in a hashTable
nodesHash = {}
for counter,n in enumerate(nodes):#counter 0~19999
    BitRep = "".join(n)
    if nodesHash.has_key(BitRep):#In fact,there's some node has the same bit!
        unionOfNodes.union_sets(counter+1,nodesHash[BitRep] )
    else:
        nodesHash[BitRep] = counter+1

#Go through all nodes
c = 0
for bitSeq in nodesHash.keys():
    c+=1
    print(c)
    nodeIndex = nodesHash[bitSeq]
    candidates = computeCandidates(bitSeq)
    for candi in candidates:
        if nodesHash.has_key(candi):
            unionOfNodes.union_sets(nodeIndex,nodesHash[candi])

print(unionOfNodes.number_roots())