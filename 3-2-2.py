# -*- coding: cp936 -*-

def dist(x1,x2,y1,y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print dist(-1, -2, 1, 2)
