# Created on October, 2020
# @author: Fábio Araújo de Sá

def square_r(number):
    return number**2

def map_reduce(n1, n2):
    
    from functools import reduce as r
    
    numbers = [number for number in range(n1, n2) if number%2 == 1] # All odd numbers between n1 and n2
    squares = list(map(square_r, numbers)) # Sqrt using map
    
    soma_or_multi = r((lambda x, y: x * y if x*y<50 else x+y), squares)

    return soma_or_multi
