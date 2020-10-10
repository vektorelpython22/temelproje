import cv2
import numpy as np

# cap = cv2.VideoCapture(r"IBRAHIM\OPENCV\people-walking.mp4")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    try:
        if cv2.waitKey(0) & 0xFF == ord("t"):
            cv2.imwrite(r"IBRAHIM\OPENCV\resimler\kirmizi.jpg",frame) 
        cv2.imshow("frame",frame)
            # //TODO templata matching yapılacak
    except Exception as hata:
        print(hata)
    if cv2.waitKey(1) & 0xFF == ord("ç"):
        break

cap.release()
cv2.destroyAllWindows()