# -*- coding: cp936 -*-

import os
path='C:\\Users\\user\\Desktop\\2017-9-28\\'
count=0

for filename in os.listdir(path):
    print filename
    
for root,dirs,files in os.walk(path):    
      for each in files:
             count += 1  
             print count        
    
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        
        fileName = path + file        
        os.startfile( fileName , "print")

print "End"
