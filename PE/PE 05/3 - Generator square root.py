# Created on February, 2021
# @author: Fábio Araújo de Sá

def sqrt(num, k):

    answer_list = []
    auxiliar = num
    delta = 100

    # List constructor
    initial = auxiliar / 2
    answer_list.append(initial)
    while len(answer_list) != k:

        next = (initial + auxiliar/initial)/2
        answer_list.append(round(next, 2))
        delta = initial - next
        initial = next
        if delta > 0.0001:
            continue

    # Generator
    for number in answer_list:
        yield number


# num = 20
# k = 6
# print(sqrt(num, k)) 