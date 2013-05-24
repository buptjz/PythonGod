ACTSS = [{'start':1,'end':4},{'start':3,'end':5},{'start':0,'end':6},{'start':5,'end':7},\
     {'start':3,'end':9},{'start':5,'end':9},{'start':6,'end':10},{'start':8,'end':11},\
     {'start':8,'end':12},{'start':2,'end':14},{'start':12,'end':16}]

ACTS = [{'start':1,'end':4},{'start':0,'end':6},{'start':5,'end':7}]
def Dynamic_Selector(start,end):
    i = 0
    r= []
    s = []
    for x in range(len(ACTS)):
        r.append(-1)
        s.append(-1)
        
    for act in ACTS:
        maxact = -3
        for subact in getSubset(start,act['end']):
            if maxact < len(getSubset(start,subact['start']))+len(getSubset(subact['end'],act['end']))+1:
                maxact = len(getSubset(start,subact['start']))+len(getSubset(subact['end'],act['end']))+1
                s[i] = subact
            r[i] = maxact
        i+=1
    
    return r,s

def getSubset(x,y):
    a = []
    for act in ACTS:
        if act['start'] >= x and act['end']<= y:
            a.append(act)
    return a

print(Dynamic_Selector(0,16))
