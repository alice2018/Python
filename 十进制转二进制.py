# -*- coding: cp936 -*-

import sys

denum = input("����ʮ������:")
print denum,"(10)",
binnum = []

while denum > 0:
    binnum.append(str(denum % 2)) 
    denum //= 2
print '= ',

while len(binnum)>0:
    sys.stdout.write(binnum.pop()) 
