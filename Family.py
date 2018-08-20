# -*- coding: cp936 -*-


class baba:

    def __init__(self):

       pass

    def funcbaba(self):

        print ("我是爸爸，会赚钱！" )

class mama:

    def __init__(self):
        pass   

    def funcmama(self):

        print ("我是妈妈，很顾家" )


class me(baba , mama):    #爸爸，妈妈在哪里？

    def __init__(self):
        baba.__init__(self)       #我继承了爸爸的优点
        mama.__init__(self)    #也继承了妈妈的优点
        
    def funcme(self):

        print ("我是宅男，既会赚钱，也会顾家，哇哈哈哈哈！！！！" )

print("我是谁？\n -------------")
DNA = me()
DNA.funcbaba()
DNA.funcmama()
DNA.funcme()
