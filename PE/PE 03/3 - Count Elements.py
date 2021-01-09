# Created on January, 2021
# @author: Fábio Araújo de Sá

def rec(alist):
    
    blist = []
    for item in alist:
        if type(item) != list:
            blist.append(item)
            
        else:
            blist = blist + rec(item)
            
    return blist

def rec_count(alist):
    
    blist = rec(alist)
    
    adict = {}
    for item in blist:
        adict[item] = adict.get(item, 0) + 1
        
    return adict
