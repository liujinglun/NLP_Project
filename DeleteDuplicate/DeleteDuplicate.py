import sys

#f = open("../test1.txt", 'r')
#f1 = open("result1.txt", 'w')
f = open("../wikitext.txt", 'r')
f1 = open("New_Wiki.txt", 'w')

stop_en_dict = ['a','about','across','after','all','almost','also','am','among',
'an','and','any','are','as','at','be','because','been','but','by','can','could',
'did','does','either','else','ever','every','for','from','he','her','hers','him',
'his','how','however','i','if','in','into','is','it','its','just','least','let',
'me','most','must','my','neither','no','nor','not','of','off','often','on','only',
'or','other','our','rather','she','should','since','so','some','than','that','the',
'their','them','then','there','these','they','this','to','too','us','was','we','were',
'what','when','where','which','while','who','whom','why','with','would','yet','you',
'your',',','.',';',':','(',')','[',']','{','}','-','?','UUUNKKK', 'The']
dot = ['.','+','*','/', ',', '?', ':', ';', '(', ')', '-', '[', ']','\"' , '\'']
#dot = ['.','+','*','/', ',', '?', ':', ';', '(', ')', '-', '[', ']']
#dot = ['.']
for line in f:
    for item in dot:
        line = line.replace(item, " ")
    items = line.split()
    #default splited by space
    for item in items:
        if not (item in stop_en_dict):
            f1.write(str(item) + " ")
    f1.write("\n")
f.close()
print ('finish')
f1.close()
