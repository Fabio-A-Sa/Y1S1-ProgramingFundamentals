# Created on November, 2020
# @author: Fábio Araújo de Sá

d = int(input())
num = int(input())

aux = num
soma = 0

for i in range (1, len(str(num))+1):

    digit = aux%10
    
    if digit > d:
        soma = soma + digit**2
    
    aux = aux//10
    
print(soma)
