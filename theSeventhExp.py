import cv2

img = cv2.imread('testImg.jpg')
cv2.imwrite("./ret_50.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 50])

img50 = cv2.imread('ret_50.jpg')
print('原图： ', img.shape)
print('压缩后： ', img50.shape)
cv2.imshow('img', img)
cv2.imshow('ret_50', img50)

cv2.waitKey(0)
cv2.destroyAllWindows()