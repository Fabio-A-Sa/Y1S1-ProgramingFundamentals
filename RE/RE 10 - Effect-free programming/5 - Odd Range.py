# Created on January, 2021
# @author: Fábio Araújo de Sá

def odd_range(start, stop, step):

    # All odd numbers between start and stop
    numbers = [x for x in range(start, stop) if x%2 == 1]

    # Step increment
    total = len(numbers)
    odd_numbers = [numbers[index] for index in range(0, total, step)]

    # Generator
    for item in odd_numbers:
        yield item
