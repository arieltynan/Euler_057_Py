#Ariel Tynan
#Euler Problem 057, Square root convergents, solved in Python
#Started 7 March 2022

from fractions import Fraction



def expansion(num,count,success):
    while count < 1000:
        count = count + 1
        f = Fraction(1 + num).limit_denominator(100000000)
        print(f,f.numerator,f.denominator,count)
        str_num = str(f.numerator)
        str_den = str(f.denominator)
        if str_num[0] == '1' and str_den[0] != '1':
            success = success + 1
            print("YES")
        num = 1/(2+num)
        #if f[0] % f[1] > f[0]/2:
            #success = success + 1
        return expansion(num,count,success)
    return success
 


print(Fraction(11,35))

frac_list = []

#print(Fraction(1,1) + expansion(1,2,0))

print(expansion(0.5,0,0))
