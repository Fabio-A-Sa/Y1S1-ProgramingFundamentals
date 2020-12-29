# Created on October, 2020
# @author: Fábio Araújo de Sá

def flatten(alist):
    
    final_list = []
    
    for item in alist:
        
        if type(item) is list:
            final_list = final_list + flatten(item)
        
        else:
            final_list.append(item)
            
    return final_list
