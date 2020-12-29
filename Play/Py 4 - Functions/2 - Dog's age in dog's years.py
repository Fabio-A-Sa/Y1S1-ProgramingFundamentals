# Created on November, 2020
# @author: Fábio Araújo de Sá

def dogs(h_age):
    
    if h_age <= 2:
        d_age = h_age * 10.5
    else:
        d_age = 21 + 4*(h_age-2)
    
    
    return(d_age)
    
