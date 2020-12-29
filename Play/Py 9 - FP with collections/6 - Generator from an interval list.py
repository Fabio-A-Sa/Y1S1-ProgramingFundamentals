# Created on December, 2020
# @author: Fábio Araújo de Sá

def generator(intlist):
    numbers = []
    for item in intlist:
        (início, fim) = item
        numbers = numbers + [x for x in range(início, fim+1)]
    for n in numbers:
        yield n
