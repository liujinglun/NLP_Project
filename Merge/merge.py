import sys
f1 = open("Batchpart4.txt", 'r')
f2 = open("test.txt", 'r')
f3 = open("result.txt", 'w')

map1={}
#map2={}
for line in f1:
	key = line.split(' ')[0]
	value = line.split(' ')[2]
	if map1.has_key(key):
		map1[key]= map1[key] + int(value)
	else:
		map1[key] = int(value)
#print map1
for line in f2:
    key = line.split(' ')[0]
    value = line.split(' ')[2]
    #print key+" "+value
    if map1.has_key(key):
        map1[key]= map1[key] + int(value)
    else:
    	map1[key] = int(value)

map2 = sorted(map1.iteritems(), key=lambda d:d[1], reverse=True)
#print mp2
for item in map2:
	a, b = item;
	f3.write(a + " " + str(b) + "\n")
#print map2
f1.close()
f2.close()
f3.close()
    
