# -*- coding: UTF-8 -*-

i = 1
while i :
    j = 1
    while j:
        print j,"*",i,"=",i*j," ",
        if i == j :
            break

        j += 1
        if j >= 10:
            break
    
    print "\n"
    i += 1
    if i >= 10:
        break





#---------------------------------------



# -*- coding: UTF-8 -*-
#右下三角格式输出九九乘法表
for i in range(1,10):
    for k in range(1,i):
        print ("      "),
        
    for j in range(i,10):
        print("%d*%d=%2d" % (i,j,i*j)),
    print
