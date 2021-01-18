def combinations(alist):

    combinations = list([(x, y) for x in alist for y in alist if x != y])
    return combinations

def is_coliding(atuple):

    def A_B(atuple):

        # A is to the left of B
        ret_A = atuple[0]
        ret_B = atuple[1]

        first_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        second_condition = ret_A['y1'] in range (ret_B['y2'], ret_B['y1'])

        third_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        fourth_condition = ret_A['y2'] in range (ret_B['y2'], ret_B['y1'])

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    def B_A(atuple):

        # B is to the left of A
        ret_A = atuple[1]
        ret_B = atuple[0]

        first_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        second_condition = ret_A['y1'] in range (ret_B['y2'], ret_B['y1'])

        third_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        fourth_condition = ret_A['y2'] in range (ret_B['y2'], ret_B['y1'])

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    return A_B(atuple) or B_A(atuple)

def number_of_collisions(objects):

    prob_colisions = combinations(objects)

    total = 0
    for item in prob_colisions:

        if is_coliding(item):
            total = total + 1
        else:
            continue

    return total
