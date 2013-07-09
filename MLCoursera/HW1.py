#!/usr/bin/env python  
# -*- coding: utf-8 -*-

#Coursera ML-003 HW1，实现一个变量的线性回归算法 ， 要求详见ex1.pdf 

import matplotlib.pyplot as plt 

#计算代价函数，代价函数在batch梯度递减算法中没有实质作用，但是能够辅助我们验证梯度递减算法是否有效。
#在每一次的迭代最开始，调用这个函数，可以发现代价是逐步递减的，不会有任何的增长。
def computeCost(trainData,theta):
    tempCost = 0
    num = len(trainData[0])
    for i in range(num):
        hx = (theta[0]+theta[1]*trainData[1][i])
        tempCost += (hx - trainData[2][i]) * (hx - trainData[2][i])
    return tempCost / (2 * num)
    
def training(trainData):
    iterations = 1500
    alpha = 0.01
    theta = [0,0]
    print(computeCost(trainData,theta))
    numb = len(trainData[0])
    
    #这里执行batch gradient descent
    for i in range(iterations):
        print  computeCost(trainData,theta)
        accum0 = 0
        accum1 = 0
        for i in range(numb):
            hx = (theta[0]+theta[1]*trainData[1][i])
            y = trainData[2][i]
            x0 = trainData[0][i]
            x1 = trainData[1][i]
            accum0 += (hx - y) * x0 
            accum1 += (hx - y) * x1
        theta[0] -= (alpha / numb )* accum0
        theta[1] -= (alpha / numb )* accum1
    print(theta)

#就像在matlab中画图一样，bx表示blue的X
def drawData(data):
    plt.plot(data[0],data[1],'bx')
    plt.show()

def main():
    filePath = "J:\coursera-master\coursera\ml-003\ex1\ex1data1.txt"
    data = readData(filePath)
    #drawData(data)
    onesColumn = []
    for i in range(len(data[0])):
        onesColumn.append(1)
    newData = [onesColumn,data[0],data[1]]
    training(newData)

#读取数据，总共有两列，用逗号隔开，第一列是X，第二列是Y    
def readData(filePath):
    data = [[],[]]
    dataFile = open(filePath,'r')
    rawdata = dataFile.read()
    valuesList = rawdata.split()
    for value in valuesList:
        x = value.split(',')
        data[0].append(float(x[0]))
        data[1].append(float(x[1]))    
    return data
 
main()