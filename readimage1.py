import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("swapnil.jpg", -1)

plt.imshow(image, cmap= "gray", interpolation = "bicubic")
plt.show()