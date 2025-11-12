import math
PI = math.pi

def trapezoidal_1(n):
    h = (PI/2)/(n)
    sum = 0
    for i in range(0,n+1):
        if(i==0 or i==n):
            sum += math.cos(i*h)
        else:
            sum += math.cos(i*h) * 2
    return sum * h/2

def trapezoidal_2(n):
    h = 1/(n)
    sum = 0
    for i in range(0,n+1):
        if(i==0 or i==n):
            sum += (i*h)**2
        else:
            sum += (i*h)**2 * 2
    return sum * h/2