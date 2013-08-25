def printTimesDecorator(f):
    global i
    def aFunc():
        f()
        print 'run in __ %d __' , i
        i+=1
    return aFunc

@printTimesDecorator
def twoSum():
    global hashTable
    i = 0
    sumValuesList = [0 for i in range(-10000,10000+1)]
    allCandidates = hashTable.keys()
    for sumValue in range(-10000,10000+1):
        for firstAddNumber in allCandidates:
            if (sumValue -firstAddNumber) in hashTable:
                sumValuesList[sumValue+10000] = 1
                print "success"
        print (i)
        i+=1
                
    return sumValuesList
            
    #list[sum+10000]

#hashTable = {}
numbers = list(open('2sum.txt'))
hashTable = {int(k):1 for k in numbers}
final = twoSum()
score = reduce(lambda x,y:(x+y), final)
print(score)
#print(len(hashTable))