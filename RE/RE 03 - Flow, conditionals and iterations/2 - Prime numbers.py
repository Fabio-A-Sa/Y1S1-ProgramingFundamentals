# Created on October, 2020
# @author: Fábio Araújo de Sá

num = int(input("Number? "))
divisores = 0

if num == 1:
    print("False)
else:
    for i in range(1, num+1, 1):
        if num % i == 0:
            divisores = divisores + 1
            
    if divisores > 2:
        print("False")
    else:
        print("True")
