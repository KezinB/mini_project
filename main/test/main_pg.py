import cv2
import numpy as np
import ultrasonic_sensor as uls
import thres_img as thres
import wrap_img as wapt
import histogram as hist

import time

curveList = []
avgVal=10

def getcurve(img,display=1):
    
    imgResult = cv2.resize(img,(480,240))
    
    #step1
    imgthres = thres.thresholding(img)
    
    #step2
    hT, wT ,c = img.shape
    points = wapt.valTrackbars()
    imgWarp = wapt.warpImg(imgthres,points,wT,hT)
    imgWarpPoints = wapt.drawPoints(imgcopy,points)
    
    #step 3 
    middlePoint,imgHist = hist.getHistogram(imgWarp,display=True)
    curveAveragePoint, imgHist = hist.getHistogram(imgWarp, display=True, minPer=0.9)
    curveRaw = curveAveragePoint - middlePoint
    #print(curveRaw)
    
    #step4
    curveList.append(curveRaw)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))
    #print(curve)
    
    curve = curve/100
      
    #obstacle detection
    obs_dist = uls.distance()
    if (obs_dist < 20):
        print("Obstacle on the path ")
    else:
        print("clear path")
        
    #cv2.imshow("Camera",img)
    cv2.imshow("threshold" ,imgthres)
    #cv2.imshow("wrap",imgWarp)
    #cv2.imshow("pts" ,imgWarpPoints)
    cv2.imshow("histogram",imgHist)
    return curve
def motordriver(val):
    pass


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    wapt.initializeTrackbars()
    frameCounter = 0
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        imgcopy = cv2.resize(img,(640,480))
        curve = getcurve(img)
        print("curve value = ",curve)
        if (curve < -0.5):
            curve = -1
            #print("-1")
        elif (curve > 0.5):
            curve = 1
            #print("1")
        else:
            curve = 10
            
        print("optimised curve value = ",curve)
        cv2.waitKey(1)
