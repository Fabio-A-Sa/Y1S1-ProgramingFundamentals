# Created on December, 2020
# @author: Fábio Araújo de Sá

def most_frequent(alist):
    
    result = {}
    chaves = []
    for item in alist:
        result[item] = result.get(item, 0) + 1
        
    for (key, value) in result.items():
        if result[key] == max(result.values()):
            chaves.append(key)
        
    return max(chaves)
