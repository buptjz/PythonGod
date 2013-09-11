'''
In this programming problem and the next you'll code up the greedy algorithms from lecture 
for minimizing the weighted sum of completion times.. Download the text file here. 
This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. 
You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in 
decreasing order of the difference (weight - length). Recall from lecture that this algorithm 
is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), 
you should schedule the job with higher weight first. Beware: if you break ties in a different way, 
you are likely to get the wrong answer. You should report the sum of weighted completion times 
of the resulting schedule --- a positive integer --- in the box below. 
'''
jobsFile = open('jobs.txt','r')
lines = jobsFile.readlines()[1:]

jobs = []
length,weight = 0,0

for line in lines:
    weight = int(line.split()[0])
    length = int(line.split()[1])
    jobs.append([weight,length,weight - length])

jobs = sorted(jobs,key = lambda x:(x[2],x[0]))
jobs = jobs[-1::-1]#inverse, decreasing order
sumTime = 0
sumLength = 0 
for job in jobs:
    sumLength += job[1]
    sumTime += job[0] * sumLength
print(sumTime)
    