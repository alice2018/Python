# -*- coding: cp936 -*-


class baba:

    def __init__(self):

       pass

    def funcbaba(self):

        print ("���ǰְ֣���׬Ǯ��" )

class mama:

    def __init__(self):
        pass   

    def funcmama(self):

        print ("�������裬�ܹ˼�" )


class me(baba , mama):    #�ְ֣����������

    def __init__(self):
        baba.__init__(self)       #�Ҽ̳��˰ְֵ��ŵ�
        mama.__init__(self)    #Ҳ�̳���������ŵ�
        
    def funcme(self):

        print ("����լ�У��Ȼ�׬Ǯ��Ҳ��˼ң��۹���������������" )

print("����˭��\n -------------")
DNA = me()
DNA.funcbaba()
DNA.funcmama()
DNA.funcme()
