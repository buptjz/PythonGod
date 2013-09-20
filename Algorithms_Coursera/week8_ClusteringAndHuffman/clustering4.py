#Try to solve Q2,failed again.

def merge(A,B):
    if not node_cluster_index[A] == node_cluster_index[B]:
        clusters[node_cluster_index[A]] += clusters[node_cluster_index[B]]  
        temp = node_cluster_index[B]
        for nodeI in clusters[node_cluster_index[B]]:
            node_cluster_index[nodeI] = node_cluster_index[A]
        del clusters[temp]
        
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

node_cluster_index = [i for i in range(numberNodes+1)]#[0,1,2,.....,20000]
clusters = {k:[k] for k in range(numberNodes+1)}#{1:[1],2:[2],.....,20000:[20000]}

#Put all nodes in a hashTable
nodesHash = {}
for counter,n in enumerate(nodes):#counter 0~19999
    BitRep = "".join(n)
    if nodesHash.has_key(BitRep):#In fact,there's some node has the same bit!
        del clusters[counter+1]
    else:
        nodesHash[BitRep] = counter+1

#Go through all nodes
for bitSeq in nodesHash.keys():
    nodeIndex = nodesHash[bitSeq]
    candidates = computeCandidates(bitSeq)
    for candi in candidates:
        if nodesHash.has_key(candi):
            merge(nodeIndex,nodesHash[candi])

print(len(clusters.values()))