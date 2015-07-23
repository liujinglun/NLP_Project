import re
import datetime
starttime = datetime.datetime.now()
#long running
#import NLTK
import collections
words = re.findall(r'\w+', open('source.txt').read().lower())
c = collections.Counter(words)
count = sum(c.values())
id = 1
f = open("new-1.txt", 'w')
for i in range(len(c.most_common())):
    print c.most_common()[i][0], c.most_common()[i][1]
    f.write(str(c.most_common()[i][0])+" "+str(id)+" "+str(c.most_common()[i][1])+"\n")
    id = id + 1
endtime = datetime.datetime.now()
print (endtime - starttime).seconds

