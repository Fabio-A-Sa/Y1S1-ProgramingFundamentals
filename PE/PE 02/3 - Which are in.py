# Created on December, 2020
# @author: Fábio Araújo de Sá

def which_are_in(l1, l2):

    result = []

    for item1 in l1:
        for item2 in l2:
            if item1 in item2:
                if item1 not in result:
                    result.append(item1)

    return sorted(result)