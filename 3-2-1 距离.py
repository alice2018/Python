# -*- coding: cp936 -*-

import math

ax = int(raw_input('A��x���� :'))  
ay = int(raw_input('A��y���� :'))
bx = int(raw_input('B��x���� :'))
by = int(raw_input('B��y���� :'))

result = math.sqrt(pow(ax-bx,2)+pow(ay-by,2))

print "������� :",result
