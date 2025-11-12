from trapezoidal import *

def richardson_extrapolation_1(p, n):
    return ((2**p * trapezoidal_1(n*2) - trapezoidal_1(n))/(2**p - 1))

def richardson_extrapolation_2(p, n):
    return ((2**p * trapezoidal_2(n*2) - trapezoidal_2(n))/(2**p - 1))

print(richardson_extrapolation_1(2, 4))
print(richardson_extrapolation_2(2, 4))