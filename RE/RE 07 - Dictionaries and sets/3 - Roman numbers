# Created on October, 2020
# @author: Fábio Araújo de Sá

def roman_to_integer(a_string):
    
    decimal = 0
    a_string = a_string.upper() # Só pa confirmar
    
    dicta = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    # A letra está no dicionário -> traduz
    
    for i in range(len(a_string)):
            
        if i > 0 and dicta[a_string[i]] > dicta[a_string[i-1]]:
            # Casos do tipo IV, IX ... 
                
            decimal = decimal +  dicta[a_string[i]] - (dicta[a_string[i-1]] + dicta[a_string[i-1]])
            # Retira o valor adicionado anteriormente ao decimal e a diferença entre i e i-1
        
        else:
            # Casos do tipo normal: III, VIII, XVIII
            decimal = decimal + dicta[a_string[i]]

    return decimal
