# Created on January, 2021
# @author: Fábio Araújo de Sá

def midpoint(p1, p2):
    mid = (p1 + p2) / 2
    return mid 

def bisect(f, n, lower=0, upper=1, total=0, aprox=0):

    if n == total:
        result = round(aprox, 5)
        return result

    else:

        aprox = midpoint(lower, upper)

        if f(lower)*f(aprox) < 0:
            return bisect(f, n, lower, aprox, total+1, aprox)
        else:
            return bisect(f, n, aprox, upper, total+1, aprox)
