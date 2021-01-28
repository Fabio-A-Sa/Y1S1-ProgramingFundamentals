# Created on January, 2021
# @author: Fábio Araújo de Sá

def count_exceptions(f, n1, n2):

    counter = 0
    integers = list([x for x in range(n1, n2+1)])

    for number in integers:

        try:
            f(number)

        except: # Any error
            counter = counter + 1
            continue

    return counter
