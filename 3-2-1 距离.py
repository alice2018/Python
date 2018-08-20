# -*- coding: cp936 -*-

import math

ax = int(raw_input('A点x座标 :'))  
ay = int(raw_input('A点y座标 :'))
bx = int(raw_input('B点x座标 :'))
by = int(raw_input('B点y座标 :'))

result = math.sqrt(pow(ax-bx,2)+pow(ay-by,2))

print "两点距离 :",result
