# -*- coding: cp936 -*-


import re

a = re.search('\d+','231422sadf')

print a.group(0)



#-------------------------

x = re.search('3', "3456")
y = re.search('3', "14789")

print x.group(0)
print y
