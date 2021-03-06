import cv2
import numpy as np

img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original',img)
cv2.imshow('Sobel horizontal', sobel_horizontal)
cv2.imshow('Sobel vertical', sobel_vertical)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('laplacian', laplacian)

canny = cv2.Canny(img, 50, 240)
cv2.imshow('canny', canny)
cv2.waitKey(0)
