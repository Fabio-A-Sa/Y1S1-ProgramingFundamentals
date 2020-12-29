# Created on October, 2020
# @author: Fábio Araújo de Sá

a = int(input())
b = int(input())
# se for ímpar, caso contrário anula:
c = (2-(a-b)%2)*(a+b)
# se for par, caso contrário anula:
d = ((a-b)%2)*(a*b)
print(c+d)
