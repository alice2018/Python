# -*- coding: cp936 -*-

import time

import numpy as np
from PIL import ImageGrab

# 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
beg = time.time()
debug = False
for i in range(10):
    img = ImageGrab.grab(bbox=(100, 150, 500, 500))
    img.save('C:\\Users\\user\\Desktop\\img\\5.jpg')
    img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
        
end = time.time()
print(end - beg)
