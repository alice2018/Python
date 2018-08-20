# -*- coding: cp936 -*-


class Tester :  
    m_var = 0  
    print "Object A, m_var=%d"%m_var
    print "Object B, m_var=%d"%m_var
    def __init__(self):    
        Tester.m_var += 1
        print "Object A call Adder Function once"
    def adder(self):
        Tester.m_var += 1
        print "Object B call Adder Function twice"
        print "Object B, m_var=%d"%Tester.m_var


m_var = Tester() 
print "Object A, m_var=%d"%Tester.m_var  
m_var.adder()
        

        
  
