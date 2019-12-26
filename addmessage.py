# -*- coding:utf-8 -*-
#  addmessage.py
import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()
reply_to = input('Reply to: ')
subject = input('Subject: ')
sender = input('Sender: ')
text = input('Text: ')
if reply_to:   query = """  
  INSERT INTO messages(reply_to, sender, subject, text)    
  VALUES({}, '{}', '{}', '{}')""".format(reply_to, sender, subject, text)
else:  query = """  
  INSERT INTO messages(sender, subject, text)  
  VALUES('{}', '{}', '{}')""".format(sender, subject, text)
curs.execute(query)
conn.commit()