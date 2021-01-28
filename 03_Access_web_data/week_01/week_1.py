import re 
x='My 2 favorite numbers are 19 and 44'
y=re.findall('[0-9]+',x)
print(y)
hand=open('mbox-short.txt')
numlist =list()
for line in hand:
    line =line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) !=1: continue
    num=float(stuff[0])
    #print(num)
    numlist.append(num)
print('list:',numlist)    
print('Maximun:',max(numlist))
