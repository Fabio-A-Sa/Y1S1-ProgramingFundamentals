# Created on January, 2021
# @author: Fábio Araújo de Sá

def multiples_of7(n):

    if n < 0:
        return None

    if n == 0:
        return n

    else:
        # All multiples of 7 in nterval [0, n[ (n not include)
        all_possibilities = [x for x in range(0, n) if x%7 == 0]

        # Generator
        for item in all_possibilities:
            yield item
