# -*- coding: cp936 -*-

import os 
import PyPDF2  
import PythonMagick
from PythonMagick import Image
  
path = 'C:\\Users\\user\\Desktop\\fp'


for pdf in [pdf_file for pdf_file in os.listdir(path) if pdf_file.endswith(".pdf")]:

    pdffilename = path + "\\" + pdf

        
    pdf_im = PyPDF2.PdfFileReader(pdffilename, "rb")
    npage = pdf_im.getNumPages()
            
    for p in range(npage):  
        im = PythonMagick.Image(pdffilename)  
        im.density('1200')  
        output_jpg = pdffilename.replace(".pdf", ".jpg")
        im.write(output_jpg)

