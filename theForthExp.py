#encoding:utf-8
import cv2 
import numpy as np 
from matplotlib import pyplot as plt
  
#读取图片
Input = cv2.imread('Yzu.jpg')

#图像缩放
Output = cv2.resize(Input, None, fx=0.2, fy=0.2)

Input = cv2.cvtColor(Input, cv2.COLOR_BGR2RGB)
Output = cv2.cvtColor(Output, cv2.COLOR_BGR2RGB)
#显示图像
plt.clf()
plt.figure(figsize=(10,6))
plt.subplot(121)
plt.imshow(Input)
plt.title('Input')
plt.subplot(122)
plt.imshow(Output)
plt.title('Output')

plt.show()
