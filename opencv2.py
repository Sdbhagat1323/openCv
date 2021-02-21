import numpy as np
import cv2

cap = cv2.VideoCapture("Of Monsters and Men – Dirty Paws (The Secret Life of Walter Mitty).mp4")
 
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.resize(frame, (720, 500))
    gray2 = cv2.resize(gray, (720, 500))
    
    cv2.imshow('frame',frame2)
    cv2.imshow('gray', gray2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()