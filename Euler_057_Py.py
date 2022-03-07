#Ariel Tynan
#Euler Problem 057, Square root convergents, solved in Python
#Started 7 March 2022

from fractions import Fraction

def expansion(num,den,count):
    while count < 1000:
        count = count + 1
        den = den + Fraction(1,2)
        f = Fraction(num,den)
        print(Fraction(num,den),count)
        return expansion(f.numerator, f.denominator,count)
    return Fraction(num,den) 
 


print(Fraction(11,35))

frac_list = []

#print(Fraction(1,1) + expansion(1,2,0))

expansion(1,2,0)
