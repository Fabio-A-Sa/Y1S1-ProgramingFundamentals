# Created on November, 2020
# @author: Fábio Araújo de Sá

def all_deleted(alist):
    answer = (len(alist) == 1)
    return answer

def last_man_standing(alist, step):
    
    contador = step - 1
    
    while all_deleted(alist) == False:
        
        while contador > len(alist):
            contador = contador - len(alist) # dá voltas ao circulo
    
        if contador < len(alist):
            
            next_deleted = alist[contador]
            alist.remove(next_deleted)
            contador = contador - 1 + step
            
        else: # contador = len(alist)
            
            next_deleted = alist[0]
            alist.remove(next_deleted)
            contador = step - 1
            
    return alist[0]
