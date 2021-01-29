# Created on January, 2021
# @author: Fábio Araújo de Sá

def lists_to_dict(list1, list2):
    
    result = {}
    
    for key in list1:
        for value in list2:
            
            if list1.index(key) == list2.index(value):
                
                result[key] = value
                
    return result
