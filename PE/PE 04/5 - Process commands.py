# Created on January, 2021
# @author: Fábio Araújo de Sá

import functools, itertools

def rec_hof(hofs, lst):
    
    # Se já não houver funções, a lista pretendida é a que está em lst
    if hofs == []:
        return lst
    
    # Se ainda houver funções, chamada recursiva entre o resto das funções e 
    # a lista derivada da função em índice 0

    else:
        return rec_hof(hofs[:len(hofs)-1], hofs[-1][0](hofs[-1][1], lst))
      
# JCL's better solution:

# alternative solution 1
def rec_hof(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists
    aux = [rec_hof(hofs[1:], x) for x in lst]
    # apply the first higher-order function to the sub-lists
    (f_op, f_arg) = hofs[0]
    return f_op(f_arg, aux)

# alternative solution 2
def rec_hof2(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists
    aux = []
    for l in lst:
        aux.append(rec_hof(hofs[1:], l))
        # apply the first higher-order function to the sub-lists
        (f_op, f_arg) = hofs[0]

    return f_op(f_arg, aux)

# alternative solution 3
import functools
def rec_hof3(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists using partial function application
    aux = map(functools.partial(rec_hof, hofs[1:]), lst)
    # apply the first higher-order function to the sub-lists
    (f_op, f_arg) = hofs[0]

    return f_op(f_arg, aux)
