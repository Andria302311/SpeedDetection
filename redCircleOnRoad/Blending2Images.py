from PIL import Image
import numpy as np

def blendingByCoordinates(data1,data2,x1,x2,y1,y2,counter):
    t=1
    cnt=0
    while t>0:
        cnt+=1
        if cnt==counter:
            t=0

        result=data1
        result[x1:x2,y1:y2]=data1[x1:x2,y1:y2]*t+data2[x1:x2,y1:y2]*(1-t)
        if t<0:
            break
        #print(t)
        #print(result[300][300][0])
        im = Image.fromarray((result).astype(np.uint8))

        name="Blender"+str(cnt)+".jpg"
        #print(t,cnt)
        #print(name)
        im.save(name)
        t -= 0.1