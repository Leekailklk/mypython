def text_create(name,msg):
    desktop_path='C://Users/葡萄桑/Desktop/'
    full_path=desktop_path+name+'.txt'
    file=open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('hello','hello world')