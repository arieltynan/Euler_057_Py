#Ariel Tynan
#Euler Problem 057, Square root convergents, solved in Python
#Started 7 March 2022

from math import floor
from fractions import Fraction
from decimal import *


def expansion(num,count,success,den_prev):
    while count < 1000:
        count = count + 1
        getcontext().prec = floor(count)+1000
        f = Fraction(Decimal(1 + num)).limit_denominator(100*(den_prev))
        print(count,f)
        str_num = str(f.numerator)
        str_den = str(f.denominator)
        den_prev = f.denominator
        if len(str_num) > len(str_den):
            success = success + 1
            print("YES")
        num = Decimal(1/(2+num))

        return expansion(num,count,success,den_prev)
    return success
 


print(Fraction(11,35))

frac_list = []

#print(Fraction(1,1) + expansion(1,2,0))

getcontext().prec = 300
print(expansion(0.5,0,0,3))

