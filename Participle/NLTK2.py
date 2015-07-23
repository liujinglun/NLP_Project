#133s
import os
import nltk
import datetime
from nltk.tokenize import word_tokenize
import datetime
starttime = datetime.datetime.now()
FilePath = "newFilePart0.txt"
dictionary = {}
j = 0
f1 = open(FilePath, "r")
f2 = open("Part0_Result.txt", 'w')
#f3 is a list
f3 = f1.readlines()
for line in f3:
    print str(j)+" of "+str(len(f3))
    tokens = nltk.word_tokenize(line)
    fredist=nltk.FreqDist(tokens)
    #fredist = nltk.FreqDist(line.split())
    print fredist
    j = j + 1
    for localkey in fredist.keys():
	    if localkey in dictionary.keys():
		     dictionary[localkey] = dictionary[localkey]+fredist[localkey]
	    else:
		     dictionary[localkey] = fredist[localkey]
pair = sorted(dictionary.items(), key = lambda x:x[1], reverse=True)
for item in pair:
	a, b = item
	f2.write(a+" "+str(b)+"\n")
f1.close()
f2.close()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
