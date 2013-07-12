
def count_inversions(numbers):
    length = len(numbers)
    leftLenght = int(length/2)
    rightLength = length - leftLenght

    if length < 2 :
        return (0,numbers)
    
    leftInv,left = count_inversions(numbers[:leftLenght])
    rightInv,right = count_inversions(numbers[leftLenght:])
    
    #merge & count split inversions
    splitInv = 0
    sortedList = [i for i in range(length)]
    leftPoint,rightPoint = 0,0
    for i in range(length):
        if leftPoint == len(left):
            sortedList[i:] = right[rightPoint:]
            break
        if rightPoint == len(right):
            sortedList[i:] = left[leftPoint:]
            break

        if left[leftPoint] < right[rightPoint]:
            sortedList[i] = left[leftPoint]
            leftPoint += 1
        else:
            splitInv += leftLenght - leftPoint
            sortedList[i] = right[rightPoint]
            rightPoint += 1
    totalSplit = leftInv+rightInv+splitInv
    return totalSplit,sortedList
            
values = list(open("IntegerArray.txt",'r'))
numbers =[int(i) for i in values]
count,sortedList = count_inversions(numbers)
print(count)
print(sortedList)
