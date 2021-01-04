# Created on January, 2021
# @author: Fábio Araújo de Sá

def to_celsius(t):
    temperatures = [round(((c-32)/1.8), 2) for c in t]
    return list(temperatures)
