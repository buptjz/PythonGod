from heapq import *
def medianMaintain():
    pass

BigHeap = []
SmallHeap = []
median = []
numbers = list(open('Median.txt'))
for index,i in enumerate(numbers):
    newNumber = int(i)   
    if index == 0:
        heappush(BigHeap,newNumber)
        median.append(newNumber)
        continue
    if index == 1:
        heappush(SmallHeap,-newNumber)
        median.append(newNumber)
        continue
    
    medFromBig = heappop(BigHeap)
    medFromSmall = -heappop(SmallHeap)
    heappush(BigHeap,medFromBig)
    heappush(SmallHeap,-medFromSmall)
    
    if newNumber >= medFromBig:
        heappush(BigHeap,newNumber)
    elif newNumber <= medFromSmall:
        heappush(SmallHeap,-newNumber)
    else:
        heappush(BigHeap,newNumber)
    if len(SmallHeap) - len(BigHeap) == 2:
        temp = -heappop(SmallHeap)
        heappush(BigHeap,temp)
        
    if len(BigHeap) > len(SmallHeap):
        med = heappop(BigHeap)
        median.append(med)
        heappush(SmallHeap,-med)
    else:
        med = -heappop(SmallHeap)
        median.append(med)
        heappush(SmallHeap,-med)
    
score = reduce(lambda x,y:x+y,median)
print(len(median))
print(score)
print(score % 10000)