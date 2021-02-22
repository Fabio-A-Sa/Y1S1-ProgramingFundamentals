# Created on February, 2021
# @author: Fábio Araújo de Sá

def n_lists(alist, n):
    
    for thing in alist:
        if type(thing[0]) is int:
        
            new = []
            for sublist in alist:

                if len(sublist) <= n:
                    new.append(sublist)

                else:
                    while len(sublist) > n:
                        new.append(sublist[:n])
                        sublist = sublist[n:]
                    new.append(sublist)
            
            return new

        else: # it's a list --> recursive search
            return list(n_lists(thing, n))


# alist = [[0], [1, 2, 3, 8, 9, 10], [5, 6]]
# n = 2
# print(n_lists(alist, n))