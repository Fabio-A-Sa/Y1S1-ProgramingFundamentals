# Created on October, 2020
# @author: Fábio Araújo de Sá

def sparse_dot_product(dict1, dict2):
    
    soma = 0
    
    for key1 in dict1:
        for key2 in dict2:
            
            if key1 == key2:
                soma = soma + dict1[key1] * dict2[key2]
            else:
                soma = soma + 0
    
    return soma
