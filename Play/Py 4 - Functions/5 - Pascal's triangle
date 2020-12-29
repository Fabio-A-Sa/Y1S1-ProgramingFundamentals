# Created on November, 2020
# @author: Fábio Araújo de Sá

def pascal(n):
    string_final = ""
    import math
    for i in range (0, n): # Row
        for j in range (i+1): #Line
            string_final = string_final + str(int(math.factorial(i) / (math.factorial(j) * math.factorial(i-j))))
            if i > j:
                string_final = string_final + " "   
        string_final = string_final + "\n"      # New line                       
    
    return string_final
                                
