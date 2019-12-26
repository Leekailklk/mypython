# -*- coding:utf-8 -*-
import zipfile


#创建一个zip文件对象，压缩是需要把mode改为‘w’
zfile=zipfile.ZipFile("test.zip","w")
#将文件写入zip文件中，即将文件压缩
zfile.write(r"ziptest.py")
#将zip文件对象关闭
zfile.close()