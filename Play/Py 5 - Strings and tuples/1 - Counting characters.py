# Created on November, 2020
# @author: Fábio Araújo de Sá

def count_chars(a_string):
    
    c_alphabetic = 0
    c_digit = 0
    c_special_symbol = 0
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    a_string = a_string.upper()
    
    for i in range (0, len(a_string)):
        
        if a_string[i] in string:
            c_alphabetic = c_alphabetic + 1
            
        elif a_string[i] in numbers:
            c_digit = c_digit + 1
        
        else:
            c_special_symbol = c_special_symbol + 1
            
    result = (c_alphabetic,) + (c_digit,) + (c_special_symbol,)
    
    return result
