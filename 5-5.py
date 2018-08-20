# -*- coding: cp936 -*-

class personData:
    tel = property()
    address = property()
    id = property()
    def __init__(self,name,age,birthday,blood,tel,address,id):
        self.name=name
        self.age=age
        self.birthday=birthday
        self.blood=blood
        self.__tel= tel
        self.__address= address
        self.__id= id
    @tel.getter
    def tel(self):
        return self.__tel
    @tel.setter
    def tel(self,value):
        self.__tel = value
    @address.getter
    def address(self):
        return self.__address
    @address.setter
    def address(self,value):
        self.__address = value
    @id.getter
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value    
        
        
p = personData('CJCOOL',29,'1989-1-3','AB','0939074754','Tainan','F122009771')
print 'Name =',p.name
print 'Telephone =',p.tel
print 'Address =',p.address
print 'Id =',p.id
print 'Age =',p.age
