import cv2
import numpy as np
import thres_img as ths

def warpImg(img,points,w,h,inv = False):
    #initializeTrackbars()
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(w,h))
    return imgWarp
 
def nothing(a):
    pass
 
def initializeTrackbars(wT=680, hT=480):
    intialTracbarVals=[130,320,85,480]
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)
 
def valTrackbars(wT=680, hT=480):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    #print(points)
    return points
 
def drawPoints(img,points):
    for x in range(4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),15,(0,0,255),cv2.FILLED)
    return img


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    #intialTracbarVals = [110,320,50,480]
    initializeTrackbars()
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        img2 = ths.thresholding(img)
        #cv2.imshow("Camera",img)
        cv2.imshow("thresholding",img2)
        
        hT, wT, c = img.shape
        points = valTrackbars()
        imgWarp = warpImg(img2,points,wT,hT)
        imgWarpPoints = drawPoints(img,points)
        cv2.imshow("wrap",imgWarp)
        cv2.imshow("pts" ,imgWarpPoints)
        cv2.waitKey(1)