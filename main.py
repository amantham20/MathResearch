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
            
            prior.add(frac)
            
            out = func(frac)
            results[frac] = out
            logging.info("Fraction: %s, Result: %s", frac, out)
            
            
            

def checkingIfSquareFree():
    for i in results:
        for j in results:
            product = results[i] * results[j]
            if product.denominator != 1:
                continue

            if gmpy.is_square(int(product)):
                print("Square Free")
                print(i, j)
                print(results[i], results[j])
                print(results[i] * results[j])
                logging.info("SquareFree, %s, %s, %s, %s", i, j, results[i], results[j])
            
            
            
logging.basicConfig(filename='app1.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

testing()
checkingIfSquareFree()
            