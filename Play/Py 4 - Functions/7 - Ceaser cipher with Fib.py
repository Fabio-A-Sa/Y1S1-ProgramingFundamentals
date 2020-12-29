# Created on November, 2020
# @author: Fábio Araújo de Sá

def caesar(message):
    
    import math
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    result = "" # Empty string to accumulate
    
    n = 0
    
    for letter in message:
        if letter in alphabet:
            result = result + alphabet[(alphabet.index(letter) - int((((1+math.sqrt(5))**n)-(((1-math.sqrt(5))**n)))/((2**n)*(math.sqrt(5))))) % 26]
        else:
            result = result + letter # In correct order
        n = n + 1
        
    return result
