# Created on January, 2021
# @author: Fábio Araújo de Sá

def maximum_depth(alist):
    
    # Caso base
    if alist == []:
        return 1

    # Else
    total = 0
    for item in alist:
        sub_total = maximum_depth(item)
        if sub_total > total:
            total = sub_total

    total = total + 1 # Add [] form        
    return total
