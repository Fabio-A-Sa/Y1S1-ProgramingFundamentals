# Created on October, 2020
# @author: Fábio Araújo de Sá

def jump(l):
    
    i = 0
    counter = 0
    i = l[i]
    
    while i != -1:
        counter = counter + 1
        i = l[i]
        
    return counter
