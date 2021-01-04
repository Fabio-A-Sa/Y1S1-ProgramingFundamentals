# Created on January, 2021
# @author: Fábio Araújo de Sá

def comprehensions(i, j):

    # To get all numbers, including j
    j = j + 1
    from math import sqrt as r

    first_part = [x for x in range(i, j) if (((str(x))[-1] == "8") or ((str(x))[-1] == "3"))]
    second_part = [round((r(x)),2) for x in range(i, j)]
    third_part = {x: chr(x) for x in range(i, j)}

    return tuple((list(first_part), tuple(second_part), dict(third_part)))
