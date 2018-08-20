# -*- coding: cp936 -*-

import os  
import ghostscript  
from PyPDF2 import PdfFileReader, PdfFileWriter  
from tempfile import NamedTemporaryFile  
from PythonMagick import Image  
  
  
reader = PdfFileReader(open('C:\\Users\\user\\Desktop\\fp\\1.pdf', "rb"))  
for page_num in xrange(reader.getNumPages()):  
    writer = PdfFileWriter()  
    writer.addPage(reader.getPage(page_num))  
    temp = NamedTemporaryFile(prefix=str(page_num), suffix=".pdf", delete=False)  
  
    writer.write(temp)  
  
    print temp.name  
  
    tempname = temp.name  
    temp.close()  
      
  
    im = Image(tempname)  
    im.density("3000") 
    #im.read(tempname)  
    im.write("some_%d.jpg" % (page_num))  
      
    os.remove(tempname)

reader.close()
    
