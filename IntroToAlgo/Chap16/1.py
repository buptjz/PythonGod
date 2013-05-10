ACTSS = [{'start':1,'end':4},{'start':3,'end':5},{'start':0,'end':6},{'start':5,'end':7},\
     {'start':3,'end':9},{'start':5,'end':9},{'start':6,'end':10},{'start':8,'end':11},\
     {'start':8,'end':12},{'start':2,'end':14},{'start':12,'end':16}]

ACTS = [{'start':1,'end':4},{'start':3,'end':5},{'start':0,'end':6},{'start':5,'end':7}]

best = []
def Dynamic_Selector(start,end):
    subSet = getSubset(start,end)
    if len(subSet) == 0:
        return 0
    tempact = {}
    maxact = 1    
    for act in subSet:
        num = Dynamic_Selector(start,act['start'])+Dynamic_Selector(act['end'],end)+1
        if num > maxact:
            maxact = num
            tempact = act
    best.append(act)
    return maxact

def getSubset(x,y):
    a = []
    for act in ACTS:
        if act['start'] >= x and act['end']<= y:
            a.append(act)
    return a

Dynamic_Selector(0,16)
print(best)