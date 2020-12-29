# Created on December, 2020
# @author: Fábio Araújo de Sá

def is_odd(a, b):
    b = b - 1
    resto = (juggler(a,b))%2
    return resto != 0

def juggler(n, p):
    
    if p == 0:
        return n
    else:
        from math import floor as f
        if is_odd (n, p):
            return f((juggler(n, p-1))**(3/2))
        else:
            return f((juggler(n, p-1))**(1/2))
