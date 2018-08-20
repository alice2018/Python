# -*- coding: cp936 -*-

class classA:
    aopencount = 0
    aclosecount = 0
    bopencount = 0
    bclosecount = 0
    def openfile(self):
        classA.aopencount += 1
        
    def closefile(self):
        classA.aclosecount += 1
        
    def test(self):
        if (classA.aopencount<0):
            return False
        else:
            return True
        
class classB:
    def openfile(self):
        classA.bopencount += 1
        
    def closefile(self):
        classA.bclosecount += 1
            
    def test(self):
        if (classA.bopencount<0):
            return False
        else:
            return True        
    
a = classA()
b = classB()

a.openfile()
a.openfile()
a.openfile()
print "a 打开%d次"%a.aopencount
b.openfile()
print "b 打开%d次"%a.bopencount
a.closefile()
a.closefile()
print "a 关闭%d次"%a.aclosecount
b.closefile()
print "b 关闭%d次"%a.bclosecount
a.test()
b.test()
if(a.aopencount + a.aclosecount == a.bopencount + a.bclosecount):
    print "File not be used"
else:
    print "File be used"
