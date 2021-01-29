# Created on January, 2021
# @author: Fábio Araújo de Sá

def sum_dicts(lst):
    
    result = {}
    
    for dictionary in lst:
        for key in dictionary:
            
            result[key] = 0
    
    for dictionary in lst:
        for key in dictionary:
            
            result[key] = result[key] + dictionary[key]
            
            
    return result
