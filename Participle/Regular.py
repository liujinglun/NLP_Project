#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
from operator import itemgetter

def readfile(f):
    with file(f,"r") as pFile:
        return pFile.read()
        
def divide(c, regex):
    #the regex below is only valid for utf8 coding
    return regex.findall(c)
    
def update_dict(di,li):
    for i in li:
        if di.has_key(i):
            di[i]+=1
        else:
            di[i]=1
    return di
    
def main():
	#files=sys.argv[1:] 
	#for f in files:
    #receive files from bash
    f='0.txt'
    f2 = open('new-3.txt', 'w')
    
    #regex compile only once
    regex=re.compile("(?x) (?: [\w-]+  | [\x80-\xff]{3} )")

    dict={}

    #get all words from files
    words=divide(readfile(f), regex)
    dict=update_dict(dict, words)

    #sort dictionary by value 
    #dict is now a list.
    dict=sorted(dict.items(), key=itemgetter(1), reverse=True)

    #output to standard-output
    for i in dict:
        print i[0], i[1]
        f2.write(i[0]+" "+str(i[1])+'\n')

    f2.close()

if __name__=='__main__':
    main()