# Created on December, 2020
# @author: Fábio Araújo de Sá

def treasure(clues):
    
    tesouro = (0, 0)
    while tesouro in clues:
        # retirar a key correspondente
        tesouro = clues.pop(tesouro)
    
    return tesouro
    
    
