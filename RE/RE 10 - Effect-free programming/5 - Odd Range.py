# Created on January, 2021
# @author: Fábio Araújo de Sá

def odd_range(start, stop, step):

    # First odd number in range (start, stop)
    number = 0
    for i in range(start, stop):
        if i%2 == 1: # Odd number
            number = i
            break
    
    # Steps until stop
    step = 2 * step
    result = []
    for n in range(number, stop, step):
        result.append(n)
    
    # Generator
    for item in result:
        yield item
