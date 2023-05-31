import Blending2Images
import drawRedCircle
import cv2

data=cv2.imread('B.png')
data1=cv2.imread('frame100.png')
data2=drawRedCircle.drawCircleInImage(30,30,30,data)
Blending2Images.blendingByCoordinates(data1,data2,50,110,170,230,10)