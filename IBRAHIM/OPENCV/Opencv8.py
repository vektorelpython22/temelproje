import cv2
import numpy as np

img = cv2.imread(r"IBRAHIM\OPENCV\resimler\resim.jpg")
imgGri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
temp = cv2.imread(r"IBRAHIM\OPENCV\resimler\temp.jpg",0)
w,h = temp.shape[::-1]
sonuc = cv2.matchTemplate(imgGri,temp,cv2.TM_CCOEFF_NORMED)
esik = 0.75
loc = np.where(sonuc>=esik)
print(*loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)



cv2.imshow("frame",temp)

cv2.imshow("frame",img)
cv2.waitKey(0)   
cv2.destroyAllWindows()