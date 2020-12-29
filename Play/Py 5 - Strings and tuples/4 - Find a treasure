# Created on November, 2020
# @author: Fábio Araújo de Sá

def map(pos, steps):
    
    (x, y) = pos # Separar a posição inicial em x e y
    
    steps = steps.split("-") # Separar os passos segundo os -
    
    for i in range (0, len(steps)):
        
        if steps[i] == "up":
            y = y + 1
            
        elif steps[i] == "down":
            y = y - 1
            
        elif steps[i] == "left":
            x = x - 1
            
        elif steps[i] == "right":
            x = x + 1
        
        
    return (x,) + (y,)
