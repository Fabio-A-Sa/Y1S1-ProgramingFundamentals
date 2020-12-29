# Created on October, 2020
# @author: Fábio Araújo de Sá

def manipulator(l, cmds):
    
    result = "" # Empty string
    
    for instruction in cmds:
        
        instruction = instruction.split(" ") # list com a instrução separada
                                             # dos números pretendidos
        
        if instruction[0] == "insert":
            l.insert(int(instruction[1]), int(instruction[2]))
        
        elif instruction[0] == "remove":
            l.remove(int(instruction[1]))
        
        elif instruction[0] == "append":
            l.append(int(instruction[1]))
            
        elif instruction[0] == "sort":
            l.sort()

        elif instruction[0] == "pop":
            l.pop()
            
        elif instruction[0] == "reverse":
            l.reverse()
            
        elif instruction[0] == "print":
            result = result + str(l) + " "
    
    result.rstrip(" ") # Delete a last space 
    return result
