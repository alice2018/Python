# -*- coding: cp936 -*-


class classA(object): 
    m_file = "A and B are using that file"
    def openFile(self,_close,_AOpen,_BOpen,_bothOpen):
        self._close=_close
        self._AOpen=_AOpen
        self._BOpen=_BOpen
        self._bothOpen=_bothOpen
        if (classA.m_file==_close):
            classA.m_file=_AOpen
        elif (classA.m_file==_BOpen):
            classA.m_file=_bothOpen
    def closeFile(self,_close,_AOpen,_BOpen,_bothOpen):
        self._close=_close
        self._AOpen=_AOpen
        self._BOpen=_BOpen
        self._bothOpen=_bothOpen
        if (classA.m_file==_AOpen):
            classA.m_file=_close
        elif (classA.m_file==_bothOpen):
            classA.m_file=_BOpen
    def test(self,_close):
        self._close=_close
        if (classA.m_file==_close):
            return False
        else:
            return True       
class classB:
    def openFile(self):
        print classA.m_file
    def closeFile(self):
        if (classA.m_file==_BOpen):
            classA.m_file=_close
        elif (classA.m_file==_bothOpen):
            classA.m_file=_AOpen
    def test(self,_close):
        self._close=_close
        if (classA.m_file==_close):
            return False
        else:
            return True        
    
a = classA()
b = classB()
b.openFile()
if(a.test(1)):
    print "File still be used"
else:
    print "File not be used"
if(b.test(1)):
    print "File not be used"
else:
    print "File still be used"
