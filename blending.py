from PIL import Image
import numpy as np

w, h = 512, 512
data1 = np.zeros((h, w, 3), dtype=np.uint8)
data2= np.ones((h,w,3),dtype=np.uint8)*125

data1[250:262,250:262] = [255, 255, 255] # white in center

img1 = Image.fromarray(data1, 'RGB')
img2 = Image.fromarray(data2, 'RGB')
img1.save('data1.png')
img2.save('data2.png')
img1.show()
img2.show()

def morphing(data1,data2):
    t=1
    cnt=0
    while t>0:
        cnt+=1
        if cnt==11:
            t=0
        M1=data1*t+data2*(1-t)
        if t<0:
            break
        print(t)
        print(M1[300][300][0])
        im = Image.fromarray((M1).astype(np.uint8))

        name="m"+str(cnt)+".jpg"
        print(t,cnt)
        print(name)
        im.save(name)
        t -= 0.1

morphing(data1,data2)