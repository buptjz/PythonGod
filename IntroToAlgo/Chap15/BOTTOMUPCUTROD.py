import random

from tool import *

@countcalls
def max(a,b):
  if a > b:
    return a
  else:
    return b

@countcalls
def CUTROD(p,n,memo):
  for j in range(1,n+1):
    q = -100
    for i in range(1,j+1):
      q = max(q,p[i]+memo[j-i])
    memo[j] = q
  return memo[n]

memo = []
for i in range(31):
  memo.append(0)

valueList = [0,1,5,8,9,10,17,17,20,24,30,35,38,42,45,50,51,54,54,60,62,65,70,71,72,73,77,79,80,85,86]
print("Which number you want?")
number = input()
x = CUTROD(valueList,number,memo)
print("The optimal solution is:")
print(x)
print('''How many calls on "max"''')
print(callcounts[max])
