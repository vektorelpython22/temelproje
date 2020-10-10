import cv2

# cap = cv2.VideoCapture(r"IBRAHIM\OPENCV\people-walking.mp4")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fgbg = cv2.BackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
    
    fgmask = fgbg.apply(frame)
    cv2.imshow("frame",frame)
    cv2.imshow("frame2",fgmask)

    if cv2.waitKey(1) & 0xFF == ord("ç"):
        break

cap.release()
cv2.destroyAllWindows()