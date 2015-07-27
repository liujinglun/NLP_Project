#! /usr/bin/python

f = open("../New_Wiki.txt", 'r') 
i = 0
file_num = 1
lines = ""
for line in f:
    if i < 100000:
        lines = lines + line
        i = i + 1
        #print i
    else:
        f1 = open(str(file_num) + ".txt", 'w')
        f1.write(lines)
        f1.close()
        i = 1
        lines = line
        file_num = file_num + 1
        #print i
if lines != "":
    f1 = open(str(file_num) + ".txt", 'w')
    f1.write(lines)
