# Created on November, 2020
# @author: Fábio Araújo de Sá

def rotate_list(l):
    
    final = l.copy()
    [x,y,z] = l[0:3]
    final.remove(x)
    final.remove(y)
    final.remove(z)
    
    final.append(x)
    final.append(y)
    final.append(z)
        
    return final
