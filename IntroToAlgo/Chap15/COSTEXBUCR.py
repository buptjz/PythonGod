import random

def CUTROD(p,n,memo,cost):
  for j in range(1,n+1):
    q = p[j]
    cutSolution[j] = j
    for i in range(1,j):
      if q < p[i] + memo[j-i] - cost:
        q = p[i] + memo[j-i] - cost
        cutSolution[j] = i
    memo[j] = q
  return memo,cutSolution

cutSolution = []
memo = []
for i in range(31):
  memo.append(0)
  cutSolution.append(0)

valueList = [0,1,5,8,9,10,17,17,20,24,30,35,38,42,45,50,51,54,54,60,62,65,70,71,72,73,77,79,80,85,86]
print("Which number you want?")
number = input()
print("Enter cost per cut:")
cost = input()
x,y = CUTROD(valueList,number,memo,cost)
print("The optimal solution is:")
print x[number]
while number > 0:
  print y[number],
  number = number - y[number]

