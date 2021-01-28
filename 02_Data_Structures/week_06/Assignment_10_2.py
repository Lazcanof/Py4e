# 10.2 Write a program to read through the mbox-short.txt 
# and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string
#  a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name= input('Enter file:')
handle=open(name)
counts=dict()
for line in handle:
    line.rstrip()
    if  line.startswith('From '): 
       words=line.split()
       hora=words[5]
       #print(hora[:2])
       #print(words[5])
       #print(words)
       counts[hora[:2]]=counts.get(hora[:2],0)+1
       #print(counts)
bigcount=None
bigword=None
for words,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=words
        bigcount=count
#print(bigword, bigcount)
#print(counts)
#lista transformada ordenada
lst=list()
for key,val in counts.items():
    newtup=(key,val)
    lst.append(newtup)
lst=sorted(lst)
for val,key in lst[:]:
    print(val,key)