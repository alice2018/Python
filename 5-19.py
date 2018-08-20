# -*- coding: cp936 -*-


class Histogram:
    form = list(range(11))
    def __init__(self,baseNumber,formNumber,formRange):
        self._baseNumber = baseNumber
        self._formNumber = formNumber
        self._formRange = formRange
    def draw(self):
        print "画出直方圆"
        for i in range(0,self._formNumber):
            print "第%d组 [%d-%d] :"%(i+1,self._baseNumber+i*self._formRange,self._baseNumber+(i+1)*self._formRange),
            i += 1
            for j in range(0,Histogram.form[i]-4):
                j += 1
                print "*",
            print " " 
    def insert(self,data):
        self.data = data
        for i in range(0,self._formNumber):
            i += 1
            if(data >= self._baseNumber+i*self._formRange and data < self._baseNumber+(i+1)*self._formRange):
                Histogram.form[i] += 1
                return True
        return False
    def remove(self,data):
        self.data = data
        for i in range(0,self._formNumber):
            i += 1
            if(data >= self._baseNumber+i*self._formRange and data < self._baseNumber+(i+1)*self._formRange):
                if(Histogram.form):
                   Histogram. form[i] -= 1
                else:
                    return False
                return True
        return False

A = Histogram(0,10,5)
A.insert(6)
A.insert(7)
A.insert(8)
A.insert(9)
A.insert(11)
A.insert(12)
A.insert(13)
A.insert(14)
A.remove(51)
A.remove(52)
A.remove(53)
A.remove(54)
A.remove(54)
A.remove(46)
A.remove(47)
A.remove(48)
A.remove(49)
A.remove(53)
A.remove(41)
A.remove(42)
A.remove(43)
A.remove(44)
A.remove(36)
A.remove(37)
A.remove(31)
A.insert(26)
A.draw()
        
