# # Created on November, 2020
# @author: Fábio Araújo de Sá

import random
import statistics

pontos_circulo = 0

pontos_sorteados = 0

lista_pi = []

for i in range(100):
    for a in range(1000):
        pontos_sorteados = pontos_sorteados + 1.0

        x = random.uniform(-1,1)
        y= random.uniform(-1,1)

        distancia = x*x + y*y

        if distancia <= 1:
            pontos_circulo = pontos_circulo + 1.0

    proporcao = pontos_circulo / pontos_sorteados

    pi = 4 * proporcao
    lista_pi.append(pi)

b = statistics.stdev(lista_pi,3.1415)
n = 1

while b > 0.005:
    lista_pi = []
    for i in range(100):
        for a in range(10002):
            pontos_sorteados = pontos_sorteados + 1.0

            x = random.uniform(-1,1)
            y= random.uniform(-1,1)

            distancia = x*x + y*y

            if distancia <= 1:
                pontos_circulo = pontos_circulo + 1.0

        proporcao = pontos_circulo / pontos_sorteados

        pi = 4 * proporcao
        lista_pi.append(pi)
    n = n+1

    b = statistics.stdev(lista_pi,3.1415)

media_lista_pi = statistics.mean(lista_pi)

print(media_lista_pi)
