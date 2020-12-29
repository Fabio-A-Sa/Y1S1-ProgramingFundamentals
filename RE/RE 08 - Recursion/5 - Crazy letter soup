# Created on October, 2020
# @author: Fábio Araújo de Sá

def letras(matrix, x, y, word):
    
    não_continua = True
    
    if matrix[x][y] == word[0]:
        
        if len(word) == 1:
            return não_continua # Acaba aqui
        
        else:
            
            vizinhança_procurada = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
            
            for (z, t) in vizinhança_procurada:
                
                if matrix[z][t] == word[1] and z >= 0 and t >=0:
                    return não_continua and letras(matrix, z, t, word[1:])
                else:
                    continue
                
                
def coordenadas(x, y):
    
    from string import ascii_letters as abc
    
    coordenada_x = abc[x]
    coordenada_y = y + 1
    
    return f"{coordenada_x}{coordenada_y}"


def soup(matrix, word):
    
    n_linhas = len(matrix)
    n_colunas = len(matrix)
    
    for x in range(n_linhas): 
        for y in range(n_colunas):  
            if letras(matrix, x, y, word): # Se encontrar a palavra pretendida
                
                return coordenadas(x, y).upper()
