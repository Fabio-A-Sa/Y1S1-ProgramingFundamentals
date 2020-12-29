# Created on October, 2020
# @author: Fábio Araújo de Sá

import math

def digits_average(n):
    
    while (n//10 != 0 ):
        number = 0
        i = 1
        while (n//10 != 0):
            a = n%10 #resto
            n = n//10
            b = n%10
            c = math.ceil((a+b)/2) #Arredonda sempre para cima
            number = number + c*i
            i = i *10
        n = number
    return n
