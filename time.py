# -*- coding: cp936 -*-

import datetime
i = datetime.datetime.now()
print ("��ǰ�����ں�ʱ���� %s" % i)
print ("ISO��ʽ�����ں�ʱ���� %s" % i.isoformat() )
print ("��ǰ������� %s" %i.year)
print ("��ǰ���·��� %s" %i.month)
print ("��ǰ��������  %s" %i.day)
print ("dd/mm/yyyy ��ʽ��  %s/%s/%s" % (i.day, i.month, i.year) )
print ("��ǰСʱ�� %s" %i.hour)
print ("��ǰ������ %s" %i.minute)
print ("��ǰ����  %s" %i.second)
