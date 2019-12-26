# -*- coding:utf-8 -*-
import zipfile
zfile = zipfile.ZipFile("test.zip")
passFile=open('6000pwd.txt') #读取你设定的密码文件
for line in passFile.readlines():
   try:
       password = line.strip('\n')
       print("the password is {}".format(password))
       zfile.extractall(path='C:\\Users\\葡萄桑\\Desktop\\', members=zfile.namelist(), pwd=password.encode('utf-8'))
       #print("the password is {}".format(password))
       break
   except:
       print("wrong")
