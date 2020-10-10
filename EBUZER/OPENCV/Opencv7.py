import cv2
import numpy as np

img = cv2.imread(r"EBUZER\OPENCV\resimler\duzeltilmis.jpg")


kernel = np.ones((15,15),np.float32)/255
smooth = cv2.filter2D(img, -1,kernel)
blur = cv2.GaussianBlur(img,(15,15),0)

cv2.imshow("frame",img)
cv2.imshow("smooth",smooth)
cv2.imshow("blur",blur)



cv2.waitKey(0)   
cv2.destroyAllWindows()