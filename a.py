import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread('img.png')
arr = img[:,:,2]

arra = np.asarray(arr)
histogram, bins = np.histogram(arr.ravel(), bins=256, range=[0, 256])
plt.plot(histogram)

