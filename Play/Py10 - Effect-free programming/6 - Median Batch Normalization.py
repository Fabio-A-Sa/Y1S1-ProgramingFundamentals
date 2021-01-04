# Created on January, 2021
# @author: Fábio Araújo de Sá

def batch_norm(alist, batch_size):

    while len(alist) != 0:

        lote = alist[:batch_size]    
        alist = alist[batch_size:]
        n = sorted(lote.copy())

        if len(lote)%2 == 1:

            mediana = n[len(lote)//2]

            yield list([number - mediana for number in lote])

        else:
            
            a = n[(len(lote)//2)-1]
            b = n[len(lote)//2]
            mediana = (a+b)/2

            yield list([number - mediana for number in lote])
