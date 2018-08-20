#! -*-coding:utf-8 -*-

import openpyxl
import re
 
def Excelpide(file_dir):
 wb=openpyxl.load_workbook(file_dir)         #打开原有的excel表
 sheet=wb.get_sheet_by_name('Sheet1')
 tuple(sheet['A1':'C3'])
 
 wb.create_sheet('Sheet2')                 #新建一个表
 sheet2=wb.get_sheet_by_name('Sheet2')
 tuple(sheet2['A1':'C3'])
 
 L1=re.compile(r'\d\d/\d\d/\d\d\d\d')      #日期格式
 L2=re.compile(r'[a-zA-Z0-9_]+@[a-zA-Z0-9-]+.com')   #邮件格式
 l1=[]
 l2=[]
 for rows in sheet['A1':'C3']:           #提取日期和邮件数据
     for cell in rows:
         A=L1.search(cell.value)
         a=A.group()
         B=L2.search(cell.value)
         b=B.group()
 for rows in sheet2['A1':'A9']:         #把日期数据写入新表
    for cell in rows:
        cell.value=a
        print(cell.coordinate,cell.value)
 for rows in sheet2['B1':'B9']:        #把邮件数据写入新表      
    for cell in rows:
        cell.value=b
        print(cell.coordinate,cell.value)
 return wb
 
g=Excelpide('C:\\Users\\user\\Desktop\\111.xlsx')
g.save('C:\\Users\\user\\Desktop\\111.xlsx')    #保存</code>
