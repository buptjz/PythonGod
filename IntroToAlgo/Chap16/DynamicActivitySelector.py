'''这道习题考察贪心算法和动态规划算法的比较。根据定理16.1，利用贪心算法自顶向下的特性计算最优解比动态规划算法自顶向上计算最优解更有效，渐进执行速度更快。
利用第224页上的递归式（注意i和j的取值范围都是从0到n+1），容易写出动态规划版本的算法：'''

def DYNAMIC_ACTIVITY_SELECTOR(s,f,n):
    # s is the array of start times, f is the array of finish times (sorted), and n is the number of activities.
    for i in range(0,n+1):
        c[(i,i)] = 0
    for l in range(0,n+1):
        for i in range(0,n+1-l):
            j = l + i
            c[(i,j)] = 0
            for k in range(i+1,j-1):
                if f[i] <= s[k] and f[k] <= s[j]:  #test if activity a_k is in S_{ij}
                    q = c[(i,k)] + c[(k,j)] + 1
                    if q > c[(i,j)]:
                        c[(i,j)] = q
                        a[(i,j)] = k
c = {}                      
ACTS = [{'start':1,'end':4},{'start':0,'end':6},{'start':5,'end':7}]
FINISHED = []
DYNAMIC_ACTIVITY_SELECTOR(ACTS,FINISHED,3)
 

'''上述伪代码中c[i,j]为S_{ij}中最大兼容子集中的活动数，
a[i,j]记录子问题划分的最优位置以便于输出最大兼容子集（可以用递归算法输出，细节省略）。
该算法的第1-2行对i = j的情况初始化（S_{ii}是空集，所以c[i,i] = 0）。
在第3-12行的循环第一次执行时计算c[i,i+1], i = 0,1,...,n；
在循环第二次执行时计算c[i,i+2], i = 0,1,...,n-1；
以此类推，当循环最后一次执行时计算c[0,n+1]，即最终结果。
注意第3-12行的循环的嵌套层数为3，容易证明算法的运行时间为O(n^3)，
并可进一步证明实际为\theta(n^3)。在f排序的情况下，
GREEDY-ACTIVITY-SELECTOR的运行时间为\theta(n)，
可见贪心算法的渐进运行时间更短。'''
