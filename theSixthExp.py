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

params = [cv2.IMWRITE_JPEG_QUALITY, 50]  # ratio:0~100
#'.jpg'表示把当前图片按照jpg格式编码

msg = cv2.imencode(".jpg", img, params)[1]
msg = (np.array(msg)).tobytes()
print("msg:", len(msg))


img = cv2.imdecode(np.frombuffer(msg, np.uint8), cv2.IMREAD_COLOR)
print(img.shape, type(img))

