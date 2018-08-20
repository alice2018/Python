# -*- coding: cp936 -*-

class Pigs:
    m_count = 0
    def add(self,value):
        self.value = value
        Pigs.m_count += value
    def count(self):
        return Pigs.m_count
class Dogs:
    m_count = 0
    def add(self,value):
        self.value = value
        Dogs.m_count += value
    def count(self):   
        return Dogs.m_count    
class Horse:
    m_count = 0
    def add(self,value):
        self.value = value
        Horse.m_count += value
    def count(self):    
        return Horse.m_count
    
def totalNumber():
    print "Animal number(Pigs+Dogs+Horses)=",Pigs.m_count+Dogs.m_count+Horse.m_count

A = Pigs()    
A.add(10)
A.add(10)
print "Pigs number=",A.count()
B = Dogs()    
B.add(5)
B.add(10)
print "Dogs number=",B.count()
C = Horse()    
C.add(1)
C.add(2)
print "Horse number=",C.count()
totalNumber()


