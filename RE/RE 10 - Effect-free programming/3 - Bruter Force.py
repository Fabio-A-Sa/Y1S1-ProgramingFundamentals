# Created on January, 2021
# @author: Fábio Araújo de Sá

def brute_force(f, l):

    # All combinations whose lenght is 3 and not (x == y or x == z or z == y)
    all_combinations = list([(x, y, z) for x in l for y in l for z in l])
    concatenated= list(["".join(possibility) for possibility in all_combinations])

    # Filter with the function f
    result = list([possibility for possibility in concatenated if f(possibility) == True])

    return result
