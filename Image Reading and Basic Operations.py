import cv2
import numpy as np
import matplotlib.pyplot as 
# Load image
img = cv2.imread('sample.jpg')  # Provide your own path
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Show original and grayscale
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray)
# Save the grayscale image
cv2.imwrite('gray_output.jpg', gray)

