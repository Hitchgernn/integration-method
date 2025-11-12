from adaptive_integration import *
from extrapolation import *
from gauss import *
from romberg import *
from trapezoidal import *

if __name__ == "__main__":
    #1.) Trapezoidal
    print("===============TRAPEZOIDAL===============")
    for n in range(1, 11):
        print(f"n={n}, hasil = {trapezoidal_1(n)}")
    print()
    for n in range(1, 11):
        print(f"n={n}, hasil = {trapezoidal_2(n)}")
    print()

    #2.) Extrapolation
    print("===============EXTRAPOLATION===============")
    print(f"p=2, hasil = {richardson_extrapolation_1(2, 4)}\n")
    print(f"p=2, hasil = {richardson_extrapolation_2(2, 4)}\n")

    #3.) Romberg
    print("===============ROMBERG===============")
    romberg_list = []
    for m in range(0, 3):
        for n in range(0, 3):
            if(n<=m):
                romberg_list.append(romberg_1(m, n))
        print(romberg_list)
        romberg_list.clear()

    print()
    romberg_list.clear()

    for m in range(0, 3):
        for n in range(0, 3):
            if(n<=m):
                romberg_list.append(romberg_2(m, n))
        print(romberg_list)
        romberg_list.clear()

    print()
    romberg_list.clear()

    #4.) Adaptive Integration
    print("===============ADAPTIVE INTEGRATION===============")
    I, E = quadpt_1(0, PI/2)
    print(f"Aproximation first integral: {I}")
    print(f"Estimated local error: {E}\n")

    I, E = quadpt_2(0, 1)
    print(f"Aproximation first integral: {I}")
    print(f"Estimated local error: {E}\n")

    #5.) Gauss
    print("===============GAUSSIAN QUADRATURE===============")
    a = 0
    b = PI/2
    for n in range(1, 11):
        result = gauss_1(a, b, n)
        print (f"n={n}, hasil = {result}")

    print()

    a = 0
    b = 1
    for n in range(1, 11):
        result = gauss_2(a, b, n)
        print (f"n={n}, hasil = {result}")
