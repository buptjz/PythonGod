# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [i for i in L if i%num != 0]



## Problem 2
def myLists(L): return [list(range(1,i+1)) for i in L]



## Problem 3
def myFunctionComposition(f, g): return {k: g[v] for (k,v) in f.items()}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1+0.001j
complex_addition_d = .001+9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L): return sum(L)



## Problem 7
def myProduct(L):
    p = 1
    for i in L:
        p *= i
    return p

## Problem 8
def myMin(L): return min(L)



## Problem 9
def myConcat(L): 
    retStr  = ""
    for item in L:
        retStr+= item
    return retStr

## Problem 10
def myUnion(L): 
    retSet = set()
    for itemSet in L:
        retSet = retSet | itemSet
    return retSet
