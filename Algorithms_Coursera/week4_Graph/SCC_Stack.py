#HW for Programming Question-4 
#computing strongly connected components (SCCs)
from Stack import Stack
import copy,sys   
#If not set this, report "RuntimeError: maximum recursion depth exceeded"
import sys
import threading
import datetime

threading.stack_size(2**27)
sys.setrecursionlimit(10**9)

class Node():
    def __init__(self,number):
        self.nextNodes = []
        self.number = number
        self.explored = False

    def addNext(self,headNumber):
        self.nextNodes.append(headNumber)
    
    def getNextNodes(self):
        return self.nextNodes

    def setExplored(self):
        self.explored = True
    
    def isExplored(self):
        return self.explored

def DFS1(node):
    global leader,s,finishT,revNodeList
    node.setExplored()
    adjNodes = node.getNextNodes()
    for headNumber in adjNodes:
        if not revNodeList[headNumber].isExplored():
            DFS1(revNodeList[headNumber])
    finishT.append(node.number)
    
def DFS2(node):
    global leader,s,finishT,nodeList
    node.setExplored()
    leader[node.number] = s.number
    adjNodes = node.getNextNodes()
    for headNumber in adjNodes:
        if not nodeList[headNumber].isExplored():
            DFS2(nodeList[headNumber])

    
def main():
    starttime = datetime.datetime.now()

    #create empty nodeList
    NODELENGTH = 875714
    global leader,s,t,finishT,revNodeList,nodeList
    t = 0
    leader = [i for i in range(NODELENGTH+1)]
    finishT = []
    leader[0] = -1
    nodeList = [Node(i) for i in range(NODELENGTH+1)]
    revNodeList = copy.deepcopy(nodeList)
    
    #read data from file and set values to 2 nodeLists
    edges = list(open('SCC.txt'))
    for edge in edges:
        tailNumber = int(edge.split()[0])
        headNumber = int(edge.split()[1])
        nodeList[tailNumber].addNext(headNumber)
        revNodeList[headNumber].addNext(tailNumber)
        
    #The first loop, on Grev
    for j in reversed(range(1,NODELENGTH+1)):
        curNode = revNodeList[j]
        if (curNode.isExplored() == False):
            DFS1(curNode)
            
    #The sec loop, on G
    for i in reversed(finishT):
        curNode = nodeList[i]
        if not curNode.isExplored():
            s = curNode
            DFS2(curNode)

    print(leader)
    
    sumup = {}
    
    #cal the top 5
    for item in leader:
        if not item in sumup:
            sumup[item] = 1
        else:
            sumup[item] += 1
    print sorted(sumup.iteritems(), key = lambda x:x[1] ,reverse = True)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()