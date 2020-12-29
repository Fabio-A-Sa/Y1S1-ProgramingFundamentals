# Created on November, 2020
# @author: Fábio Araújo de Sá

def sort_rule(item):
    return (100 - max(item[1]), len(item[1]), item[0])


def sort_leaders(records):
    return tuple(sorted(records, key=sort_rule, reverse=False))

# records = (('João', (80, 90, 100)), ('Ana', (90, 100)), ('José',
# (100,)), ('Ana', (50, 90)), ('Rui', (50, 90)))
# print(sort_leaders(records))
