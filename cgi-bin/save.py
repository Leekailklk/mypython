# !C:\ProgramData\Anaconda3\python.exe
# -*- coding:gbk -*-
print('Content-type: text/html\n')
import cgitb;

cgitb.enable()
import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()
import cgi, sys

form = cgi.FieldStorage()
sender = form.getvalue('sender')
subject = form.getvalue('subject')
text = form.getvalue('text')
reply_to = form.getvalue('reply_to')
if not (sender and subject and text):
    print('Please supply sender, subject, and text')
    sys.exit()
if reply_to is not None:
    query = ("""INSERT INTO messages(reply_to, sender, subject, text)    
                   VALUES( ?, ?, ?, ?)""",
             [int(reply_to), sender, subject, text])
else:
    query = ("""INSERT INTO messages(sender, subject, text)    
                     VALUES(?, ?, ?)""",
             [sender, subject, text])
curs.execute(*query)
conn.commit()
print(""" 
<html> 
    <head>   
         <title>Message Saved</title> 
    </head> <body>  
    <h1>Message Saved</h1>  <hr />  
    <a href='main.py'>Back to the main page</a> 
    </body> </html> """)
