import sys
from os.path import exists
fileCount = 1
#def splitFile(fileName, partSize=1):
#fileName = "New_Wiki.txt"
fileName = "../test1.txt"
f1 = open(fileName, 'r')
LineNumber = 0;
count = 5
while True:
	newFile = "newFilePart"+str(fileCount)+".txt"
	fileCount = fileCount + 1
	f2 = open(newFile, "w")
	content = f1.readlines()
	for LineNumber in range(0, 4):
		print str(content[LineNumber])+str(LineNumber)+"\n"
		f2.write(content[LineNumber])
	for LineNumber in range(0, 4)
	    content.pop(LineNumber)
	LineNumber = 0
	if content == "":
		break
f1.close()
f2.close()
print 'split file complete!'
