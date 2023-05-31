import cv2
import numpy
import numpy as np

A=np.array([[1,2,3,3,2,1],
           [1,1,1,1,1,1],
           [1,2,3,3,2,1],
           [2,2,2,2,2,2],
           [1,2,3,3,2,1],
           [3,3,3,3,3,3]])

Mask=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

print(A[:][:3])

def mult(a,b):
    c=0
    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            c+=a[i][j]*b[i][j]
    return c

def center_of_conv_1(matrix0,mask0):
    c = 0
    cnt1 = 0
    i = 0
    while (i < 3):
        j = 0
        cnt2 = 0
        if (cnt1 < 3):
            while (j < 3):
                if (cnt2 < 3):
                    # print(i)
                    # print(j)
                    c += A[i][j] * Mask[cnt1][cnt2]
                    cnt2 = cnt1 + 1
                    j = j + 1
                    # print("c:")
                    # print(c)
                else:
                    cnt2 = 0
                    continue
            cnt1 = cnt1 + 1
            i = i + 1
        else:
            cnt1 = 0
            continue
    return c

C=np.zeros((A.shape))
print(C)

def Conv_matrix(matrix,mask):
    c=np.zeros((matrix.shape))
    m=3
    for i in range(1,len(c)-1):
        n=3
        for j in range(1,len(c[i])-1):
            c[i][j]=mult(matrix[i-1:m,j-1:n],mask)
            print(matrix[i-1:m,j-1:n])
            n+=1
        m+=1
    return np.array(c,dtype=np.uint8)

print(Conv_matrix(A,Mask))

print(A[:3,1:4])

imag = cv2.imread('frame100.png')
print(imag)
x_filter=numpy.array([[0,0,0],[1,0,-1],[0,0,0]])
y_filter=numpy.array([[0,-1,0],[0,0,0],[0,1,0]])

import numpy as np
from PIL import Image as im

print(Conv_matrix(imag,Mask))
data=im.fromarray(Conv_matrix(imag,Mask))
data.save('my.png')






