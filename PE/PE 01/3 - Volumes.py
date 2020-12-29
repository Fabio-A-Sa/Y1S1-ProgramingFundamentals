# Created on November, 2020
# @author: Fábio Araújo de Sá

import math
shape = str(input())

if (shape == "sphere"):
    radius = float(input())
    
    volume = (4/3)*math.pi*(radius**3)

elif (shape == "cylinder") or (shape == "cone"):
    radius = float(input())
    height = float(input())
    
    if (shape == "cylinder"):
        volume = math.pi*(radius**2)*height
        
    elif (shape == "cone"):
        volume = (1/3)*math.pi*(radius**2)*height

print(round(volume, 1))
