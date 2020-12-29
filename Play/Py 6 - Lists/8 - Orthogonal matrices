# Created on November, 2020
# @author: Fábio Araújo de Sá

def is_orthogonal(mx):
    
    diagonal_ok = True
    others_ok = True
    diagonal = 0
    resto = 0
    
    for i in range (0, len(mx)):
        for j in range (0, len(mx)):
        
            if i == j:
                
                for k in range(0, len(mx[i])):
                    diagonal = diagonal + mx[i][k] * mx[j][k]
                
                diagonal_ok = diagonal_ok and (diagonal == 1)
                diagonal = 0
                
            else: 
                
                for k in range(0, len(mx[i])):
                    resto = resto + mx[i][k] * mx[j][k]
                
                others_ok = others_ok and (resto == 0)
                resto = 0
                
    return ( diagonal_ok and others_ok )
