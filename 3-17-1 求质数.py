# -*- coding: cp936 -*-


x = int(input('请输入上限 :'))
m = []

#total = 0
for n in range(1,x+1):
    if n == 1:
        continue
    elif n == 2:
        m.append(2)
        #total += 1
    else:
        if 0 not in [n%i for i in range(2,n)]:
            m.append(n)
            #total += 1        
            
print "所有质数为 ：",m
#print "合计为 :",total
print "合计为 :",len(m)





        
