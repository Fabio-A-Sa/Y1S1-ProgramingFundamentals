# Created on April, 2021
# @author: Fábio Araújo de Sá

def normalize(expr):

    if len(expr) == 1:
        return expr

    exp1, operator, exp2 = expr
    
    if type(exp1) == int and type(exp2) == int:
        return expr

    elif type(exp1) == int and type(exp2) == tuple and operator == '+':
        return exp1, operator, normalize(exp2)
    
    elif type(exp1) == int and type(exp2) == tuple and operator == '*':
        exp2 = normalize(exp2)
        return tuple([tuple((exp1, '*', exp2[0])), '+', tuple((exp1, '*', exp2[2]))])

    elif type(exp1) == tuple and type(exp2) == int and operator == '+':
        return normalize(exp1), operator, exp2
    
    elif type(exp1) == tuple and type(exp2) == int and operator == '*':
        exp1 = normalize(exp1)
        return tuple([tuple((exp1[0], '*', exp2)), '+', tuple((exp1[0], '*', exp2))])

    elif type(exp1) == tuple and type(exp2) == tuple and operator == '+':
        return normalize(exp1), operator, normalize(exp2)
    
    elif type(exp1) == tuple and type(exp2) == tuple and operator == "*":
        exp1 = normalize(exp1)
        exp2 = normalize(exp2)
        return tuple([tuple([tuple((exp1[0], '*', exp2[0])), '+', tuple((exp1[0], '*', exp2[2]))]), '+', tuple([tuple((exp1[2], '*', exp2[0])), '+', tuple((exp1[2], '*', exp2[2]))])])

    else:
        return None

attemps = [     (6, '*', (4, '+', 8)), 
                ((6, '+', 2), '*', (4, '+', 8)), 
                (4, '+', (6, '*', (3, '+', 2))), 
                (4, '+', (6, '*', ((3, '*', 1), '+', (2, '+', 5))))     ]

for attemp in attemps:
    print(normalize(attemp))