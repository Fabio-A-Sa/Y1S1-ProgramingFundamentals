# Created on October, 2020
# @author: Fábio Araújo de Sá

def matriz_resultado(linhas, colunas):
    # Criação de uma matriz com um número certo de "casas" para preencher
    
    result = []
    while len(result) < linhas:
        result.append([])
        while len(result[-1]) < colunas:
            result[-1].append([])
 
    return result


def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    return (b == c)


def mult(M, N):

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        result = matriz_resultado(a, d)
        for i in range(a):
            for j in range(d):
                total = 0
                for k in range(b):
                    total = total + M[i][k] * N[k][j]
                result[i][j] = total
                
        return result
     
    else:
        return []
