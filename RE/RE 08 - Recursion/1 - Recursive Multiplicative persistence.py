# Created on October, 2020
# @author: Fábio Araújo de Sá

def rec_multiplicative_persistence(n):
    
    if len(str(n)) == 1:
        return 0
    else:
        passo_seguinte = retira_numeros(n)
        return 1 + rec_multiplicative_persistence(passo_seguinte)

def retira_numeros(n):
    
    if len(str(n)) == 1:
        return n
    else:
        return n%10 * retira_numeros(n//10)
