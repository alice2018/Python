# -*- coding: cp936 -*-


key_list=[]  
value_list=[]  
mydisc = {'1':'11','2':'22','3':'33','4':'44','5':'55'}  
for key,value in mydisc.items():  
    key_list.append(key)  
    value_list.append(value)  
  
get_value = raw_input("������Ҫ���ֵ��")  
if get_value in value_list:  
    get_value_index = value_list.index(get_value)  
    print "Ҫ��ѯ��ֵ����Ӧ�ļ�Ϊ��%s" %key_list[get_value_index]  
else:  
    print "Ҫ��ѯ��ֵ%s������" %get_value  
