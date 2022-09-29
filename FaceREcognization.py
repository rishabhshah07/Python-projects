import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret, frame = cap.read()

    #display the resulting frame
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

#everything done so relaese the capture
cap.release()
cv2.destroyAllWindows()