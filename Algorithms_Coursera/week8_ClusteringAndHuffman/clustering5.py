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