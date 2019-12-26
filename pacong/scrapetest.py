from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://github.com/Bytom/bytom")
bsObj = BeautifulSoup(html.read())
str1="ok!"+bsObj.head.prettify()+"ok"
print(str1
      )
