import numpy as np

def gauss(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x+1)*(b-a)/2 + a
    return (b-a)*np.sum(w*f(t))/2

f = lambda x: x**2

a = 0
b = 1
for n in range(1, 11):
    result = gauss(f, a, b, n)
    print (f"n={n}, hasil = {result}")