import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    cv2.imshow("deneme",frame)

    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        break 

cap.release()
cv2.destroyAllWindows()