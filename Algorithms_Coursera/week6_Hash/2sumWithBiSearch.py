#First of all,sort all the given numbers,then go through every number in the sortedList,for each nunumber A,
#find (Use binary search to find the index range) all the other numbers B where -10000<=A+B <=10000
#then put every sum of A+B in the record list
#This is more fast than the algorithms in 2SUM.py which takes O(20000*1000000)
#Algorithm in this file may take O(1000000*log1000000)
def binarySearch(start,end,targetValue):
    global sortedList
    if end - start <=1:
        return start
    mid = (start+end) / 2
    if targetValue == sortedList[mid]:
        return mid 
    elif targetValue > sortedList[mid]:
        return binarySearch(mid,end,targetValue)
    elif targetValue < sortedList[mid]:
        return binarySearch(start,mid,targetValue)

def twoSum():
    global sortedList
    i = 0
    #-10000<=canA+canB<=10000
    sumValuesList = [0 for i in range(-10000,10000+1)]
    length = len(sortedList)
    for candidateA in sortedList:
        start = binarySearch(0,length,-10000-candidateA)
        end = binarySearch(0,length,10000-candidateA)+1
        for candidateB in sortedList[start:end+1]:
            sumValue = candidateA + candidateB
            if sumValue <= 10000 and sumValue >=-10000:
                sumValuesList[sumValue+10000] = 1
        print(i)
        i +=1
            
    return sumValuesList
            
numbers = list(open('2sum.txt'))
sortedList = sorted([int(k) for k in numbers])
final = twoSum()
score = reduce(lambda x,y:(x+y), final)
print(score)
