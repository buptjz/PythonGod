
def merge_sort(numbers):
    length = len(numbers)
    if length < 2 :
        return numbers
    left = merge_sort(numbers[:int(length/2)])
    right = merge_sort(numbers[int(length/2):])
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
            sortedList[i] = right[rightPoint]
            rightPoint += 1

    return sortedList
            
a = [0,100,1,3,2,4,5,7,9,8,10,31,24,52]
print(merge_sort(a))
