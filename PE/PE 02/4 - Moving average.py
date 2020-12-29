# Created on December, 2020
# @author: Fábio Araújo de Sá

def moving_average(alist, n):
    
    result = []
    
    if len(alist) < 3 or n < 3:
        return result
    
    else:
    
        nei = n//2
        for i in range(nei, len(alist)-nei):
            soma = 0
            for j in range(1, nei+1):  
                soma = soma + alist[i+j] + alist[i-j]
            average = round(soma/(nei*2), 2)    
            result.append(average)
            
        return result 
