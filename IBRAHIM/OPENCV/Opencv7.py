import cv2
import numpy as np

img = cv2.imread(r"IBRAHIM\OPENCV\resimler\duzeltilmis.jpg")

kernel = np.ones((15,15),np.float32)/225

smooth = cv2.filter2D(img,-1,kernel)
blur = cv2.GaussianBlur(img,(15,15),0)
median = cv2.medianBlur(img,5)

cv2.imshow("frame",img)
cv2.imshow("frame2",smooth)
cv2.imshow("frame3",blur)
cv2.imshow("frame4",median)


cv2.waitKey(0)   
cv2.destroyAllWindows()