# -*- coding: cp936 -*-

x = int(raw_input('please input x:'))  
y = int(raw_input('please input y:'))
z = int(raw_input('please input z:'))
if (x==y and x==z):
    print "三数值相等"
elif(x!=y and x!=z and y!=z):
    print "皆不相等"
else:
    print "两值相等"
