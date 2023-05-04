from fractions import Fraction



from sympy.ntheory.primetest import is_square 

import logging
import time 
PRODUCTIONS_UPPERBOUND = 200
PRODUCTIONS_LOWERBOUND = 1


results = {}

# class logger():
#     def __init__(self, name):
#         self.name = name
#         logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def func(x):
    return  (2*x-1)*(4*(x*x)-2*x-1)

def testing():
    prior = set()
    
    for i in range(PRODUCTIONS_LOWERBOUND, PRODUCTIONS_UPPERBOUND):
        for j in range(PRODUCTIONS_LOWERBOUND, PRODUCTIONS_UPPERBOUND): #Deneominator
            
            frac = Fraction(i, j)
            if frac in prior:
                continue
            
            
            out = func(frac)
            
            if out == 0:
                continue

            prior.add(frac)
            results[frac] = out
            # logging.info("Fraction: %s, Result: %s", frac, out)
            logging.info("%s, %s", frac, out)
            
    del prior
            
            
            

def checkingIfSquareFree():
    sameOne = set()
    for i in results:
        for j in results:
            if i == j:
                continue
            
            if (i, j) in sameOne or (j, i) in sameOne:
                continue

            product = results[i] * results[j]

            sameOne.add((i, j))
            
            # if gmpy.is_square(int(product)):
            if is_square(product.numerator) and is_square(product.denominator):
                
                print("Square Free")
                print(i, j)
                print(results[i], results[j])
                print(results[i] * results[j])
                logging.info("%s, %s, %s, %s", i, j, results[i], results[j])
            
            
timeOfComputation = time.time()
logging.basicConfig(filename=f'output/Numebers_output{timeOfComputation}.log', filemode='w', format='%(message)s', level=logging.INFO)
testing()
logging.basicConfig(filename=f'output/SquareFree_{timeOfComputation}.log', filemode='w', format='%(message)s', level=logging.INFO)
logging.info("u, t, f(u), f(t)")
logging.debug("Square Free")
checkingIfSquareFree()
            