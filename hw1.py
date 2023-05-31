import cv2
import numpy
import numpy as np

#1
orig = cv2.imread('nasa.jpg')
cv2.imshow('Original', orig)
gsi = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gsi)

#2-3

image = cv2.imread('nasa.jpg')

# Print error message if image is null
if image is None:
    print('Could not read image')

# Apply identity kernel
kernel1=numpy.array([[0,0,0],[1,0,-1],[0,0,0]])
kernel2=numpy.array([[0,-1,0],[0,0,0],[0,1,0]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
identity1= cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image)
cv2.imshow('Identity', identity)
cv2.imshow('Identity2',identity1)

cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()

# Apply blurring kernel
kernel2 = np.ones((5, 5), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

cv2.imshow('Original', image)
cv2.imshow('Kernel Blur', img)

cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img)
cv2.destroyAllWindows()



#4
import cv2
import numpy as np
import matplotlib.pyplot as plot
image = cv2.imread("nasa.jpg",0)

# Below code convert image gradient in both x and y direction
lap = cv2.Laplacian(image,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

# Below code convert image gradient in x direction
sobelx= cv2.Sobel(image,0, dx=1,dy=0)
sobelx= np.uint8(np.absolute(sobelx))

# Below code convert image gradient in y direction
sobely= cv2.Sobel(image,0, dx=0,dy=1)
sobely = np.uint8(np.absolute(sobely))

results = [lap,sobelx,sobely]
images =["Gradient Image","Gradient In X direction","Gradient In Y direction"]
for i in range(3):
    plot.title(results[i])
    plot.subplot(1,3,i+1)
    plot.imshow(results[i],"plasma")
    plot.xticks([])
    plot.yticks([])

plot.show()