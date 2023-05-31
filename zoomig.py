import numpy
import numpy as np
from PIL import Image


w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[250:262,250:262] = [255, 255, 255] # white in center
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()

A=[[5,6],[7,8]]
print(A[:2][:2])
A1=[]
def column_zooming(K1,Matrix):
    new_matrix=[]
    for i in range(len(Matrix)):
        for j in range(K1):
            new_matrix.append(Matrix[i])
    return new_matrix
print(column_zooming(3,A))

# in row every i element must be copy k-times
# for loop ( every row)
# for loop ( in row copy and shifting)

def row_zooming(K2,Matrix):
    new_matrix = []
    for i in range(len(Matrix)):
        ls = []
        for j in Matrix[i]:
            for k in range(K2):
                ls.append(j)
        new_matrix.append(ls)
    return new_matrix
print(row_zooming(3,A))

def Zooming_K(Matrix,K):
    return column_zooming(K,row_zooming(K,Matrix))

print(len(Zooming_K((data[250:262,250:262]).tolist(),2)))

def Zooming_obj_InMatrix(Image,k,i1,i2,j1,j2):
    i11=i1-(i2-i1)*(k-1)/2
    print(i11)
    i22=i2+(i2-i1)*(k-1)/2
    print(i22)
    j11=j1-(j2-j1)*(k-1)/2
    print(j11)
    j22=j2+(j2-j1)*(k-1)/2
    print(j22)
    Matrix=(Image[i1:i2,j1:j2]).tolist()
    #Image[i11:i22,j11:j22]=Zooming_K(Matrix,k)
    return np.array(Zooming_K(Matrix,k),dtype=np.uint8)

i=Zooming_obj_InMatrix(data,16,250,262,250,262)
img = Image.fromarray(i, 'RGB')
img.save('zoom.png')
img.show()



# def zoom(i1,i2,j1,j2,k,array):
#     # i1-i2 is size of rows
#     for i
#     object=array[i1:i2,j1:j2]
