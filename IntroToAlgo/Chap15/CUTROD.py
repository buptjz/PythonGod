import random

from tool import *
def max(a,b):
  if a > b:
    return a
  else:
    return b

@countcalls
def CUTROD(p,n):
  if n == 0:
    return 0
  q = -1
  for i in range(1,n+1):
    q = max(q,p[i]+CUTROD(p,n-i))
  return q


valueList = [0,1,5,8,9,10,17,17,20,24,30]
lastNum = 30
for i in range(20):
  accu = random.randint(1,10)
  lastNum += accu
  valueList.append(lastNum)

print("Which number you want?")
number = input()
x = CUTROD(valueList,number)
print("The optimal solution is:")
print(x)
print('''How many calls on "CUTROD"''')
print(callcounts[CUTROD])
