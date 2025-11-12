import math
PI = math.pi

def trapezoidal_1(m):
    h = (PI/2)/(m)
    sum = 0
    for i in range(0,m+1):
        if(i==0 or i==m):
            sum += math.cos(i*h)
        else:
            sum += math.cos(i*h) * 2
    return sum * h/2

def trapezoidal_2(m):
    h = 1/(m)
    sum = 0
    for i in range(0,m+1):
        if(i==0 or i==m):
            sum += (i*h)**2
        else:
            sum += (i*h)**2 * 2
    return sum * h/2