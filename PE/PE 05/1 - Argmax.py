# Created on February, 2021
# @author: Fábio Araújo de Sá

def argmax1(lst):
    return (lst.index(max(lst)))

def argmax2(lst):

    maior = -10000000
    for number in lst:
        if number > maior:
            maior = number

    for index in range(len(lst)):
        if maior == lst[index]:
            return index
        index = index + 1

    return None

alist = [1, 10, 1, 2, 10]
print(argmax2(alist))