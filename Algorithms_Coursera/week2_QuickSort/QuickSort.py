import math

def findMedia(numbersDic):
    aT = numbersDic.keys()
    aT.remove(max(aT))
    aT.remove(min(aT))
    return numbersDic[aT[0]]

def quickSortMed(left,right):
    global A,count

    if right-left < 1:#quit if length <=1
        return 
    
    #the pivot has to compare with the other m-1 numbers.
    count += (right-left+1)-1
    middle = int(math.floor((left+right)/2))
    mediumIndex = 0
    if right-left == 1:
        mediumIndex = left
    else:    
        mediumIndex = findMedia({A[left]:left,A[right]:right,A[middle]:middle})
        
    A[left],A[mediumIndex] = A[mediumIndex],A[left]
    pivot = A[left]
    bound = left+1
    
    #compare with the other m-1 numbers
    for i in range(left+1,right+1):
        if A[i] < pivot:
            A[i],A[bound] = A[bound],A[i]
            bound +=1
    
    #Exchange the value of the first number and the last one which is less than the fist number.
    A[left],A[bound-1] = A[bound-1],A[left]
    quickSortMed(left,bound-2)
    quickSortMed(bound,right)
    
def quickSortLast(left,right):
    global A,count
    
    if right-left < 1:#quit if length <=1
        return 
    
    #the pivot has to compare with the other m-1 numbers.
    count += (right-left+1)-1
    A[left],A[right] = A[right],A[left]
    pivot = A[left]
    bound = left+1
    
    #compare with the other m-1 numbers
    for i in range(left+1,right+1):
        if A[i] < pivot:
            A[i],A[bound] = A[bound],A[i]
            bound +=1
    
    #Exchange the value of the first number and the last one which is less than the fist number.
    A[left],A[bound-1] = A[bound-1],A[left]
    quickSortLast(left,bound-2)
    quickSortLast(bound,right)
    
def quickSort(left,right):
    global A,count

    if right-left < 1:#quit if length <=1
        return 
    
    #the pivot has to compare with the other m-1 numbers.
    count += (right-left+1)-1
    pivot = A[left]
    bound = left+1
    
    #compare with the other m-1 numbers
    for i in range(left+1,right+1):
        if A[i] < pivot:
            A[i],A[bound] = A[bound],A[i]
            bound +=1
    
    #Exchange the value of the first number and the last one which is less than the fist number.
    A[left],A[bound-1] = A[bound-1],A[left]
    quickSort(left,bound-2)
    quickSort(bound,right)
    
#count : How many comparisons
#A : The unsorted array

global A,count 
count = 0
values = list(open("QuickSort.txt",'r'))
A =[int(i) for i in values]
#A = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
quickSort(0,len(A)-1)
print(A)
print(count)

#print(findMedia({13:10,12:12,15:30}))

