import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
img = cv2.imread("swapnil.jpg", cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap= "gray", interpolation = "bicubic")
plt.xticks([]), plt.yticks([])
# DRAW LINE ON IMAGE.
plt.plot([200, 300, 400],[100, 200, 300], "c",linewidth=5)
plt.show()

'''
import cv2
cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
im = cv2.imread("swapnil.jpg")                        # Read image
imS = cv2.resize(im, (960, 540))                    # Resize image
cv2.imshow("output", imS)                            # Show image
cv2.waitKey(0)                
