#shit, got failed!!

theFile = open("clustering1.txt",'r')

lines = theFile.readlines()
numberLines = int(lines[0])
lines = lines[1:]

edges = [[int(line.split()[0]),int(line.split()[1]),int(line.split()[2])] for line in lines]
edges = sorted(edges,key = lambda x:x[2])

pointsClusterIndex = [None for i in range(500+1)]
clusterPoints = [[] for i in range(501)]
clusterIndex = 0
result = None
NextStop = False
for counter,edge in enumerate(edges):
    if NextStop:
        print(edge[2])
        break
    point1 = edge[0]
    point2 = edge[1]
    #if point1 and 2 both not in any cluster
    if pointsClusterIndex[point1] == None and pointsClusterIndex[point2] == None:
        clusterIndex += 1
        pointsClusterIndex[point1]  = clusterIndex
        pointsClusterIndex[point2]  = clusterIndex
        clusterPoints[clusterIndex].append(point1)
        clusterPoints[clusterIndex].append(point2)
    
    #if point1 in some cluster,add point2 not in any cluster
    elif not pointsClusterIndex[point1] == None and pointsClusterIndex[point2] == None:
        pointsClusterIndex[point2] = pointsClusterIndex[point1]
        clusterPoints[pointsClusterIndex[point2]].append(point2)
    #point2 in some cluster ,point1 not in any cluster
    elif not pointsClusterIndex[point2] == None and pointsClusterIndex[point1] == None:
        pointsClusterIndex[point1] = pointsClusterIndex[point2]
        clusterPoints[pointsClusterIndex[point1]].append(point1)
    #both point1 and point2 in some cluster
    else:
        #check if they are in the same cluster,
        if pointsClusterIndex[point1] == pointsClusterIndex[point2]:
            continue
        else:

            (sLeP,bLeP) = (point1,point2) if pointsClusterIndex[point1] < pointsClusterIndex[point2] else (point2,point1)
            
            clusterPoints[pointsClusterIndex[sLeP]] += clusterPoints[pointsClusterIndex[bLeP]]
            clusterPoints[pointsClusterIndex[bLeP]] = [] 
            pointsClusterIndex[bLeP] = pointsClusterIndex[sLeP]
            #clusterIndex -= 1

    a = [i for i in clusterPoints if not i == []]
    if len(a) == 4 and counter > 200:
        NextStop = True
print(1)