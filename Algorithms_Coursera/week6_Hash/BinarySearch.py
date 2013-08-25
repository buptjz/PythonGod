def binarySearch(start,end):
    global targetValue,sortedList
    if end - start <=1:
        return start
    mid = (start+end) / 2
    if targetValue == sortedList[mid]:
        return mid 
    elif targetValue > sortedList[mid]:
        binarySearch(mid,end)
    elif targetValue < sortedList[mid]:
        binarySearch(start,mid)
    
targetValue = 10
sortedList = list(range(20))
result = binarySearch(0,len(sortedList))
