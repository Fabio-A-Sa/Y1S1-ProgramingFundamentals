# Created on November, 2020
# @author: Fábio Araújo de Sá

def collatz(n):
    aux = n
    final_str = ""
    
    while aux > 1:
        final_str = final_str + str(aux) + ","
        
        if (aux%2 == 1):
            aux = (aux * 3 + 1)
        
        elif (aux%2 == 0):
            aux = round(aux//2)
        
    
    return (final_str + "1")
