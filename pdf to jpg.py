# -*- coding: cp936 -*-

import os
import PythonMagick
import ghostscript
from PythonMagick import Image

         
pdf_dir = 'C:\\Users\\user\\Desktop\\fp' 
bg_colour = "#ffffff"

for pdf in [pdf_file for pdf_file in os.listdir(pdf_dir) if pdf_file.endswith(".pdf")]:

    input_pdf = pdf_dir + "\\" + pdf
    img = PythonMagick.Image(input_pdf)
    img.density('300')


    size = "%sx%s" % (img.columns(), img.rows())

    output_img = Image(size,bg_colour)
    output_img.type = img.type
    output_img.composite(img,0,0,PythonMagick.CompositeOperator.SrcOverCompositeOp)
    output_img.resize(str(img.rows()))
    output_img.magick('JPG')
    output_img.quality(100)


    output_jpg = input_pdf.replace(".pdf", ".jpg")
    output_img.write(output_jpg)

print "finish"
