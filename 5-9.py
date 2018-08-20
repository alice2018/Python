# -*- coding: cp936 -*-



class parity:
    def __init__(self):
        self.m_count = 0
    def put(self):
        self.m_count += 1
    def test(self):   
        if self.m_count%2 == 0:
            return "true"
        else:
            return "false"
        
A = parity()
B = parity()

A.put()
A.put()
A.put()

B.put()

if(A.test()=='true'):
    print "A has even items"
else:
    print "A has odd items"


    
    
