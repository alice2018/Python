# -*- coding: cp936 -*-


class small_set:
    m_set = {}
    for i in range(0,31):
        i += 1
        m_set[i]=False
    def set(self,item):
        self.item = item
        if (item>=0 and item<31):
            small_set.m_set[item]=True
    def clear(self,item):
        self.item = item
        if (item>=0 and item<31):
            small_set.m_set[item]=False
    def test(self,item):
        self.item = item
        if (item>=0 and item<31):
            return small_set.m_set[item]
        
A = small_set()
A.set(1)
A.set(3)
A.set(5)
print "A set 1 3 5"
if(A.test(1)):
    print "1 being set"
else:
    print "1 being not set"
    
print "A clear 1"
A.clear(1)

if(A.test(1)):
    print "1 being set"
else:
    print "1 not set"
