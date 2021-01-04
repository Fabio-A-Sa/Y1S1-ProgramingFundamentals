# Created on January, 2021
# @author: Fábio Araújo de Sá

def rearrange(l):
    negative_numbers = list((x for x in l if x <= 0))
    positive_numbers = list((x for x in l if x > 0))

    return negative_numbers + positive_numbers
