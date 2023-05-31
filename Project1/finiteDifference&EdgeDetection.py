import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# 1.2 and 1.3 homeworks
# 1,2,4 finite difference formulas for partial derivatives with that order and output by kernel matrix convolution


I = cv2.imread('frame100.png', 0).astype(np.float64)


#-partial Derivative x- finite difference - for vertical edges
Kx = -1*np.array([[-1,0,1]])
Fx = ndimage.convolve(I, Kx)

# 2 finite difference - second order partial derivative - for x - vertical
Kx2 = -1*np.array([[-1,2,1]])
Fx2 = ndimage.convolve(I, Kx2)

# 4 finite difference - fourth order partial derivative - for x - veritcal
Kx4 = -1*np.array([[1,-4,6,-4,1]])
Fx4 = ndimage.convolve(I, Kx4)

#-Derivative y - finite difference  - for horizontal edges
Ky = -1*np.array([[-1],[0],[1]])
Fy = ndimage.convolve(I, Ky)

# 2 finite difference - second order partial derivative - for y - horizontal
Ky2 = -1*np.array([[1],[2],[1]])
Fy2 = ndimage.convolve(I, Ky2)

# 4 finite difference - fourth order partial derivative - for x- vertical
Ky4 = -1*np.array([[1],[-4],[6],[4],[1]])
Fy4 = ndimage.convolve(I, Ky4)

#-Gradient

#--Magnitute - vertical and horizontal lines
magnitude = np.sqrt(Fx**2 + Fy**2) # G
magnitude2= np.sqrt(Fy2**2+Fy2**2)
magnitude4 = np.sqrt(Fx4**2 + Fy4**2)


# #--Orientation
# phase = cv2.phase(Fx, Fy, angleInDegrees=True) #theta
# mask_phase = np.zeros((I.shape[0], I.shape[1],3), dtype=np.uint8)
#
# mask_phase[ (magnitude != 0) & (phase >= 0) & (phase <= 90)] = np.array([0, 0, 255]) #red
# mask_phase[ (magnitude != 0) &  (phase > 90) & (phase <= 180)] = np.array([0, 255, 255]) #yellow
# mask_phase[ (magnitude != 0) & (phase > 180) & (phase <= 270)] = np.array([0, 255, 0]) #green
# mask_phase[ (magnitude != 0) & (phase > 270) & (phase <= 360)] = np.array([255, 0, 0])  #blue

#-Save
#We take the abs value of Fx and Fy without considering the sign of derivative. This is important to show the edge in the image.
cv2.imwrite("FDx.png",np.abs(Fx))
cv2.imwrite("FD2x.png",np.abs(Fx2))
cv2.imwrite("FD4x.png",np.abs(Fx4))
cv2.imwrite("FDy.png",np.abs(Fy))
cv2.imwrite("FD2y.png",np.abs(Fy2))
cv2.imwrite("FD4y.png",np.abs(Fx4))
cv2.imwrite("Magnitude.png",magnitude)
cv2.imwrite("Magnitude2.png",magnitude2)
cv2.imwrite("Magnitude4.png",magnitude2)
# cv2.imwrite("Orientation.png",mask_phase)