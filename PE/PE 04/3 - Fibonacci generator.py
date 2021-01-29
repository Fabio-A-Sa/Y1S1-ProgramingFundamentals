# Created on January, 2021
# @author: Fábio Araújo de Sá

def rec_fib(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    else:
        return rec_fib(n-1) + rec_fib(n-2)
    
    
def fib(start, end):
    
    all_numbers = []
    
    for n in range(start, end+1):
        all_numbers.append(rec_fib(n))
    
    for number in all_numbers:
        yield number

# JCL's better solution:
