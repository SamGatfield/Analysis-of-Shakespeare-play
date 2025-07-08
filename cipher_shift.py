import matplotlib.pyplot as plt
import numpy as np

def Sum(m): #m is a parameter which gets passed into the function
    total = 0 
    n = 1 
    for i in range(0,m):
        total += n**(-1/5)
        n+=1
    return total


def find_shift(user_number):
    k = 1 #Initial value for the k we need to find

    while Sum(k) <= user_number:
        k += 1
        Sum(k)
        
    print(f'The value for k such that the sum is > {user_number} is k = {k}')

    #Next compute the gcd of k and user_number

    max_val = max(k, user_number)
    min_val = min(k, user_number)

    r = max_val
    s = 0 #This is for the multiples of min_val we subtract
    while r > 0:
        while r >= min_val:
            r = max_val - s*min_val
            s += 1
            
        max_val = min_val
        min_val = r
        s = 0

    gcd = max_val #Offset used to encode the text (and also the GCD)
    print(f'The GCD of {k} and {user_number} is {gcd} \n')
    shift = gcd
    return shift
    
