# Created on October, 2020
# @author: Fábio Araújo de Sá

distance = 313
hour_integer = int(input())
minutes_integer = int(input())/60

hours_data= hour_integer + minutes_integer
velocidade = distance/hours_data

v = round(velocidade)
print(v)
