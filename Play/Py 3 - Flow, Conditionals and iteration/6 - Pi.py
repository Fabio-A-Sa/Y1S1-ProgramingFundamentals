# Created on October, 2020
# @author: Fábio Araújo de Sá

import math

somatorio = 0

for K in range(0, 51):
    somatorio = somatorio + (math.factorial(4  * K) * (1103 + 26390 * K)) / (math.factorial(K)**4 * 396**(4*K))
inversopi = (2 * 2**.5 / 9801) * somatorio

pi_normal = 1 / inversopi
print(round(pi_normal, 8))
