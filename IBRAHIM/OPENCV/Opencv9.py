import cv2
import numpy as np
# cap = cv2.VideoCapture(r"IBRAHIM\OPENCV\people-walking.mp4")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    print(ret)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    dus_kir = np.array([30,150,50])
    yuk_kir = np.array([255,255,180])


    mask = cv2.inRange(hsv,dus_kir,yuk_kir)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("frame2",mask)
    cv2.imshow("frame",gray)
    if cv2.waitKey(1) & 0xFF == ord("ç"):
        break

cap.release()
cv2.destroyAllWindows()