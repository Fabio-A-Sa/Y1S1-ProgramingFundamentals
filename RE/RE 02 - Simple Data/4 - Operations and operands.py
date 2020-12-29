# Created on October, 2020
# @author: Fábio Araújo de Sá

p = float(input())
n = float(input())
r = float(input())

a = (p*((1+r/n)**n)**2)     
print(round(a, 3))
