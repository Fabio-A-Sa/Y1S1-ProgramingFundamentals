# Created on December, 2020
# @author: Fábio Araújo de Sá

def separação(atuple):
    
    total = []  
    total.append(atuple)
    atuple = list(atuple)
    
    for item in atuple:
        if type(item) != type(("f","a","b")):
            continue
        else:
            subtotal = biggest_member(item) # Fragmentação
            total.append(item)
            total.append(subtotal)
            
    return total

def biggest_member(atuple):

    all_tuples = separação(atuple)
    item_max = all_tuples[0]
    
    for item in all_tuples:
        if len(item) > len(item_max):
            item_max = item
    
    return item_max
