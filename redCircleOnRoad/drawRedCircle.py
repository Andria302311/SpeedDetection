import numpy as np
from PIL import Image
import cv2
import math

def createMatrixBySize(w,h):
     matrix=np.ones((w, h, 3), dtype=np.uint8)
     return matrix

def drawCircleInImage(x0,y0,radius,image):
     for y in range(-radius,radius+1):
          x = int(math.sqrt(radius**2-y**2))
          print(x)
          x1=(-x+x0)
          x2=(x+x0)
          y=(y+y0)
          image[x0+x1:x0+x2,y0+y]=[255,0,0]
          print(x0+x1,x0+x2,y0+y)
     return image



image=cv2.imread('frame100.png')
Image.fromarray(drawCircleInImage(30,30,30,image),'RGB').save('red.png')
(Image.fromarray(createMatrixBySize(424,1616),'RGB')).save('B.png')
