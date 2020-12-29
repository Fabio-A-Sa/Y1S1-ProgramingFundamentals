# Created on October, 2020
# @author: Fábio Araújo de Sá

number = int(input())
soma = 0

for i in range(1, number+1):
    if number%i == 0:
        soma = soma + i
        
print(soma)
