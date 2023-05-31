import numpy as np
import numpy
import math

x = np.random.randint(1, 1000, 3)
print(x)

norm1 = sum(x)
norm01=np.linalg.norm(x,1)
norm2 = round(np.sqrt(sum(x ** 2)))
norm02=np.linalg.norm(x,2)

print("norm1=" + str(norm1)+" compare to "+str(norm01))

print("norm2=" + str(norm2)+" compare to "+str(norm02))

def p_norm(v,p):
    return np.sum(np.abs(v) ** p) ** (1. / p)

norm_p=p_norm(x,5)
norm_p1=np.linalg.norm(x, 5)
print("norm_p="+str(norm_p)+" compare to "+str(norm_p1))

def infinity_norm(v):
    max=0
    for i in v:
        if(i>max):
            max=i
    return max
print("vector infinity norm")
print(infinity_norm(x))

# def p_root(n,n1,p,acc):
#     if(n>4):
#         n0=round(n/p)
#         print(n0)
#         if(n0**p>n1):
#            return p_root(n0,n1,p,n)
#         else:
#             return (n,acc)
#     else:
#         return (1,2)
# print(p_root(1024,1024,10,0))

# n=1024
# n0=1024
# p=10
#
# def condition(n0,p,n):
#     diff=0
#     for i in range(2,p):
#         diff=n-n0**i
#         if(diff>0):
#             continue
#         else:
#             if(abs(diff)>n-n0**(i-1)):
#                 return (diff,i)
#             else:
#                 return (n-n0**(i-1),i-1)

def matrix_norm1(M):
    max=0
    for i in range(0,len(M)):
        if(sum(M[i])>max):
            max=sum(M[i])
    return max

def matrix_infinity(M):
    res = list(map(sum, zip(*M)))
    return max(res)

M= [[3, 9, 7], [1, 3, 5], [9, 3, 2]]

print("matrix norm1")
print(matrix_norm1(M))
print("matrix infinity norm")
print(matrix_infinity(M))

def frobenius_norm(M):
    sumSq = 0
    for i in range(0,len(M)):
        for j in M[i]:
            sumSq+=j**2

    return round(np.sqrt(sumSq))
print("frobenius:")
print(frobenius_norm(M))