import numpy as np
import cv2

img = cv2.imread("hand.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 400))

cv2.rectangle(img, (180, 80),(430, 320),(255, 255, 255), 5)
cv2.circle(img, (305, 200),100, (0, 0, 255), 5)

pts= np.array([[180, 80],[250, 200], [180, 200], [305, 200]], np.int32)
#pts = pts.reshape((-1, 1,2))
cv2.polylines(img,[pts],True, (0, 255, 255), 5)
#cv2.line(img, (0,0), (100, 100), (255, 255, 255), 15)

#Writing on image
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpEn CV..', (180, 80), font, 1,(255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.distroyAllWindows()