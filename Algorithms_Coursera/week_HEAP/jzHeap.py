#Try to implement the heap data structure
#1)pop the minimum item in O(logN)
#2)push an item in O(logN)
#heap is a balance tree,children are bigger their parent
#Althugh it's a balance tree,we can implement it by using a list
class jzHeap:
    def __init__(self,initialList = []):
        self.heapList = initialList
    
    def getMin(self):
        retItem = self.heapList[0]
        self.heapList[0] = self.heapList[-1]
        del self.heapList[-1]
        self.bubbleDown(0)
        
        return retItem
    
    def push(self,item):
        self.heapList.append(item)
        self.bubbleUp(len(self.heapList) - 1)
    
    def bubbleUp(self,index):
        '''
        Recursively Check if the index node is smaller than it's parent,if true,exchange the value 
        '''
        #if node < parent,exchange
        parent = (index - 1) / 2
        if self.heapList[index] < self.heapList[parent]:
            self.heapList[index],self.heapList[parent] = self.heapList[parent],self.heapList[index]
            self.bubbleUp(parent)
        return
    
    def bubbleDown(self,index):
        '''
        Recursively Check if the index node is smaller than it's children,if not,exchange the value 
        '''
        #no right child
        if len(self.heapList) <= index * 2 + 2:
            #no right child and left child
            if len(self.heapList) <= index * 2 + 1:
                return
            #no right but has left
            else:
                #left > index
                if self.heapList[index] > self.heapList[index * 2 + 1]:
                    self.heapList[index],self.heapList[index * 2 + 1] = \
                        self.heapList[index * 2 + 1],self.heapList[index]
                    self.bubbleDown(index * 2 +1)
                #left <= index
                else:
                    return
        #has right child
        else :
            smallerOne = (index * 2 + 1 ) if self.heapList[index * 2 + 1] < self.heapList[index * 2 + 2] \
                      else (index * 2 + 2 ) 
            #index > the smaller one of the two child
            if self.heapList[index] > self.heapList[smallerOne]:
                self.heapList[index],self.heapList[smallerOne] = self.heapList[smallerOne],self.heapList[index]
                self.bubbleDown(smallerOne)
        return

#here's some test
heapQB = jzHeap([1,4,5,9,10,6,7])
heapQB.push(3)
heapQB.push(2)
heapQB.getMin()
#heapQB.getMin()
#heapQB.getMin()
print(heapQB.heapList)
        