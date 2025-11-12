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

def gauss(f, a, b, n):
    data = {
        1: ([0.0], [2.0]),
        2: ([-0.5773502692, 0.5773502692], [1.0, 1.0]),
        3: ([0.0, -0.7745966692, 0.7745966692], [0.8888889, 0.5555556, 0.5555556]),
        4: ([-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116], [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451]),
    }
    x, w = data[n]
    total = 0
    for i in range(n):
        xi = 0.5 * (b - a) * x[i] + 0.5 * (a + b)
        total += w[i] * f(xi)
    return 0.5 * (b - a) * total