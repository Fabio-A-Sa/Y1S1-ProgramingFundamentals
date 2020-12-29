# Created on October, 2020
# @author: Fábio Araújo de Sá

def conc(l1,l2):
    # Add/conc item in l2 and item in l1 if item[0] in l1 not in item[0] in l2
    alist = [x for x in l2] + [y for y in l1 if (y[0] not in (z[0] for z in l2))]  
    return alist 
    
def override(l1, l2):
    # Sorted by firts letter in tuple
    return sorted(conc(l1, l2), key = lambda x: x[0] )
