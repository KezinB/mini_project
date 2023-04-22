import cv2
import numpy as np
import thres_img as thres
#import utlis
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        #getLaneCurve(img)
        img2 = thres.thresholding(img)
        cv2.imshow("Camera",img)
        #cv2.imshow("thr" ,img2)
        cv2.waitKey(1)