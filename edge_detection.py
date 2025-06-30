import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image in grayscale
img = cv2.imread('images/sample.jpg', cv2.IMREAD_GRAYSCALE)
# 1. Sobel Edge Detection
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
# 2. Laplacian Edge Detection
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# 3. Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

