import numpy as np


###   1

# draw rectangle on same size image
def draw_rectangle(coord_x,coord_y,size,x,y):
    import numpy as np
    from PIL import Image
    # frame size
    w, h = x, y
    data1 = np.zeros((w, h, 3), dtype=np.uint8)
    # # road coordinates
    # j = 300
    # i = 144
    # # size of rectangle
    # s = 10
    data1[coord_x - size:coord_x + size, coord_y - size:coord_y + size] = [255, 0, 0]
    img1 = Image.fromarray(data1, 'RGB')
    img1.save('rectangle.png')
    img1.show()
    return data1

rectangle=draw_rectangle(144,300,10,424,1616)

# create black/white image and move rectangle by blending

from PIL import Image

black_image=np.ones((424,1616,3),dtype=np.uint8)*255

def morphing(data1,data2,x1,x2,y1,y2):
    t=1
    cnt=0
    while t>0:
        cnt+=1
        if cnt==11:
            t=0
        M1=data1
        M1[x1:x2,y1:y2]=data1[x1:x2,y1:y2]*t+data2[x1:x2,y1:y2]*(1-t)
        if t<0:
            break
        print(t)
        print(M1[300][300][0])
        im = Image.fromarray((M1).astype(np.uint8))

        name="circle"+str(cnt)+".jpg"
        print(t,cnt)
        print(name)
        im.save(name)
        t -= 0.1

#coordinates where i want to locate circle
x0,x1,y0,y1=134,154,290,310

morphing(black_image,rectangle,x0,x1,y0,y1)

# y= -x/2 + 350 line where moves circle
import cv2
from PIL import Image as im

cnt=20
i=40
x=x0
y=y0

image = cv2.imread('frame100.png')
image0=cv2.imread('frame100.png')
frame=100

while(cnt>0):

    x+=i
    if(x>420):
        print("vso")
        break
    if(y<0):
        break
    y=int(x*(1/2)+400)
    print(x,y)

    r=draw_rectangle(x , y, 10, 424, 1616)

    #str_frame='frame'+str(frame)+'.png'
    #print(str_frame)
    image0 = cv2.imread('frame100.png')
    image0[x-10:x+10, y-10:y+10] = r[x-10:x+10, y-10:y+10]
    image1 = im.fromarray(image0)
    str1='moving'+str(20-cnt)+'.png'
    image1.save(str1)
    image1.show()
    frame+=1
    cnt-=1

#create video
#create folder , throw pics in folder
import os

images = [img for img in os.listdir('moving_circle') if img.endswith(".png")]
frame = cv2.imread(os.path.join('moving_circle', images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter('video.avi', 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join('moving_circle', image)))

cv2.destroyAllWindows()
video.release()
