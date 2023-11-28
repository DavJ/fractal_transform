import cmath
import math

PI = math.pi()

def fractal_transform1(signal: List[complex], k_sigma: complex):
    order = len(signal)

    if order == 1:
       return signal[0]

    else: 
       signal_even = signal[0:order:2]
       signal_odd = signal[1:order:2]
       W = exp(-j*2*PI*k_sigma/order) 

       return fractal_transform1(signal_even, k_sigma) + W*fractal_transform1(signal_odd, k_sigma)

def fractal_transform(signal: List[complex], K:int , L: int):

    return [fractal_transform1(signal, k*exp(j*theta)) for k in range(K)] for theta in range(L)]
    
     

 
