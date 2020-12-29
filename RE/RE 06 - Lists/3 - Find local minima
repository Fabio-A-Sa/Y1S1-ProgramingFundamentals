# Created on October, 2020
# @author: Fábio Araújo de Sá

def local_minima (alist, n):
    
    result = []
    avaliados = round((n-n%2)/2) # Números avaliados para cada lado
    
    for (i, number) in enumerate(alist):
        
        if i-avaliados < 0:
            esquerda = alist[0:i]
        else:
            esquerda = alist[i-avaliados:i]
        
        direita = alist[i+1:i+1+avaliados]
        
        if result == [] or (i - result[-1][1] > avaliados): 
            
            if direita == []: # Se está no fim da lista
            
                if number < min(esquerda) or min(esquerda) == number:
                    result.append((number, i)) # Add tuple
                    
            elif esquerda == []: # Se está no início da lista
            
                if number < min(direita) or min(direita) == number:
                    result.append((number, i)) # Add tuple
                    
            else: # Está no meio da lista, sem ser nas pontas
                
                if (number <= min(esquerda) and number <= min(direita)):
                    result.append((number, i)) # Add tuple
                    
    return result
