# Created on October, 2020
# @author: Fábio Araújo de Sá

def chegou_ao_mínimo(something):
    return type(something[-1]) == type([1,2,3])

def reduce_map_filter(args):
    
    final = args
    
    if chegou_ao_mínimo(final):
        # Se chegar ao fim da recursão e encontrar uma lista no item 3:

        if final[0] == "filter" :
            # Faz a função filter de args[1] sobre a lista args[2]
            return list(filter(final[1], final[2]))
                
                
        if final[0] == "map" :
            # Faz a função args[1] sobre a lista args[2]
            return list(map(final[1], final[2]))
            
                
        if final[0] == "reduce" :
            # Reduz a função args[1] sobre a lista arg[2]
            from functools import reduce as r
            return int(r(final[1], final[2]))

    else:
        passo_seguinte = final[-1]
        l = reduce_map_filter(passo_seguinte)
        return reduce_map_filter((final[0],final[1],l))
