from fractions import Fraction
import gmpy

import logging

PRODUCTIONS_UPPERBOUND = 1000
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
            if gmpy.is_square(product.numerator) and gmpy.is_square(product.denominator):
                
                print("Square Free")
                print(i, j)
                print(results[i], results[j])
                print(results[i] * results[j])
                logging.info("SquareFree, %s, %s, %s, %s", i, j, results[i], results[j])
            
            
            
logging.basicConfig(filename='app3.log', filemode='w', format='%(message)s', level=logging.INFO)

testing()
logging.debug("Square Free")
checkingIfSquareFree()
            