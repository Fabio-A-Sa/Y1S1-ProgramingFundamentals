# Created on December, 2020
# @author: Fábio Araújo de Sá

def academy_awards(alist):
    
    result = {}
    for item in alist:
        result[item[1]] = result.get(item[1], 0) + 1 

    return result
