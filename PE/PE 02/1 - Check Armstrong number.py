# Created on December, 2020
# @author: Fábio Araújo de Sá

def is_armstrong(n):     
    
    aux = n
    soma = 0
    
    while aux:
        
        soma = soma + (aux%10)**3
        aux = aux//10
    
    return (soma == n)
