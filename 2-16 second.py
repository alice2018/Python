# -*- coding: cp936 -*-

import time

seconds = int(raw_input("请输入倒数秒数( >0 ) :"))
while(seconds):
    seconds -= 1
    time.sleep(10)
    print seconds
print 'end'    
