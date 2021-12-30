# imports
sudo apt-get install libopencv-dev python-opencv
bash install-opencv.sh



# Python program to Edge detection
# using OpenCV in Python
# using Sobel edge detection
# and laplacian method

import cv2
import numpy as np

# Capture livestream video content from camera 0
cap = cv2.VideoCapture(0)

while(1):
    
    # Take each frame
    _, frame = cap.read()
    
    # Convert to HSV for simpler calculations
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # calculate of SobelX
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    
    # Calculation of SobelY
    sobely = cv2.Sobel(frame, csv2. CV_64F, 0, 1, ksize=5)
    
    # Calculation of Laplacian
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    csv2.imshow('soblex', sobelx)
    cv2.imshow('sobley', sobely)
    cv2.imshow('laplacian', laplacian)
    k = cv2.waitKey(5) & OxFF
    if k == 27:
        break
        
cv2.destroyAllWindows()
cap.release()

cv2.Sobel(original_image, ddepth, xorder, yorder, kernelsize)
cv2.Laplacian(frame, cv2.CV_64F)
    
    