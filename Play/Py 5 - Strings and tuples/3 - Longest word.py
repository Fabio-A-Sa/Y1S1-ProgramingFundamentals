# Created on November, 2020
# @author: Fábio Araújo de Sá

def longest(s):
    
    s = s.split()
    long = 0
    
    for i in range(0, len(s)):
        
        medida = len(s[i])
        
        if medida >= long:
            long = medida
            

    return long  
