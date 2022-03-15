#Ariel Tynan
#Euler Problem 057, Square root convergents, solved in Python
#Started 7 March 2022, solved 14 March 2022

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
        #print(count,f)
        den_prev = f.denominator
        if len(str(f.numerator)) > len(str(f.denominator)): #check num is longer than den each iteration
            success = success + 1
        return expansion(Decimal(1/(2+num)),count,success,den_prev) #recursion with updated vars
    return success
 

getcontext().prec = 1000 #precision to 1000 decimal places
print(expansion(0.5,0,0,3)) #(num, count, success, den_prev)

