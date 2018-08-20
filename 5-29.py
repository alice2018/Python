# -*- coding: cp936 -*-



class Parent(object):  
    def think(self):  
        print "The father thinking"  
class Child(Parent):  
    def think(self):  
        print "The son thinking"
        
father = Parent()  
son = Child()       
father.think()  
son.think()  









