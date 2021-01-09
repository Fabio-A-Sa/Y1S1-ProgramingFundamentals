# Created on January, 2021
# @author: Fábio Araújo de Sá

def unique_values(alist):
    
    aset = set()
    
    for dictionary in alist:
        for key in dictionary:
            if dictionary[key] not in aset:
                aset.add(dictionary[key])
                
    return aset
