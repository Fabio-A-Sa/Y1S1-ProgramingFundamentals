# Created on October, 2020
# @author: Fábio Araújo de Sá

number = float(input("Number? "))
a = number
b = 0

while True:
    medio = (a + b) / 2 #Ponto Médio de a e b
    if (medio*medio == number) or (round(a, 5) - round(b, 5) == 0):
        # Quando o médio é o valor ideal:
        print(round(medio, 5))
        break
    elif medio*medio > number:
        # Limita o intervalo à esquerda da raiz quadrada
        a = medio
    else:
        # Limita o intervalo à direita da raiz quadrada
        b = medio
