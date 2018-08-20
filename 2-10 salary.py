# -*- coding: cp936 -*-

hours = int(input("Please input hours( >0 ): "))
salary = float(input("Please input salary( >0 ): "))
if(hours*7L > 40L):
    weekSalary=40L*salary+(hours*7L-40L)*salary*1.5
else:
    weekSalary=hours*7L*salary
print "weekSalary :",weekSalary    
