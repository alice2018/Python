# -*- coding: cp936 -*-


class Engine:
    def __init__(self,engine):
        self.engine=engine

class Wheels:
    def __init__(self,wheels):
        self.wheels=wheels

class GearBox:
    def __init__(self,gearBox):
        self.gearBox=gearBox
    
class car:
    def __init__(self,engine,wheels,gearBox):
        self.engine=Engine(engine)
        self.wheels=Wheels(wheels)
        self.gearBox=GearBox(gearBox)
        print "car:",self.engine.engine,self.wheels.wheels,self.gearBox.gearBox
        
a = car(1,4,1)
print a.wheels.wheels
        

