# Created on October, 2020
# @author: Fábio Araújo de Sá

def logic(s, operations):
    
    for key in operations.keys():
        set_local = operations[key]
        
        if len(set_local) > len(s):
            
            if key == 'and':
                s = set_local.intersection(s)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = set_local.difference(s)
                
            else: # key == "xor"
                s = set_local ^ s
                
        else:
            
            if key == 'and':
                s = s.intersection(set_local)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = s.diference(set_local)
                
            else: # key == "xor"
                s = set_local ^ s           
        
    return s
