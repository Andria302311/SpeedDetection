import numpy as np
from PIL import Image

#frame size

w, h = 424, 1616
data1 = np.zeros((w,h, 3), dtype=np.uint8)

# road coordinates
j=300
i=144
#size of rectangle
s=10

data1[i-s:i+s,j-s:j+s]=[255,0,0]

img1 = Image.fromarray(data1, 'RGB')

img1.save('data1.png')

img1.show()