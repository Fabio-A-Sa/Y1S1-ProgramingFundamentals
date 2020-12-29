# Created on October, 2020
# @author: Fábio Araújo de Sá

def adigits(a, b, c):
    d = 0
    e = 0
    f = 0
    g = a + b + c
    
    d = max(a, b, c)
    f = min(a, b, c)
    e = g - (d+f)
    
    return int(f"{d}{e}{f}")
