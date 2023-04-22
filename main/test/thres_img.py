# step 1

import cv2
import numpy as np

def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([0, 0, 90])
    upperWhite = np.array([179, 255, 255])
    maskedWhite= cv2.inRange(hsv,lowerWhite,upperWhite)
    return maskedWhite

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        img1 = thresholding(img)
        #getLaneCurve(img)
        cv2.imshow("Camera",img)
        cv2.imshow("threshold",img1)
        cv2.waitKey(1)
