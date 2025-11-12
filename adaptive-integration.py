import math
PI = math.pi

def quadpt_1(a, b):
    tol = 1e-10
    c = (a+b)/2
    fa = math.cos(a)
    fb = math.cos(b)
    fc = math.cos(c)
    I, E = qstep_1(a, b, tol, fa, fc, fb)
    return I, E

def qstep_1(a, b, tol, fa, fc, fb):
    h1 = (b - a)/2
    h2 = h1/2
    c = (a + b)/2
    fd = math.cos((a + c)/2)
    fe = math.cos((c + b)/2)
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

def quadpt_2(a, b):
    tol = 1e-10
    c = (a+b)/2
    fa = a**2
    fb = b**2
    fc = c**2
    I, E = qstep_2(a, b, tol, fa, fc, fb)
    return I, E

def qstep_2(a, b, tol, fa, fc, fb):
    h1 = (b - a)/2
    h2 = h1/2
    c = (a + b)/2
    fd = ((a + c)/2)**2
    fe = ((c + b)/2)**2
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