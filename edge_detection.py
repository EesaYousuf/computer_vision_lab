import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image in grayscale
img = cv2.imread('images/sample.jpg', cv2.IMREAD_GRAYSCALE)
# 1. Sobel Edge Detection
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
