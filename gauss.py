import numpy as np
import math
pi = math.pi

def gauss_1(a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x+1)*(b-a)/2 + a
    return (b-a)*np.sum(w*np.cos(t))/2

def gauss_2(a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x+1)*(b-a)/2 + a
    return (b-a)*np.sum(w*(t**2))/2