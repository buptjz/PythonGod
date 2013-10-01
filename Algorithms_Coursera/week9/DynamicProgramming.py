'''
Week9 Dynamic Programming

In this programming problem and the next you'll code up the knapsack algorithm from lecture. 
Let's start with a warm-up. Download the text file here. 
This file describes a knapsack instance, and it has the following format:
[knapsack_size][number_of_items]
[value_1] [weight_1]
[value_2] [weight_2]
...
For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.
In the box below, type in the value of the optimal solution. 
'''
from copy import deepcopy
def compute(nodes):
    nodes.insert(0,None)

    #Init A
    row = [None for i in range(knapsack_size+1)]#10000 items
    A = [deepcopy(row) for i in range(number_of_items+1)]#101 items
    for i in range(knapsack_size+1):
        A[0][i] = 0
        
    #Dynamic Process
    for i in range(1,number_of_items+1): 
        for x in range(knapsack_size+1):
            if x-nodes[i][1] < 0 :
                A[i][x]  = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x],A[i-1][x-nodes[i][1]] + nodes[i][0])
    return A

theFile = open('knapsack1.txt','r')
lines = theFile.readlines()
knapsack_size = int(lines[0].split()[0])
number_of_items = int(lines[0].split()[1])
items = []
for l in lines[1:]:
    items.append([int(l.split()[0]),int(l.split()[1])])

mat = compute(items)
print(-1)


