# -*- coding: cp936 -*-

import time

seconds = int(raw_input("�����뵹������( >0 ) :"))
while(seconds):
    seconds -= 1
    time.sleep(10)
    print seconds
print 'end'    
