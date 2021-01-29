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

