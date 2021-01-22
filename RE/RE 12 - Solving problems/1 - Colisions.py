  
# Created on January, 2021
# @author: Fábio Araújo de Sá

def combinations(alist):

    combinations = list([(x, y) for x in alist for y in alist if x != y])
    return combinations

def is_coliding(atuple):

    ret_A = atuple[0]
    ret_B = atuple[1]

    # If XXs are not close
    answer1 = ret_A['x2'] < ret_B['x1'] or ret_A['x1'] > ret_B['x2'] 

    # If YYs are not close
    # In programming the YYs grow down!
    answer2 = ret_B['y1'] > ret_A['y2'] or ret_A['y1'] > ret_B['y2'] 

    return not (answer1 or answer2)

def number_of_collisions(objects):

    prob_colisions = combinations(objects)

    total = 0
    for item in prob_colisions:

        if is_coliding(item):
            total = total + 1
        else:
            continue
    
    # Duplicate elimination
    answer = total // 2
    return answer
