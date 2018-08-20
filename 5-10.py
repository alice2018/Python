# -*- coding: cp936 -*-


class check:
    m_sum = 0
    def add_item(self,amount):
        self.amount = amount
        check.m_sum += amount
    def total(self):   
        return check.m_sum
        
A = check()
A.add_item(10)
A.amount 
print "A sum =",A.total()
A.add_item(20)
print "A sum =",A.total()


    
