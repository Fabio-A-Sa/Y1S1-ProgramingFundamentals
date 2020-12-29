# Created on October, 2020
# @author: Fábio Araújo de Sá

import math
def time_until_lost_connection(direction_A, direction_B):
    
    # Constantes

    velocidade = 5 # km/h ou 5/60 km/minuto
    distancia_maxima = 35 # km em linha reta
    pi = math.pi

    # Passagem de graus para radianos

    ra = direction_A*pi/180
    rb = direction_B*pi/180
    
    # Cálculo da distância entre A e B
    
    total_distance = math.sqrt((35*35)/((math.cos(rb)-math.cos(ra))**2+(math.sin(rb)-math.sin(ra))**2))
    time = (total_distance*60)/5
    
    return round(time, 3)
