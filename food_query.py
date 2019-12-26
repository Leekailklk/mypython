# -*- coding:utf-8 -*-
import sqlite3, sys
conn = sqlite3.connect('food.db')
curs = conn.cursor()
#query = 'SELECT * FROM food WHERE ' + sys.argv[1]
query = 'SELECT * FROM food WHERE ' + "kcal <= 100 AND fiber >= 10 ORDER BY sugar"
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print(pair,end=",")
        #print('{}: {}'.format(*pair))
    print("")
print()
