# -*- coding: cp936 -*-

  
x = int(raw_input('��������� :'))

print "�������ֵ"
for i in range(0,x):
    i += 1
    print "��%d�� :"%i,i
      
y = int(raw_input('����Ѱ֮��ֵ :'))

if y in range(0, x):
    print "��ֵ����"
else:
    print "��ֵ������"


