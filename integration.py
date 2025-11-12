#TRAPEZOIDAL RULE

#1.) cos(x) from 0 to pi/2
#2.) x^2 from 0 to 1

import math

PI = math.pi

def f_1(x, h):
    return math.cos(x*h)

def f_2(x, h):
    return (x*h)**2

def trapezoidal_1(m):
    #ada m+1 trapesium
    h = (PI/2)/(m+1)
    sum = 0
    for i in range(0,m+2):
        if(i==0 or i==m+1):
            sum += f_1(i, h)
        else:
            sum += f_1(i, h) * 2
    return sum * h/2

def trapezoidal_2(m):
    h = 1/(m+1)
    sum = 0
    for i in range(0,m+2):
        if(i==0 or i==m+1):
            sum += f_2(i, h)
        else:
            sum += f_2(i, h) * 2
    return sum * h/2

for i in range(0, 10):
    print(f"{i+1} {trapezoidal_1(i)}")

print()

for i in range(0, 10):
    print(f"{i+1} {trapezoidal_2(i)}")
