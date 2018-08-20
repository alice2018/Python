# -*- coding: cp936 -*-

import os 
import PyPDF2  
import PythonMagick
  
pdffilename = 'C:\\Users\\user\\Desktop\\fp\\1.pdf'
pdf_im = PyPDF2.PdfFileReader(pdffilename, "rb")  
  
npage = pdf_im.getNumPages()   
for p in range(npage):  
    im = PythonMagick.Image(pdffilename + '[' + str(p) +']')  
    im.density('1200')  
    output_jpg = pdffilename.replace(".pdf", ".jpg")
    im.write(output_jpg)

 



