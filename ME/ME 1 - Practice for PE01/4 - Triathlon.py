# Created on November, 2020
# @author: Fábio Araújo de Sá

tS = float(input())
tC = float(input()) # in hours
tR = float(input())

vS = 1.5/tS
vC = 40/tC # in Km/h
vR = 10/tR

total_time = tS + tC + tR # Total time of stages

if total_time > 4:
    print("Time")
elif vS < 2:
    print("Swimming")
elif vC < 20:
    print("Cycling")
elif vR < 8:
    print("Running")
else:
    print(total_time)
