# Created on November, 2020
# @author: Fábio Araújo de Sá

def pattern_hunting(l1, l2, p):

    result = [] # empty list
    
    for element in range(0, len(l1)):
        
        if p in l1[element]:
            result.append(l2[element])
            
        elif p in l2[element]:
            result.append(l1[element])
    
    final = sorted(result, reverse=True)
    
    return final
