# Created on December, 2020
# @author: Fábio Araújo de Sá

def gcd_rec(n1, n2):
    
    resto = n1%n2
    if resto == 0:
        return n2
    
    else:
        return gcd_rec(n2,resto)

# Other option without recursion
# def gcd_rec(n1, n2):
#     from math import gcd as euclid
#     return euclid(n1,n2)
