def main():
    filePath = "J:\coursera-master\coursera\ml-003\ex1\ex1data1.txt"
    data = readData(filePath)
    
def readData(filePath):
    data = [[],[]]
    dataFile = open(filePath,'r')
    rawdata = dataFile.read()
    valuesList = rawdata.split()
    for value in valuesList:
        x = value.split(',')
        data[0].append(float(x[0]))
        data[1].append(float(x[1]))    
 
main()