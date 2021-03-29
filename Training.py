def factorial (n):

    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def iter_factorial(n):

    total = 1
    while (n > 1):
        total = total * n
        n = n-1

    return total

def going(n):
    
    denominator = iter_factorial(n)
    numerator = 0
    for number in range(1, n+1):
        numerator = numerator + iter_factorial(number)

    solution = str(numerator/denominator)
    return float(solution[:solution.find(".")+7])

print(going(7))

def run ():

    c = []
    for i in range(4, 60):
        comentario = str(input("Next: "))
        if i < 10:
            c.append("[Atualização 15:0{}] : {} ".format(i, comentaSrio))
        else:
            c.append("[Atualização 15:{}] : ".format(i, comentario))
    
    for ci in c:
        print(ci)
        
print(run())