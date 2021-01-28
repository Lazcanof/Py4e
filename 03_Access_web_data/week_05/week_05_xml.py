#  Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#  The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract
# the comment counts from the XML data, compute the sum of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    #Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
    #Actual data: http://py4e-data.dr-chuck.net/comments_691291.xml (Sum ends with 72)

#You do not need to save these files to your folder since your program will read the data directly from the URL.
#  Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 

import urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location : ')
output = urllib.request.urlopen(url).read()
tree = ET.fromstring(output)
print("Retrieving:", url)
suma = 0
count =0
leng= 0
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        #leng += len(comment.find('name').text)
        suma += int(comment.find('count').text)
        count=count+1

print('Retrieved',len(output),'characteres')
print('Count:', count)
print('Sum:', suma)