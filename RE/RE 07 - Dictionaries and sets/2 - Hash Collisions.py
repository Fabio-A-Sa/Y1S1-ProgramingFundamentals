# Created on October, 2020
# @author: Fábio Araújo de Sá

def collisions(alist):
    
    blist = [] # Vai conter as somas de dígitos de cada número
    clist = [] # Vai conter os %8 de blist
    final_dict = {} # dicionário formado pela clist
    
    for number in alist:
        
        if len(str(number)) == 1:
            blist.append(number)
            continue
        
        else:
            soma = 0
            while number > 9:
                digit = number%10
                soma = soma + digit
                number = number//10
             
            soma = soma + number    
            blist.append(soma)
            soma = 0 # Null
            
            
    for number in blist:
        clist.append(number%8)
        
    # formar o dicionário correspondente
    
    for number in clist:
        final_dict[number] = final_dict.get(number, 0) + 1 
    
    return final_dict
