# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()
curs.execute('''
create table messages (    
id       integer primary key autoincrement,    
subject     text not null,    
sender      text not null,    
reply_to    int,    
text text   not null )
''')

conn.commit()
conn.close()