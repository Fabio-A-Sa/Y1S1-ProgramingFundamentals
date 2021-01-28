# Created on January, 2021
# @author: JCL as PE 03 solution

# First solution

# importing functools for reduce()
import functools

def nested_fmr(f, m, r, lst):
    # using recursion to deal with the nested list
    # base case
    if type(lst) != list:
        return lst
    # iteration with the recursive call
    aux = []
    for l in lst:
        aux.append(nested_fmr(f, m, r, l))
    
    return functools.reduce(r, map(m, filter(f, aux)))

# Second solution

def nested_fmr2(f, m, r, lst):
    # solve it with the focus on data (as in PE04)  
    if type(lst) != list:
        return lst
    aux = [nested_fmr2(f, m, r, l) for l in lst]

    return functools.reduce(r, map(m, filter(f, aux)))
