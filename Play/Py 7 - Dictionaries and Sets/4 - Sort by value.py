# Created on December, 2020
# @author: Fábio Araújo de Sá

def ordem(result):
    return result[1]

def sort_by_value(dict):
    
    result = []
    atuple = ()
    for key, value in dict.items():
        atuple = (key, value)
        result.append(atuple)
    
    return sorted(result, key=ordem)
