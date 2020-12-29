# Created on October, 2020
# @author: Fábio Araújo de Sá

def calculator(expr):
    
    if type(expr) == type(1): #Se for um inteiro
        return expr
    
    else:
        
        seguinte = expr[1] # Se houver mais tuples
        
        if seguinte == '+': # Soma
            return calculator(expr[0]) + calculator(expr[2])
        
        elif seguinte == '*': # Multiplicação
            return calculator(expr[0]) * calculator(expr[2])
        
        elif seguinte == '-': # Subtração
            return calculator(expr[0]) - calculator(expr[2])
