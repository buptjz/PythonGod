#The prototype of this implementation comes this book:
#<The Algorithm Design Manual 2nd Edition P200>
class Union:
    def __init__(self,n):
        self.parents = [0]
        self.sizes = [1 for i in range(n+1)]
        for i in range(1,n+1):#1~n
            self.parents.append(i)
        self.number = n;
        
    def find(self,index):
        if self.parents[index] == index:
            return index
        else:
            return(self.find(self.parents[index]))
    
    def union_sets(self,index1,index2):
        r1 = self.find(index1)
        r2 = self.find(index2)
        if r1 == r2:
            return
        if self.sizes[r1] >= self.sizes[r2]:
            self.sizes[r1] += self.sizes[r2]
            self.parents[r2] = r1
        else:
            self.sizes[r2] += self.sizes[r1]
            self.parents[r1] = r2
            
    def same_component(self,index1,index2):
        return self.find(index1) == self.find(index2)
    
    def number_roots(self):
        result = -1#Because the 0 index
        for counter,p in enumerate(self.parents):
            if p == counter:
                result +=1
        return result