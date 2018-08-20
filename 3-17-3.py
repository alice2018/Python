# -*- coding: cp936 -*-

a = 2 
b = 100 

E = []
for num in range(a,b+1):
   snum = int(num*0.5+1)
   for i in range(2,snum): 
      if num%i == 0: 
         break 
   else: 
      E.append(num)
print a,'到',b,'的质数有',E
print a,'到',b,'有',len(E),'个质数' 
