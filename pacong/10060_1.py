# coding=utf-8
import urllib
import urllib2
import re

url = "http://tieba.baidu.com/p/2460150866"
request = urllib2.Request(url)
page = urllib2.urlopen(url)
html = page.read()
print(html)