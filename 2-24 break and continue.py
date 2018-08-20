# -*- coding: UTF-8 -*-

print "continue test"
for i in range(1,4):
    i += 1
    print "1"
    if(i < 3):
        continue
    print "2"

print "break test"  
for i in range(1,4):
    i += 1
    print "1"
    if(i < 3):
        break
    print "2"
   
