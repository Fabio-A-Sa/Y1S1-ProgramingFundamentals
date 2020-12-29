# Created on October, 2020
# @author: Fábio Araújo de Sá

num = int(input("Number? "))
result = 0
temporario = num

while temporario > 0:
    unid = temporario % 10
    result = result * 10 + unid
    temporario = temporario // 10

print(result)
