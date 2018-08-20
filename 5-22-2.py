# -*- coding: cp936 -*-


class classA:
    myfile = "file"
    opencount = 0
    closecount = 0
    def openfile(self,aopen):
        self.aopen = aopen
        classA.opencount += self.aopen
        
    def closefile(self,aclose):
        self.aclose = aclose
        classA.closecount += self.aclose
        
    def test(self):
        if (self.aopen < self.aclose):
            return False
        else:
            return True
        
class classB:
    def openfile(self,bopen):
        self.bopen = bopen
        classA.opencount += self.bopen
        
    def closefile(self,bclose):
        self.bclose = bclose
        classA.closecount += self.bclose
        
    def test(self):
        if (self.bopen < self.bclose):
            return False
        else:
            return True        
    
a = classA()
b = classB()

a.openfile(1)
a.closefile(0)
a.test()
b.openfile(5)
b.closefile(3)
b.test()
print "�ĵ��򿪴��� ��",a.opencount
print "�ĵ��رմ��� ��",a.closecount 
if(a.opencount == a.closecount):
    print "File not be used"
else:
    print "File be used"
