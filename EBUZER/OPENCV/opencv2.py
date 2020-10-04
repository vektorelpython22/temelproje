import cv2
import numpy as np
img = cv2.imread(r"EBUZER\OPENCV\resimler\baska.png",cv2.IMREAD_UNCHANGED)
imgGri = cv2.imread(r"EBUZER\OPENCV\resimler\baska.png",cv2.IMREAD_GRAYSCALE)


buyuk_perc = 20
width = int(img.shape[1]*buyuk_perc/100)
height = int(img.shape[0]*buyuk_perc/100)
dim =(width,height)
resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

cv2.imshow("image",resized)
# cv2.imshow("imageGri",imgGri)
cv2.imwrite(r"EBUZER\OPENCV\resimler\duzeltilmis.jpg",resized)
cv2.imshow("image",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

