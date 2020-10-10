import cv2
import numpy as np

img = cv2.imread(r"EBUZER\OPENCV\resimler\duzeltilmis.jpg")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

dus_kir = np.array([30,150,50])
yuk_kir =np.array([255,255,180])

mask= cv2.inRange(hsv,dus_kir,yuk_kir)
res = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("frame",img)
cv2.imshow("frame2",mask)
cv2.imshow("frame3",res)
cv2.imshow("frame4",hsv)


cv2.waitKey(0)   
cv2.destroyAllWindows()