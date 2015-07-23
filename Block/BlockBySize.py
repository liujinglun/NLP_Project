import sys
from os.path import exists
fileCount = 0
#def splitFile(fileName, partSize=1):
fileName = "../New_Wiki.txt"
partSize = 500;
    # 1024 * 1024 = 1048576
length = partSize * 1048576
f1 = open(fileName, "r")
while True:
    content = f1.read(length)
    if content == "":
        break
        #newFile = distFile(fileName)
    newFile = "newFilePart"+str(fileCount)+".txt"
    fileCount = fileCount + 1
    f2 = open(newFile, "w")
    f2.write(content)
f2.close()
f1.close()
print 'split file complete!'

