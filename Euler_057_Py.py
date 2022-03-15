#Ariel Tynan
#Euler Problem 057, Square root convergents, solved in Python
#Started 7 March 2022

from math import floor
from fractions import Fraction
from decimal import *

#Expansion function uses recursion to layer the fraction shown in the problem
#Outputs result in fractional form for every added layer
#Takes in the current total value in "num"
#Count, the number of iterations
#Success, the number of successes very len numerator > len denominator
#den_prev, the previous denominator value for use of limiting the next denominator
def expansion(num,count,success,den_prev):
    while count < 1000: #1000 iterations
        count = count + 1 #while loop used for recursion
        f = Fraction(Decimal(1 + num)).limit_denominator(100*(den_prev))
        print(count,f)
        str_num = str(f.numerator)
        str_den = str(f.denominator)
        den_prev = f.denominator
        if len(str_num) > len(str_den): #check num is longer than den each iteration
            success = success + 1
            print("YES")
        num = Decimal(1/(2+num))

        return expansion(num,count,success,den_prev)
    return success
 

getcontext().prec = 1000 #precision to 1000 decimal places
print(expansion(0.5,0,0,3)) #(num, count, success, den_prev)

