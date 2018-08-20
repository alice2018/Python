# -*- coding: cp936 -*-

class Point:
    x1=0,x2=0
    y1=0,y2=0
    def setX(self):
        self.x1=x1
        self.x2=x2
    def setY(self):
        self.y1=y1
        self.y2=y2
    def setXY(self,x1,y1):
        self.x1=x1
        self.y1=y1
p1=Point()
p2=Point()
p1.setXY(1,1)
print p1.x1


class Line:
    p1=Point(x1,y1)
    p2=Point(x2,y2)
    def __init__(self,solid,dashed,dotted,outline,thick,begin,end):
        self._solid=solid
        self._dashed=dashed
        self._dotted=dotted
        self._outline=outline
        self._thick=thick
        self._begin=begin
        self._end=end        
    def Line(self):
        self._begin = Line.p1
        self._end = Line.p2
        self._thick = 1
        self._outline = self._solid
    def Line(ln):
        self._begin = ln._begin
        self._end = ln._end
        self._thick = ln._thick
        self._outline = ln._outline
    def setBegin(pt):
        self._begin = pt
    def setEnd(pt):
        self._end = pt
    def setOutline(ol):
        self._outline = ol
    def setThick(thick):
        self._thick = thick
    def begin():
        return self._begin
    def end():
        return self._end
    def outline():
        return self._outline
    def thick():
        return self._thick

a = Line()

print a.Line
        
