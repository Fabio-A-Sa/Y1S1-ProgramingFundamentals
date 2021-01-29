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

# Another recursive and better solution:

import time

def rec_fib(n, fib_values):

    if n in fib_values.keys():
        return fib_values[n]

    else:
        fib_values[n] = rec_fib(n-1, fib_values) + rec_fib(n-2, fib_values)
        return fib_values[n]

    
def fib(start, end):
    
    all_numbers = []

    fib_values = {
        
        1 : 1,
        2 : 1,
        3 : 2, 

    }

    total = 0
    t0 = time.perf_counter()

    for n in range(start, end+1):
        print("Número {} da Sequência de Fibonacci --> {}".format(n, rec_fib(n, fib_values)))
        t1 = time.perf_counter()
        total = total + t1
        print("Tempo que demorou: {} segundos".format(round(t1-t0, 2)))
        print(" ")
        all_numbers.append(rec_fib(n, fib_values))
    
    t1 = time.perf_counter()
    
    print(" ")
    return "Processo finalizado. Tempo total utilizado: {} segundos!".format(round(total, 2))
    
931487 segundos = 10 dias aproximadamente!
start = 1
end = 10000
print(fib(start, end))
