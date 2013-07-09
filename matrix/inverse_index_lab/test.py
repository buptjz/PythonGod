from inverse_index_lab import *

testFile = open("./stories_small.txt",'r')
strList = testFile.readlines()

inverseDic = makeInverseIndex(strList)
result = andSearch(inverseDic,["even","it"])
print(result)