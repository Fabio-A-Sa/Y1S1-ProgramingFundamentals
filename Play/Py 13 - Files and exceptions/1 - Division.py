# Created on January, 2021
# @author: Fábio Araújo de Sá

def division(a, b):

    try:
        number = a/b
        return "{}/{} = {}".format(a, b, number)

    except ZeroDivisionError:
        return "can't divide by 0!"
        
    except TypeError:
        return "unsupported operand type(s) for division"
