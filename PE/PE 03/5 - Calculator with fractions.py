# Created on January, 2021
# @author: Fábio Araújo de Sá

def maximo_divisor(n1, n2):
    
    import math
    return math.gcd(n1, n2)

def calculator(expr):
    
    if len(expr) == 2:
        return expr
    
    else:
        
        operator = expr[1]
        
        if operator == "*":
            a = calculator(expr[0])
            b = calculator(expr[2])
            c = maximo_divisor(a[0]*b[0], a[1]*b[1])
            d = (((a[0]*b[0])//c), ((a[1]*b[1])//c))
            return d
        
        if operator == "/":
            a = calculator(expr[0])
            b = calculator(expr[2])
            c = maximo_divisor(a[0]*b[1], a[1]*b[0])
            d = (((a[0]*b[1])//c), ((a[1]*b[0])//c))
            return d
