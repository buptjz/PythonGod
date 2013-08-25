class Node:
    def __init__(self,nodeID):
        self.nodeID = nodeID
        self.adjacent = []

def readData():
    items = list(open('dijkstraData.txt'))
    #items = list(open('testCase.txt'))
    nodes = []
    for item in items:
        newNode = Node(int(item.split()[0]))
        for adj in item.split()[1:]:
            u = int(adj.split(',')[0])
            v = int(adj.split(',')[1])
            newNode.adjacent.append((u,v))
        nodes.append(newNode)
    return nodes
    
def DJ():
    global U,V,A,nodes
    shortest = (None,None,100000)#(u,v,distance)
    for nodeID_U in U:
        distance_U = A[nodeID_U-1] 
        for nodeID_V,disFromUtoV in nodes[nodeID_U-1].adjacent:
            if nodeID_V in V and (disFromUtoV+distance_U < shortest[2]):
                shortest = (nodeID_U,nodeID_V,disFromUtoV+distance_U)
               #print (shortest)

    U.append(shortest[1])
    V.remove(shortest[1])
    if shortest[1] == 198:
        print(1)
    A[shortest[1]-1] = shortest[2]
    #print shortest,A[shortest[1]-1] 
    #print (shortest)
    #print(U)
    #print ('---------------')
                #candidate.append((nodeID_U,nodeID_V,disFromUtoV+A[nodeID_U-1]))
            

NODELENGTH = 200
def main():
    global U,V,A,nodes
    U = []
    V = []
    nodes = readData()
    U.append(nodes[0].nodeID)#Put s into U
    V = [i.nodeID for i in nodes[1:]]#Other nodes into V
    A = [10000 for i in range(NODELENGTH)]#init A which records the shortest distance
    A[0] = 0#distance from start point to start point is 0

    while len(V) >= 1:
        DJ()
    supposed = [7,37,59,82,99,115,133,165,188,197]
    #supposed = [6,38,58,83,100,116,132,166,181,198]
    
    print([A[i-1] for i in supposed])
    #print(A)
    #2818,3548,3668,3997,2970,3513,2468,3814,2345,1724
    2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

main()
        