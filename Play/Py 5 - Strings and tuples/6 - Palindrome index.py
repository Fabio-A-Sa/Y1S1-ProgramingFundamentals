# Created on November, 2020
# @author: Fábio Araújo de Sá

def palindrome_index(s):
    
    new = ""
    new_new = ""
    result = 0
    
    for i in range (0, len(s)):
        
        new = s[:i] + s[i+1:] # new string sem a letra de idex i
        
        if s == s[::-1]:
            result = -1
            break

        elif new == new[::-1]: # Se é igual ao seu inverso
            result = i
            break
        
        else:
            if i == len(s)-1:
                result = -1
            else:
                continue
            
    return result

# s = str(input())
# print(palindrome_index(s))
