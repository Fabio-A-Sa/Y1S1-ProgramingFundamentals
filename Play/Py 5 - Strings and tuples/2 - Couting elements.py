# Created on November, 2020
# @author: Fábio Araújo de Sá

def count_until(tup):
    
    if len(tup) == 0:
        return -1
    
    for i in range (0, len(tup)):
        if type(tup[i]) == type((1,)):
            return i
        else:
            if (i == len(tup)-1):
                return -1
            else:
                continue
