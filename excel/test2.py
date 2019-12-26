import xlrd,xlwt,xlutils
#打开文件，获取excel文件的workbook（工作簿）对象
workbook=xlrd.open_workbook("rb201911.xls")  #文件路径
'''对workbook对象进行操作'''

# 获取所有sheet的名字
names = workbook.sheet_names()
print(names)

# 通过sheet索引获得sheet对象
worksheet = workbook.sheet_by_index(0)
print(worksheet)  # <xlrd.sheet.Sheet object at 0x000001B98D99CFD0>


sheet0_name = workbook.sheet_names()[0]  # 通过sheet索引获取sheet名称
print(sheet0_name)  # 各省市

'''对sheet对象进行操作'''
name = worksheet.name  # 获取表的姓名
print(name)  # 各省市

nrows = worksheet.nrows  # 获取该表总行数
print(nrows)  # 32

ncols = worksheet.ncols  # 获取该表总列数
print(ncols)  # 13

for i in range(nrows):  # 循环打印每一行
    print(worksheet.row_values(i))  # 以列表形式读出，列表中的每一项是str类型


col_data = worksheet.col_values(0)  # 获取第一列的内容
print(col_data)


