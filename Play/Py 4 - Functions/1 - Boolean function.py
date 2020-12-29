# Created on November, 2020
# @author: Fábio Araújo de Sá

def validate(grade):
    value = (type(grade) == type(1) or type(grade) == type(1.5)) and (100 >= grade >= 0)
    # É verdadeiro se o número estiver entre 0 e 100 e se for int ou float
    return(value)
