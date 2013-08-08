import random 
def readGraph():
    items = list(open("kargerMinCut.txt",'r'))
    graph = {}
    for item in items:
        values = item.split()
        graph[values[0]] = values[1:]
    return graph
    
def contract():
    global graph
    
    #Random Select an Edge
    ranStart = random.choice(graph.keys())
    ranEnd = random.choice(graph[ranStart])
    
    #Merge Srart & End
    while ranEnd in graph[ranStart]:
        graph[ranStart].remove(ranEnd)
    while ranStart in graph[ranEnd]:
        graph[ranEnd].remove(ranStart)
    graph[ranStart] += graph[ranEnd]

    #Delete End point
    graph.pop(ranEnd)

    #update all points
    for k,v in graph.items():
        while ranEnd in v:
            graph[k].remove(ranEnd)
            graph[k].append(ranStart)

def runContractManyTimes():
    global graph
    N = len(graph)
    while N > 2:
        contract()
        N -= 1
    return len(graph.values()[0])


global graph
runTimes = 200*10
lines = 1000
while runTimes>0:
    graph = readGraph()
    newlines = runContractManyTimes()
    if lines > newlines:
        lines = newlines
    runTimes -=1
    print 'runT:',runTimes,'line',newlines
    
print(lines)

