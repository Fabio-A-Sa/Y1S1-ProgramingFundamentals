# Created on December, 2020
# @author: Fábio Araújo de Sá

def permuta(alist, step=0):

    all_permutations = []

    if len(alist) == 1:
        # Base case
        return list([alist])
    
    if len(alist) == 2:
        return [alist, [alist[1], alist[0]]]

    if len(alist) == step:
        all_permutations.append(alist)

    if len(alist) > 2:
        a = step
        b = len(alist)
        for item in range(a, b):
            cop = alist.copy()
            cop[item] = alist[a]
            cop[a] = alist[item]
            all_permutations += permuta(cop, 1+a)
        
        return all_permutations
