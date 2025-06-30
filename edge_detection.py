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
# Display all results using matplotlib
titles = ['Original Image', 'Sobel X', 'Sobel Y', 'Sobel Combined', 'Laplacian', 'Canny']
images = [img, sobel_x, sobel_y, sobel_combined, laplacian, canny]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(np.abs(images[i]), cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()

