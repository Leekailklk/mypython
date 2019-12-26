import sqlite3

from docx import Document  # 导入库

path = "C:\\PycharmProjects\\untitled\\4.4学生补录信息表20190918(3)(1)(1).docx"  # 文件路径
document = Document(path)  # 读入文件
tables = document.tables  # 获取文件中的表格集
table = tables[0]  # 获取文件中的第一个表格
conn = sqlite3.connect('food.db')
curs = conn.cursor()
# curs.execute(''' DROP TABLE  food ''')
curs.execute(''' 
 CREATE TABLE students ( 
name TEXT PRIMARY KEY, 
sex    TEXT, 
dad_name   TEXT, 
dad_id    TEXT, 
mam_name TEXT, 
mam_id  TEXT
) ''')
query = 'INSERT INTO students VALUES (?,?,?,?,?,?)'
for i in range(1, len(table.rows)):  # 从表格第一行开始循环读取表格数据
    result = []
    for j in range(0, 6):
        result.append(table.cell(i, j).text.strip('\n').replace(' ', ''))
    # cell(i,0)表示第(i+1)行第1列数据，以此类推
    print(result)
    curs.execute(query, result)
conn.commit()
conn.close()
