#Try to implement the heap data structure
#1)pop the minimum item in O(logN)
#2)push an item in O(logN)
#heap is a balance tree,children are bigger their parent
#Althugh it's a balance tree,we can implement it by using a list
class jzHeap:
    def __init__(self,initialList = []):
        self.heapList = initialList
    
    def deleteItem(self,index):
        #Delete the index item and move the last item to this index,and then try bubbleDown
        #If bubbleDown does nothing,try bubbleUp
        
        #if delete the last,do it directly
        if len(self.heapList) == index+1:
            del self.heapList[-1]
            return
        
        self.heapList[index] = self.heapList[-1]
        self.heapList[index].index = index
        
        del self.heapList[-1]
        if len(self.heapList) <= 0 :
            return
        temp = self.heapList[index]
        self.bubbleDown(index)
        if self.heapList[index] == temp:
            self.bubbleUp(index)
        return
        
    def getMin(self):
        retItem = self.heapList[0]
        if len(self.heapList) == 1:
            del self.heapList[-1]
            return retItem
        self.heapList[0] = self.heapList[-1]
        self.heapList[0].index = 0
        del self.heapList[-1]
        self.bubbleDown(0)
        
        return retItem
    
    def push(self,item):
        item.index = len(self.heapList)
        self.heapList.append(item)
        self.bubbleUp(len(self.heapList) - 1)
    
    def bubbleUp(self,index):
        '''
        Recursively Check if the index node is smaller than it's parent,if true,exchange the value 
        '''
        #if node < parent,exchange
        if index <= 0:
            return
        parent = (index - 1) / 2
        if self.heapList[index] < self.heapList[parent]:
            self.heapList[index],self.heapList[parent] = self.heapList[parent],self.heapList[index]
            
            #Set the index of the exchanged two nodes
            self.heapList[index].index = index
            self.heapList[parent].index = parent
            
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
                    
                    #Set the index of the exchanged two nodes
                    self.heapList[index].index = index
                    self.heapList[index * 2 + 1].index = index * 2 + 1
                    
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
                
                #Set the index of the exchanged two nodes
                self.heapList[index].index = index
                self.heapList[smallerOne].index = smallerOne
                    
                self.bubbleDown(smallerOne)
        return

def test():
    heap = jzHeap([1,8,4,9,12,7])
    print(111)
#test()