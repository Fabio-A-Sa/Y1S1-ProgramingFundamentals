def find_it(seq):

    d = {}
    for item in seq:
        if item not in d.keys():
            d[item] = d.get(item, 0) + 1
            
    solution = 0
    for key in d:
        if (d[key])%2 == 1:
            solution = key
            break
    return solution