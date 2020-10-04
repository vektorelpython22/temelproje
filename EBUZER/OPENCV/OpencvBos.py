import cv2

img = cv2.imread(r"IBRAHIM\OPENCV\resimler\duzeltilmis.jpg")

cv2.imshow("frame",img)
cv2.waitKey(0)   
cv2.destroyAllWindows()