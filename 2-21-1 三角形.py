# -*- coding: UTF-8 -*-

x = int(raw_input("请输入列数 ："))
for i in range(0,x):
    for j in range(0,i+1):
        print "@",
        j += 1
    i += 1
    print " "
