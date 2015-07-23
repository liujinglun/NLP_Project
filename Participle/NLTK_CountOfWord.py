#60s
import os
import nltk
import datetime
starttime = datetime.datetime.now()
FilePath = '0.txt'
#read every line and get the frequecy, then put them into the dictionary,
#dictionar is used to store the word and its frequencys
dictionary = {}
f1 = open(FilePath, 'r')
f2 = open("new-2.txt", 'w')
text = f1.read()
text = text.replace('\n', ' ')
fredist = nltk.FreqDist(text.split(' '))
print fredist
#print fredist.keys()
for localkey in fredist.keys():
	if localkey in dictionary.keys():
		dictionary[localkey] = dictionary[localkey]+fredist[localkey]
	else:
		dictionary[localkey] = fredist[localkey]
pair = sorted(dictionary.items(), key = lambda x:x[1], reverse=True)
print pair
#print pair
for item in pair:
	a, b = item
	f2.write(a+" "+str(b)+"\n")
f1.close()
f2.close()
endtime = datetime.datetime.now()
print "time: "+str((endtime - starttime).seconds)
