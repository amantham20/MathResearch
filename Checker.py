from fractions import Fraction
from sympy.ntheory.primetest import is_square

import subprocess
import time



def process_result(i, j, val_i, val_j):

    product = val_i * val_j

    if is_square(product.numerator) and is_square(product.denominator):
        print("Square Free")
        print(i, j)
        print(val_i, val_j)
        print(val_i* val_j)
        # logging.info("%s, %s, %s, %s", i, j, results[i], results[j])

def main():



    filename = 'Numbers/NumberAndOut100.log'

    numberoflines = int(subprocess.check_output('wc -l ' + filename, shell=True).split()[0])
    print(numberoflines)
    i = 0
    counts = 0

    startTime = time.perf_counter()

    with open(filename, 'r') as file1:
        for line1 in file1:
            temp1 = line1
            line1 = line1.split(',')
            with open(filename, 'r') as file2:
                for line2 in file2:
                    if temp1 == line2:
                        i += 1
                        if ( i % (numberoflines//100) == 0):
                            print( i/numberoflines * 100, "%")
                        break
                    
                    line2 = line2.split(',')
                    process_result(line1[0], line2[0], Fraction(line1[1]), Fraction(line2[1]))
                    # counts += 1



    endTime = time.perf_counter()

    print(endTime - startTime, "seconds")
    print(i)
    print(counts)



if __name__ == "__main__":
    main()