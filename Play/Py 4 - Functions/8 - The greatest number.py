# Created on November, 2020
# @author: Fábio Araújo de Sá

def greatest(num):
    
    num = "".join(sorted(str(num), reverse = True)) # Ascending
    resultado = int(num)
        
    return resultado
