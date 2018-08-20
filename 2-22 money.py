# -*- coding: UTF-8 -*-

c25=0
c10=0
c5=0
c1=0

while 1:
    value = int(raw_input("please input cents( < 100) :"))
    if value < 100:
        break
for i in range(1,value):
    i += 1
    if (value >= 25):
        value -= 25
        c25 += 1
    
for j  in range(1,value):
    j += 1
    if (value >= 10):
        value -= 10
        c10 += 1
        
for m  in range(1,value):
    m += 1
    if (value >= 5):
        value -= 5
        c5 += 1
        
for n  in range(1,value+1):
    n += 1
    if (value >= 1):
        value -= 1
        c1 += 1
        
print "25 cents :",c25
print "10 cents :",c10
print "5 cents :",c5
print "1 cents :",c1










