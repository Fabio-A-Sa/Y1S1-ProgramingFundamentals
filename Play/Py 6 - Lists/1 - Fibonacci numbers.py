# Created on November, 2020
# @author: Fábio Araújo de Sá
def fib(n):
    
    result = [0, 1] # initial values
    soma_2_anteriores = 0
    
    if n == 1:
        return [0]
    
    elif n == 2:
        return result
    
    else:
        for i in range (n-2):
            soma_2_anteriores = int(result[i]) + int(result[i+1])        
            result.append(soma_2_anteriores)
        return result
