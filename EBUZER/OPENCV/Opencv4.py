import cv2

img = cv2.imread(r"EBUZER\OPENCV\resimler\duzeltilmis.jpg")
px = img[100:150,100:150]
print(px)
img [100:150,100:150] =[255,255,255]
    
cv2.line(img,(0,0),(150,150),(255,255,255),10)
cv2.rectangle(img,(0,0),(150,150),(255,120,120),2)
cv2.circle(img,(100,65),55,(0,255,0),2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Lorem Ipsum",(10,150),font,2,(255,0,0),5,cv2.LINE_AA)


cv2.imshow("frame",img)
cv2.waitKey(0)   
cv2.destroyAllWindows()