# Created on November, 2020
# @author: Fábio Araújo de Sá

def ajustes(result):
    
    result = result[1::] # retira a primeira vírgula
    new_list = result.split(",") # lista com itens do tipo "n->m" ou "n->n"
    final = ""
    
    for x in range (0, len(new_list)):
        
        y = round((len(new_list[x])-2)/2) # número de dígitos de n
        
        if new_list[x][:y] == new_list[x][-y:]: #significa que n->n
            new_list[x] = new_list[x][0:y] #substitui por n
            
        else:
            continue
        
    for z in range(0, len(new_list)):  
        final = final + "," + new_list[z]
        
    return final[1::] # retira a primeira vírgula

            
def summary_ranges(a_string):
    
    vazio = ""
    
    if a_string == "":
        return vazio
    
    if len(a_string) == 1:
        return a_string
    
    a_list = a_string.split(",")
    result = ""
    
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while (i < len(a_list)+1) or ((i+j+1) < len(a_list)):
    
        while ((int(a_list[i+j]) - int(a_list[i])) == j):
            if (i+j) == (len(a_list)-1):
                result = result + "," + str(a_list[i]) + "->" + str(a_list[i+j])
                
                return ajustes(result) # chama a outra função que irá retirar a 
                                       # primeira vírgula e substituir casos 
                                       # do tipo "n->n" por "n"
            else:
                j = j + 1
        
        else:
            result = result + "," + str(a_list[i]) + "->" + str(a_list[i+(j-1)])
            i = i + j
            j = 0 # cancel complement

# a_string = str(input("qualquer coisa"))
# print(summary_ranges(a_string))
