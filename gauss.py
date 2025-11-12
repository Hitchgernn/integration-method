import numpy as np
import math
pi = math.pi

def gauss_1(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x+1)*(b-a)/2 + a
    return (b-a)*np.sum(w*math.cos(t))/2

def gauss_2(_2f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    t = (x+1)*(b-a)/2 + a
    return (b-a)*np.sum(w*(t**2))/2