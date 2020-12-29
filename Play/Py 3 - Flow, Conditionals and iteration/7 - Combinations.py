# Created on October, 2020
# @author: Fábio Araújo de Sá

def C(n,r):
    
    n_result = 1
    r_result = 1
    n_menos_r_result = 1
    
    for i in range(1, n+1):
        n_result = n_result*i
    
    for i in range(1, r+1):
        r_result = r_result*i
    
    for i in range (1, (n-r)+1):
        n_menos_r_result = n_menos_r_result*i
    
    combination = n_result/ (r_result*n_menos_r_result)
    
    return(round(combination))
