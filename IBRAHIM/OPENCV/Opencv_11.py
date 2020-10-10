import cv2 


# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap = cv2.VideoCapture(r"IBRAHIM\OPENCV\people-walking.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow("deneme",fgmask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()