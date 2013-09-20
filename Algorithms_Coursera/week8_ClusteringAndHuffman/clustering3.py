#https://class.coursera.org/algo2-002/forum/thread?thread_id=127
#Takes too many time...,unbearable, O(n2)
def distanceOf(a,b):
    dis = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dis +=1
    return dis


def clustering():
    pass
    

#Load Data & Initialize
theFile = open("clustering_big.txt",'r')
lines = theFile.readlines()
theFile.close()
numberNodes = int(lines[0].split()[0])
numberBits = int(lines[0].split()[1])
lines = lines[1:]
nodes = [l.split() for l in lines]
nodes.insert(0,[i for i in range(numberBits)])#align

node_cluster_index = [i for i in range(numberNodes+1)]#[0,1,2,.....,20000]
clusters = {k:[k] for k in range(numberNodes+1)}#{1:[1],2:[2],.....,20000:[20000]}

#conver ['1','0','1'] to [True,False,True]
convertFunc = lambda x:True if x=='1' else False
for counter,node in enumerate(nodes):
    nodes[counter] = [convertFunc(b) for b in node]
    
for i in range(1,numberNodes + 1):#1~20000
    for j in range(i+1,numberNodes + 1):#(i+1)~20000
        if not node_cluster_index[j] == j:
            continue
        elif distanceOf(nodes[i],nodes[j]) <= 2:
            clusters[node_cluster_index[i]].append(j)
            del clusters[j]
            node_cluster_index[j] = node_cluster_index[i]
    
print(len(clusters.keys()))
print("---")
