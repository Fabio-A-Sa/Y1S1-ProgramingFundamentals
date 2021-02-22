# Created on February, 2021
# @author: Fábio Araújo de Sá

def sum_sublists(lst):

    sum_lists = []

    pointer = 0
    index_max = len(lst[0])

    while pointer < index_max:

        total = 0
        for sublist in lst:
            total = total + sublist[pointer]

        sum_lists.append(total)
        pointer = pointer + 1

    return sum_lists

# alist = [[1, 2, 0], [2, 5, 0], [0, 1, 2]]
# print(sum_sublists(alist))