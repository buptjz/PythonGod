downloadFile = "/home/wangjz/Desktop/imageContent.txt"
df = open(downloadFile,'r')
downImages = df.readlines();
df.close()

dataSet = "/home/wangjz/Desktop/photonet_dataset.txt"
ds = open(dataSet,'r')
dataSetImage = ds.readlines()
ds.close()

DownImagesList = []
noneDownImagesList = []
downImagesNameList = []

for i in downImages:
    downImagesNameList.append(i.split('.')[0])


for image in dataSetImage:
    imageName = image.split()[1]
    if imageName in downImagesNameList:
        DownImagesList.append(image)
        #print('Down ++' + image)
    else:
        noneDownImagesList.append(image)
        #print('NoneDown --' + image)

print(noneDownImagesList)

noneDownloadFile = "/home/wangjz/Desktop/noneDownloadFile.txt"
ndf = open(noneDownloadFile,'w')  
ndf.writelines(noneDownImagesList)
ndf.close()

downloadFile = "/home/wangjz/Desktop/downloadFile.txt"
df = open(downloadFile,'w')  
df.writelines(DownImagesList)
df.close()



