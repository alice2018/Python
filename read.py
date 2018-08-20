#-*- coding:UTF-8 -*-

# 打开文件
fo = open("1.txt", "r")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行 %s" % (line)

line = fo.readline(5)
print "读取的字符串为: %s" % (line)

# 关闭文件
fo.close()

