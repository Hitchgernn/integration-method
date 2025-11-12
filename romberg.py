from trapezoidal import *

def romberg_1(m, n):
    if(n==0):
        return trapezoidal_1(2**m)
    return (4**n * romberg_1(m, n-1) - romberg_1(m-1, n-1)) / (4**n - 1)

def romberg_2(m, n):
    if(n==0):
        return trapezoidal_2(2**m)
    return (4**n * romberg_2(m, n-1) - romberg_2(m-1, n-1)) / (4**n - 1)