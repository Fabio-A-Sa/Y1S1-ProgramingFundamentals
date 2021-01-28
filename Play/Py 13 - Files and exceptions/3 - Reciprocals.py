# Created on January, 2021
# @author: Fábio Araújo de Sá

def reciprocals(alist):

    answer = []

    for item in alist:

        try:
            number = 1/item
            answer.append(round(number, 3))
        
        except TypeError:
            continue
            
        except ZeroDivisionError:
            continue

    return answer
