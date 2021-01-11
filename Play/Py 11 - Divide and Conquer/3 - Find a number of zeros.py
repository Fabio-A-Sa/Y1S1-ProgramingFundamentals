# Created on January, 2021
# @author: Fábio Araújo de Sá

def aux(f):
    return f if type(f) is list else f()

def count_zeros(f):

    alist = aux(f)
    total = 0

    if len(alist) == 1:
        # Caso base
        return total

    else:
            
        if len(alist)%2 == 1:
            middle = int((len(alist)+1)//2)
        else:
            middle = int(len(alist)//2)

        left = alist[:middle]
        right = alist[middle:]

        if alist[middle] != 0:
            # Os zeros estão mais à frente
            total = total + count_zeros(right)

        if alist[middle] == 0:
            # Inclui tudo para a frente mais um pedaço de trás
            total = total + len(right) + count_zeros(left)

    return total
