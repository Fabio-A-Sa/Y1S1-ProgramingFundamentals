# Created on October, 2020
# @author: Fábio Araújo de Sá

def mastermind(g1, g2, g3, c1, c2, c3):
    pontuation = 0
    
    if g1 == c1:
        pontuation = pontuation + 3
    if g1 == c2 or g1 == c3:
        pontuation = pontuation + 1
    
    if g2 == c2:
        pontuation = pontuation + 3
    if g2 == c1 or g2 == c3:
        pontuation = pontuation + 1
        
    if g3 == c3:
        pontuation = pontuation + 3
    if g3 == c1 or g3 == c2:
        pontuation = pontuation + 1
    
    if (g1 == g2 or g1 == g3 or g2 == g3) and not (g1 == g2 == g3):
        pontuation = pontuation - 1
    
    if g1 == g2 and g2 == g3:
        pontuation = 6
    
    return (pontuation)
