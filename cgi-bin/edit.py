# !C:\ProgramData\Anaconda3\python.exe
# -*- coding:gbk -*-
print('Content-type: text/html\n')
import cgitb;

cgitb.enable()
import sqlite3

conn = sqlite3.connect('food.db')
curs = conn.cursor()
import cgi

form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')
print("""  
<html>   
      <head>     
            <title>Compose Message</title>   
      </head>   
      <body>  
            <h1>Compose Message</h1> 
            <form action='save.py' method='POST'>    
      """)
subject = ''
if reply_to is not None:
    print('<input type="hidden" name="reply_to" value="{}"/>'.format(reply_to))
    curs.execute('SELECT subject FROM messages WHERE id = %s'%reply_to)
    subject = curs.fetchone()[0]
    if not subject.startswith('Re: '):  subject = 'Re: ' + subject
print(
    """  
    <b>Subject:</b>
    <br />  
          <input type='text' size='40' name='subject' value='{}' />
    <br />  
    <b>Sender:</b>
    <br />  <input type='text' size='40' name='sender' />
    <br />  
    <b>Message:</b>
    <br />  
    <textarea name='text' cols='40' rows='20'></textarea>
    <br />  
    <input type='submit' value='Save'/>  
    </form><hr />  
    <a href='main.py'>Back to the main page</a>'   
    </body> </html> 
    """.format(subject))