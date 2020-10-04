import cv2
import numpy as np

img = cv2.imread(r"EBUZER\OPENCV\resim\baska.png",cv2.IMREAD_UNCHANGED)
print(img.shape)
resize_perc = 60
width = int(img.shape[1]*resize_perc/100)
height = int(img.shape[0]*resize_perc/100)
dim(width,height)
resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

cv2.imshow("resize",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()