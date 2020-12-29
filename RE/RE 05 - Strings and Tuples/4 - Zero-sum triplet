# Created on October, 2020
# @author: Fábio Araújo de Sá

def triplet(a_tuple):
    
    a = 0
    b = 0
    c = 0
    
    empty = ()
    final_tuple = ()
    final_final_tuple = ()

    for x in range (0, len(a_tuple)):
        for y in range (x+1, len(a_tuple)):
            for z in range (y+1, len(a_tuple)):
                
                if ((int(a_tuple[x]) + int(a_tuple[y]) + int(a_tuple[z])) == 0):
                    
                    a = int(a_tuple[x])
                    b = int(a_tuple[y])
                    c = int(a_tuple[z])
                    
                    final_tuple = (a,) + (b,) + (c,)
                    final_final_tuple = final_final_tuple + (final_tuple,)
                    
    if len(final_final_tuple) == 0:
        return empty
    else:
        return final_final_tuple[0]
