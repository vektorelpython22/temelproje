import cv2


# cap = cv2.VideoCapture(r"IBRAHIM\OPENCV\people-walking.mp4")

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    try:
        cv2.imshow("frame",frame)
    except:
        break
    if cv2.waitKey(1) & 0xFF == ord("ç"):
        break

cap.release()
cv2.destroyAllWindows()