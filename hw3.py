import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")



nodes_x=[0,1,4]
nodes_y=[1,2,2]

# n=int(input("take number of nodes:"))
#
# for i in range(0,n):
#     x=int(input("take x node point:"))
#     y=int(input("take y node point:"))
#     nodes_x.append(x)
#     nodes_y.append(y)
#
# print("nodes of interpolation:")
# print(nodes_x)
# print(nodes_y)


def vietaFormula(roots):
    # Declare an array for
    # polynomial coefficient.
    n=len(roots)
    coeff = [0] * (n + 1)

    # Set Highest Order
    # Coefficient as 1
    coeff[n] = 1
    for i in range(1, n + 1):
        for j in range(n - i - 1, n):
            coeff[j] += ((-1) * roots[i - 1] *
                         coeff[j + 1])


    return coeff

print(vietaFormula([0,1,2]))


def poly(i,nodes_x):

    denom=1
    x=nodes_x[i]
    nodes_x.remove(i)
    coeff=vietaFormula(nodes_x)

    for j in nodes_x:
        denom*=(x-i)

    coeff=list(map(lambda k: k/denom ,coeff))

    return coeff

print(poly(0,nodes_x))

x = [0, 2, 4]
y = [1, 2, 2]
print(poly(0,x))

# get the polynomial function
coeff=poly(0,nodes_x)

P = poly.Polynomial(coeff)
x_new = np.arange(-1.0, 3.1, 0.1)
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, P(x_new), "b", label = "P1")



plt.plot(x, np.ones(len(x)), "ko", x,np.zeros(len(x)), "ko")
plt.title("Lagrange Basis Polynomials")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()