# -*- coding: cp936 -*- 


x = {}
y = x
x['key']='value'
print y
x.clear()
print y




d = {}
d['name']='alice'
d['age']=23
print d 
c = d.clear()
print d 
print c 
