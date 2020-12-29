# Created on December, 2020
# @author: Fábio Araújo de Sá

def map_filter_reduce(lst, f1, f2, f3):
    from functools import reduce as r
    return int(r(f3, list(map(f2, list(filter(f1, lst))))))
