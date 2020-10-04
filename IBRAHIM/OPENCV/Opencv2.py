import cv2
import numpy as np

img = cv2.imread(r"IBRAHIM\OPENCV\resimler\baska.png",cv2.IMREAD_UNCHANGED)



buyuk_perc = 20
en = int(img.shape[1] * buyuk_perc/100)
boy = int(img.shape[0] * buyuk_perc/100)
boyut = (en,boy)

resized = cv2.resize(img,boyut,interpolation=cv2.INTER_AREA)


cv2.imwrite(r"IBRAHIM\OPENCV\resimler\duzeltilmis.jpg",resized)
cv2.imshow("image",resized)
# cv2.imshow("imageGri",imgGri)


cv2.waitKey(0)
cv2.destroyAllWindows()