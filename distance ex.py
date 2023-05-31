

def distance(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[0])


def find_coordinates(x,y):
    list=[]
    for i in range(1,x):
        for j in range(1,y):
            if(distance((i,j),(0,0))==distance((0,0),(x,y))/2):
                if(distance((i,j),(x,y))==distance((0,0),(x,y))/2):
                    list.append((i,j))

    return list

print(find_coordinates(42,13))


