# -*- coding: cp936 -*-

import time

import numpy as np
from PIL import ImageGrab

# ÿץȡһ����Ļ��Ҫ��ʱ��ԼΪ1s,���ͼ��ߴ�СһЩЧ�ʾͻ��һЩ
beg = time.time()
debug = False
for i in range(10):
    img = ImageGrab.grab(bbox=(100, 150, 500, 500))
    img.save('C:\\Users\\user\\Desktop\\img\\5.jpg')
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
        
end = time.time()
print(end - beg)
