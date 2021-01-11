# Created on January, 2021
# @author: Fábio Araújo de Sá

def aux(f):
    return f if type(f) is list else f()

def bitonic_point(f):

    alist = aux(f)

    if len(alist)%2 == 1:
        middle = (len(alist)+1)//2
    else:
        middle = len(alist)//2

    left = alist[:middle]
    right = alist[middle:]

    if alist[middle - 1] < alist[middle] and alist[middle] > alist[middle + 1]:
        # Atingiu o pico
        return alist[middle]

    if alist[middle-1] < alist[middle]:
        # O número procurado está depois
        return bitonic_point(right)
    
    if alist[middle] > alist[middle + 1]:
        # O número procurado está antes
        return bitonic_point(left) 
