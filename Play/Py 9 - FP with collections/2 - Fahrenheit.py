# Created on December, 2020
# @author: Fábio Araújo de Sá

def to_fahrenheit(t):
    return list(map(lambda f: round(((f*1.8)+32), 2), t))
