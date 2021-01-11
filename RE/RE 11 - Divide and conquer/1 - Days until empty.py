# Created on January, 2021
# @author: Fábio Araújo de Sá

def days_until_empty(C, l):
    
    dias_passados = 0
    agua_no_tanque = C

    while agua_no_tanque > 0:

        dias_passados = dias_passados + 1
        agua_no_tanque = C - dias_passados if agua_no_tanque + l >= C else agua_no_tanque + l - dias_passados
        
    return dias_passados
