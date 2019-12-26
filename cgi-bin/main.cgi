# !C:\ProgramData\Anaconda3\python.exe
# -*- coding:utf-8 -*-
print('Content-type: text/html\n')
import cgitb; cgitb.enable()
import sqlite3
conn = sqlite3.connect('food.db')
curs = conn.cursor()

print("""    
<html>    
      <head>    
            <title>The FooBar Bulletin Board</title>    
      </head>    
      <body>   
            <h1>The FooBar Bulletin Board</h1>   
        """)

curs.execute('SELECT * FROM messages')
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

toplevel = []
children = {}
for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:     toplevel.append(row)
    else:  children.setdefault(parent_id, []).append(row)
def eformat(row):
    print('<p><a href="view.py?id={}">{}</a></p>'.format(row['id'],row['subject']))
    #print('{subject}{id}'.format(row))

    try:
        kids = children[row['id']]
    except KeyError: pass
    else:
        print('<blockquote>')
        for kid in kids:   eformat(kid)
        print('</blockquote>')
    print('<p>')
for row in toplevel:    eformat(row)
print("""
     </p>  <hr />  <p><a href="edit.py">Post message</a></p>
</body> </html> """)
