# Created on November, 2020
# @author: Fábio Araújo de Sá

import math

def solver(a,b,c):
    
    delta = (b**2 - 4*a*c)
    
    if delta > 0:
        solution1 = (-1*b+math.sqrt(delta))/(2*a)
        solution2 = (-1*b-math.sqrt(delta))/(2*a)
    
        if solution1 == solution2:
            return [solution1]
        
        if solution2 > solution1:
            return [solution1, solution2]
        else:
            return [solution2, solution1]
        
    elif delta == 0:
        solution = (-1*b)/(2*a)
        return [solution]
        
    else:
        return [] # Lista vazia
