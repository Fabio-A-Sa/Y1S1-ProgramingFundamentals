# Created on October, 2020
# @author: Fábio Araújo de Sá

def palindrome(a_string):
    
      counter = 0
      
      for x in range(0, len(a_string)-1):
         for y in range(x, len(a_string)):
            
             if y > x: # Y anda sempre à frente de X
                 string = a_string[x:y+1]
                 if string == string[::-1]: # Se encontrar uma sequência igual
                     counter = counter + 1
                 else:
                     continue
               
      return f"The string '{a_string}' contains {counter} palindrome substrings."
