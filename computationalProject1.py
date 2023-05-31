# 1
# blending two images
# road and ball (any size)
# locate ball on road coordinates by interpolating
# blend two images by matrix operations

# 2
#finite difference formulas
# dy/dx = f(xi)' = f(Xi+1)-f(Xi-1)/2h
# d^2y/dx= dx^2= f(Xi+1)-2f(Xi)+f(Xi-1)/h^2
# d^4y/dx^4 = y(i-2)-4y(i-1)+6y(i)-4y(i+1)+y(i+2)/h^4


import detectEdge
import cv2
import numpy as np
from PIL import Image as im


# image as matrix
image = cv2.imread('frame100.png')
# convalution matrix
# mask for x-axis edges
Mask=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
image1=im.fromarray(detectEdge.Conv_matrix(image,Mask))
image1.save('edges.png')

# draw circle and save as image
#
#
#

# circle = np.zeros((1616, 424, 3), np.uint8)
#
# # Window name in which image is displayed
# window_name = 'Image'
#
# # Center coordinates
# center_coordinates = (220, 150)
#
# # Radius of circle
# radius = 100
#
# # Red color in BGR
# color = (255, 133, 233)
#
# # Line thickness of -1 px
# thickness = -1
#
# # Using cv2.circle() method
# # Draw a circle of red color of thickness -1 px
# im = cv2.circle(circle, center_coordinates, radius, color, thickness)
#
# # Displaying the image
# cv2.imshow(window_name, im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#

# draw rectangle

# def drawRedRectangle(i,j):
#     rectangle=np.ones((i,j,3),dtype=np.uint8)
#     rectangle[:,:]=[255,0,0]
#     image=im.fromarray(rectangle,'RGB')
#     image.save('rectangle.png')
#
# drawRedRectangle(200,200)



#  1
# !!!

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
    img1.save('data1.png')
    img1.show()
    return img1

rectangle=draw_rectangle(144,300,10,1616,424)

