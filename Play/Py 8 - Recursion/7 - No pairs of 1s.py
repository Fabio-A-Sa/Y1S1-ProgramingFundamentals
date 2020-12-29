# Created on December, 2020
# @author: Fábio Araújo de Sá

dict_numbers = {1:2, 2:3}
def no_consecutives1(k):
    # Fibonacci sequence with dict

    if k in dict_numbers:
        return dict_numbers[k]
    
    else:
        valor = no_consecutives1(k-1) + no_consecutives1(k-2)
        dict_numbers[k] = valor
        return dict_numbers[k]
