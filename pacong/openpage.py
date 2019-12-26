from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.ip138.com/post")
bsObj = BeautifulSoup(html)
print(bsObj)
images = bsObj.findAll("a",{"href":re.compile("\\[0-9]*")})
for image in images:
      print(image["href"])