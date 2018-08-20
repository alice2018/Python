# -*- coding: cp936 -*-

import os
import time

NUM=0
while 1:
    wPath="e:/%s.txt"%NUM
    if os.path.isfile(wPath):
        NUM+=1
        continue
    else:
        with open(wPath,"w") as fw:
            fw.write(wPath)
    time.sleep(10)
