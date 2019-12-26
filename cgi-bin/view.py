# !C:\ProgramData\Anaconda3\python.exe
# -*- coding:gbk -*-
print('Content-type: text/html\n')
import cgitb; cgitb.enable()
import sqlite3
conn = sqlite3.connect('food.db')
curs = conn.cursor()
import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')
print(""" 
<html>   
     <head>  
           <title>View Message</title> 
     </head>   
     <body>  
           <h1>View Message</h1>    
        """)
try: id = int(id)
except:
    print('Invalid message ID')
    sys.exit()
curs.execute('SELECT * FROM messages WHERE id =%s'%id)
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]
if not rows:
    print('Unknown message ID')
    sys.exit()
row = rows[0]
print("""  
     <p><b>Subject:</b> {}<br />  
     <b>Sender:</b> {}<br />  
     <pre>{}</pre>  </p>  
     <hr />  <a href='main.py'>Back to the main page</a>   
     | <a href="edit.py?reply_to={}">Reply</a>   
     </body> </html> 
     """.format(row['subject'],row['sender'],row['text'],row['id']))