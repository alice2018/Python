# -*- coding: cp936 -*-

x = int(raw_input('please input x:'))  
y = int(raw_input('please input y:'))
z = int(raw_input('please input z:'))
if (x==y and x==z):
    print "����ֵ���"
elif(x!=y and x!=z and y!=z):
    print "�Բ����"
else:
    print "��ֵ���"
