from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name.replace('/', '_') + ".html", "w") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(file_content)
def getHtml(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        head =str(bsObj.head)
        body=str(bsObj.find('div',id='quesdiv3394525'))
    except AttributeError as e:
        return None
    return head,body
head,body = getHtml("http://zujuan.xkw.com/3q3394525.html")
if body == None:
    print("myHtml could not be found")
else:
   file_content='<!DOCTYPE html>'+'\n<html lang="en">'+head+'<body>'+body+'\n</body>'+'\n</html>'
   saveHtml("ForWife",file_content)
   #print(str(body))
   print("saveHtml ok")
