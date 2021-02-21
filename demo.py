import cv2
import numpy as np

img = cv2.imread("roi.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (720,500))

ball = img[430:420, 510:500]
img[510:92, 590:12] = ball

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.distroyAllWindows()
