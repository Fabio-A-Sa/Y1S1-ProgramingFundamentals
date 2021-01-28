# Created on January, 2021
# @author: Fábio Araújo de Sá

def to_fahrenheit(t):
    temperatures = [round(((f*1.8)+32), 2) for f in t]
    return list(temperatures)
