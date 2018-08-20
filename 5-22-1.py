# -*- coding: cp936 -*-


class classA:
    myfile = "file"
    opencount = 0
    closecount = 0
    def __init__(self,aopen,aclose):
        self.aopen=aopen
        self.aclose=aclose
        
    def openfile(self):
        classA.opencount += self.aopen
        
    def closefile(self):
        classA.closecount += self.aclose
        
    def test(self):
        if (self.aopen < self.aclose):
            return False
        else:
            return True
        
class classB:
    def __init__(self,bopen,bclose):
        self.bopen=bopen
        self.bclose=bclose
        
    def openfile(self):
        classA.opencount += self.bopen
        
    def closefile(self):
        classA.closecount += self.bclose
        
    def test(self):
        if (self.bopen < self.bclose):
            return False
        else:
            return True        
    
a = classA(1,0)
b = classB(5,5)

a.openfile()
a.closefile()
a.test()
b.openfile()
b.closefile()
b.test()
print "�ĵ��򿪴��� ��",a.opencount
print "�ĵ��رմ��� ��",a.closecount 
if(a.opencount == a.closecount):
    print "File not be used"
else:
    print "File be used"





