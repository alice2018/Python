# -*- coding: UTF-8 -*-

#左上三角格式输出九九乘法表
for i in range(1,10):
    for j in range(i,10):
        print("%d*%d=%2d" %(i,j,i*j)),    
    print


#---------------------------------------



# -*- coding: UTF-8 -*-
#右下三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,10-i):
        print ("      "),
        
    for j in range(1,i+1):
        print("%d*%d=%2d" % (i,j,i*j)),
    print





