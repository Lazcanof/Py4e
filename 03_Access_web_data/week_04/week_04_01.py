# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write
#  a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will
#  use urllib to read the HTML from the data files below, and parse the data, extracting numbers
#  and compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you 
# the sum for your testing and the other is the actual data you need to process for the assignment.

    # Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
    # Actual data: http://py4e-data.dr-chuck.net/comments_691289.html (Sum ends with 46)


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
suma=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    suma=suma+int(tag.contents[0])
print('la suma de los comentarios es:',suma)