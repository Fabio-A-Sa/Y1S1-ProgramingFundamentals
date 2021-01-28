# Created on January, 2021
# @author: Fábio Araújo de Sá

def get_composites(n):

    all_numbers = [x for x in range(4, n+1)]
    primes_until_n = [y for y in all_numbers if all( y % z != 0 for z in range(2, y))]
    composites_filter = lambda c: c not in primes_until_n

    result = filter(composites_filter, all_numbers)

    # Genetator
    for number in list(result):
        yield number
