# -*- coding: cp936 -*-


key_list=[]  
value_list=[]  
mydisc = {'1':'11','2':'22','3':'33','4':'44','5':'55'}  
for key,value in mydisc.items():  
    key_list.append(key)  
    value_list.append(value)  
  
get_value = raw_input("请输入要查的值：")  
if get_value in value_list:  
    get_value_index = value_list.index(get_value)  
    print "要查询的值所对应的键为：%s" %key_list[get_value_index]  
else:  
    print "要查询的值%s不存在" %get_value  
