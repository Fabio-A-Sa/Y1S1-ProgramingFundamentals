# Created on November, 2020
# @author: Fábio Araújo de Sá

num = int(input())
soma = 0

for i in range (1, num+1):
    if num%i == 0:
        soma = soma + i
    else:
        continue

print(soma)
    
