# Created on December, 2020
# @author: Fábio Araújo de Sá

def reverse_subtuples(alist):
    
    clist = []
    for i in range(len(alist)):
        blist = list(alist[i])
        blist.reverse()
        clist.append(tuple(blist))
    
    return clist
