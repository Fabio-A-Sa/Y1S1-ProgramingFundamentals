# Created on November, 2020
# @author: Fábio Araújo de Sá

def fetch_middle(llists):
    
    from math import floor as m
    
    result = [] # empty list
    middle_element = 0
    a = 0
    b = 0
    
    for x in range (0, len(llists)):
        
        comprimento = int(len(llists[x]))
        
        if comprimento%2 == 0: # se o número de elementos for par
        
            a = round((comprimento/2)-1)
            b = round(comprimento/2)
            middle_element = round(((llists[x][a]+llists[x][b])/2), 1)
            result.append(middle_element)
        
        else: # se o número de elementos for ímpar
            b = m(comprimento/2)
            a = llists[x][b]
            result.append(a)
        
    return result
