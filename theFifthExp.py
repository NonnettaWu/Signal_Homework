#encoding:utf-8
from __future__ import division
 

 
import cv2
import json
import urllib
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
 
 
#编码操作
img=cv2.imread('Yzu.jpg')
print(img.shape)
#'.jpg'表示把当前图片按照jpg格式编码
imgEncodeJpg=cv2.imencode('.jpg',img)[1]
dataEncodeJpg=np.array(imgEncodeJpg)
strEncodeJpg=dataEncodeJpg.tostring()
print('strEncodeJpg_type: ', type(strEncodeJpg))

#数据存储
with open('encodeJpg.txt','wb') as f:
    f.write(strEncodeJpg)

#解码操作
with open('encodeJpg.txt','rb') as f:
    strEncodeJpg=f.read()

#jpg
imgArrayJpg=np.fromstring(strEncodeJpg,np.uint8)
imgDecodeJpg=cv2.imdecode(imgArrayJpg,cv2.IMREAD_COLOR)
print('imgDecodeJpg_shape: ', imgDecodeJpg.shape)

#可视化展示
plt.clf()
plt.figure(figsize=(10,6))
plt.subplot(121)
plt.imshow(img)
plt.title('original')
plt.subplot(122)
plt.imshow(imgDecodeJpg)
plt.title('jpg')

plt.show()


