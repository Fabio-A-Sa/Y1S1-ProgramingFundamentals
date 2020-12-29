# Created on December, 2020
# @author: Fábio Araújo de Sá

def rearrange(l):
    negative_numbers = list(filter(lambda x: x <= 0 , l))
    positive_numbers = list(filter(lambda y: y > 0, l))
    return negative_numbers + positive_numbers
