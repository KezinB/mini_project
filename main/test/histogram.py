import cv2
import numpy as np
import thres_img as thres
import wrap_img as wapt

def getHistogram(img,display=False,minPer = 0.1,region= 4):
    histValues = np.sum(img, axis=0)#getting histogram values
    
    maxValue = np.max(histValues) #getting maximum histogram values
    minValue = minPer*maxValue #getting minimum histogram values
    
    #print(minValue)
    
    indexArray = np.where(histValues >= minValue) #index array
    basePoint = int(np.average(indexArray)) #base point in the array
    
    #print(basePoint)
    if display:
        imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
        for x,intensity in enumerate(histValues):
            cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(255,0,255),1)
            cv2.circle(imgHist,(basePoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
        return basePoint,imgHist
 
    return basePoint
 

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    wapt.initializeTrackbars()
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE0
        imgthres = thres.thresholding(img)
        hT, wT ,c = img.shape
        points = wapt.valTrackbars()
        imgWarp = wapt.warpImg(imgthres,points,wT,hT)
        #getHistogram(imgWarp)
        middlePoint,imgHist = getHistogram(imgWarp,display=True)
        #cv2.imshow("Camera",img)
        cv2.imshow("threshold",imgthres)
        cv2.imshow("histogram",imgHist)
        cv2.imshow("wraped",imgWarp)
        #cv2.imshow("histogram",img2)
        cv2.waitKey(1)