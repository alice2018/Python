# -*- coding: cp936 -*-

  
x = int(raw_input('请输入笔数 :'))

print "请输入键值"
for i in range(0,x):
    i += 1
    print "第%d笔 :"%i,i
      
y = int(raw_input('欲搜寻之键值 :'))

if y in range(0, x):
    print "键值存在"
else:
    print "键值不存在"


