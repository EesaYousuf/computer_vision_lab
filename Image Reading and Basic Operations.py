import cv2
import numpy as np
import matplotlib.pyplot as 
# Load image
img = cv2.imread('sample.jpg')  # Provide your own path
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)