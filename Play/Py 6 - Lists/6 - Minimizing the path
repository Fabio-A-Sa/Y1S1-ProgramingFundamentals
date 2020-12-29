# Created on November, 2020
# @author: Fábio Araújo de Sá

def min_path(path):

    i = 0
    j = len(path)

    while i < j-1:
        
        if (path[i] == "RIGHT" and path[i+1] == "LEFT") or (path[i] == "LEFT" and path[i+1] == "RIGHT"):
            path.remove(path[i])
            path.remove(path[i])
            i = 0
            j = j - 2
            
        elif (path[i] == "UP" and path[i+1] == "DOWN") or (path[i] == "DOWN" and path[i+1] == "UP"):
            path.remove(path[i])
            path.remove(path[i])
            i = 0
            j = j - 2
             
        else:
            i = i + 1
            continue
            
    return path
