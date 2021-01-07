# Created on December, 2020
# @author: Fábio Araújo de Sá

def average(a, b):

    from math import ceil as c
    result = c((a+b)/2)
    return result

def next_number(n):

    if n < 100: # Only 2 digits
        return average((n%10), ((n//10)%10))
    else: # More than 2 digits
        return average(n % 10, (n//10) % 10) + next_number(n//10) * 10
        
def digits_average(n):

    if n < 9: # Only one digit
        return n
    else: # Two or more
        return digits_average(next_number(n))
