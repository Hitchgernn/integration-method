import math

PI = math.pi

def f_1(x):
    return math.cos(x)

def quadpt_1(a, b):
    tol = 1e-10
    c = (a+b)/2
    fa = f_1(a)
    fb = f_1(b)
    fc = f_1(c)
    I, E = qstep_1(a, b, tol, fa, fc, fb)
    return I, E

def qstep_1(a, b, tol, fa, fc, fb):
    h1 = (b - a)/2
    h2 = h1/2
    c = (a + b)/2
    fd = f_1((a + c)/2)
    fe = f_1((c + b)/2)
    I1 = h1/3 * (fa + 4*fc + fb)
    I2 = h2/3 * (fa + 4*fd + 2*fc + 4*fe + fb)

    E = abs(I2 - I1)  # estimated local error
    
    if E < tol:
        I = I2 + (I2 - I1) / 15
        return I, E
    else:
        Ia, Ea = qstep_1(a, c, tol / 2, fa, fd, fc)
        Ib, Eb = qstep_1(c, b, tol / 2, fc, fe, fb)
        return Ia + Ib, Ea + Eb
    
def f_2(x):
    return x**2

def quadpt_2(a, b):
    tol = 1e-10
    c = (a+b)/2
    fa = f_2(a)
    fb = f_2(b)
    fc = f_2(c)
    I, E = qstep_2(a, b, tol, fa, fc, fb)
    return I, E

def qstep_2(a, b, tol, fa, fc, fb):
    h1 = (b - a)/2
    h2 = h1/2
    c = (a + b)/2
    fd = f_2((a + c)/2)
    fe = f_2((c + b)/2)
    I1 = h1/3 * (fa + 4*fc + fb)
    I2 = h2/3 * (fa + 4*fd + 2*fc + 4*fe + fb)

    E = abs(I2 - I1)  # estimated local error
    
    if E < tol:
        I = I2 + (I2 - I1) / 15
        return I, E
    else:
        Ia, Ea = qstep_2(a, c, tol / 2, fa, fd, fc)
        Ib, Eb = qstep_2(c, b, tol / 2, fc, fe, fb)
        return Ia + Ib, Ea + Eb

if __name__ == "__main__":
    I, E = quadpt_1(0, PI/2)
    print(f"Aproximation first integral: {I}")
    print(f"Estimated local error: {E}\n")
    I, E = quadpt_2(0, 1)
    print(f"Aproximation first integral: {I}")
    print(f"Estimated local error: {E}\n")