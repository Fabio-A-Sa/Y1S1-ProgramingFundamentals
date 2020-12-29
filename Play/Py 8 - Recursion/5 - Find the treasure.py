# Created on December, 2020
# @author: Fábio Araújo de Sá

def find_treasure(pos, steps):
    
    if len(steps) == 0:
        return pos
    
    else:
        (x, y) = pos
        
        if steps[0] == "up":
            y = y + 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
        if steps[0] == "down":
            y = y - 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps) 
        if steps[0] == "left":
            x = x - 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
        if steps[0] == "right":
            x = x + 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
