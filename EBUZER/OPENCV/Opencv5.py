import cv2

img = cv2.imread(r"EBUZER\OPENCV\resimler\bookpage.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold = cv2.threshold(gri,10,255,cv2.THRESH_BINARY)

th=cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    cv2.THRESH_BINARY,115,1)
cv2.imshow("örnek",threshold)
cv2.imshow("adaptive",th)


cv2.imshow("frame",img)
cv2.waitKey(0)   
cv2.destroyAllWindows()