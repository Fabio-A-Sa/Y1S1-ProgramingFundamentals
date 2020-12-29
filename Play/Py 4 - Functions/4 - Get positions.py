# Created on November, 2020
# @author: Fábio Araújo de Sá

def get_positions(setence, word_list):
    
     sentence = setence.split()
     string_final = []
     
     for a in range(0, 2): # Words in sentence
          for b in range(0, 3): # Words in word_list
          
               if sentence[a] == word_list[b]:
                   string_final.append(b) # Add b value
                   break        
               
     if len(string_final) == 2: # Finish
        return str(string_final[0]) + " " + str(string_final[1])
    
     else:
        return "" # Nothing
