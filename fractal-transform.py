from typing import List
import cmath
import math
import numpy as np

PI = math.pi
j=1j

def fractal_transform1(signal: List[complex], k_sigma: complex):
    order = len(signal)

    if order == 1:
       return signal[0]

    else: 
       signal_even = signal[0:order:2]
       signal_odd = signal[1:order:2]
       W = cmath.exp(-j*2*PI*k_sigma/order)

       return fractal_transform1(signal_even, k_sigma) + W*fractal_transform1(signal_odd, k_sigma)

def fractal_transform(signal: List[complex]):
    K = len(signal)
    L = K
    return np.array([[fractal_transform1(signal, k*cmath.exp(j*2*PI*l/L)) for k in range(K)] for l in range(L)])

print(fractal_transform([1,0,1,0,1,0,1,0]))

    
     

 
