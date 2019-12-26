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
        head =bsObj.head
        body = bsObj.body.table
        new_tag = bsObj.new_tag("td")
        new_tag.attrs = {"class": "content"}
        new_tag.string = "The original code is from https://github.com/bytom. I just fork them and get it by using python."
        # replace the paragraph using `replace_with` method
        body.find_all('td',class_='content',string='Failed to load latest commit information.')[0].replace_with(new_tag)
    except AttributeError as e:
        return None
    return head,body
head,body = getHtml("https://github.com/Leekailklk/bytom-1")
if body == None:
    print("myHtml could not be found")
else:
   file_content='<!DOCTYPE html>'+'\n<html lang="en">'+head.prettify()+body.prettify()+'\n</html>'
   saveHtml("Bytom",file_content)
   print("saveHtml ok")
