# -*- coding: UTF-8 -*-

# 打开文件
fo = open("1.txt", "w")
print "name: ", fo.name
seq = ["W3Cschool教程 1\n", "W3Cschool教程 2\n","W3Cschool教程 3"]
fo.writelines( seq )

# 关闭文件
fo.close()
