# Created on January, 2021
# @author: Fábio Araújo de Sá

def brute_force(f, l):

    # For the resolution of the exercise I consulted how to make combinations using comprehensions. 
    # I found this site that helped me with the task:
    # https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
    
    from itertools import product as p

    n = len(l)
    all_combinations = list(p(l, repeat = 3))

    # Combinations whose length is equal to 3 using filter
    function = lambda j: len(j) == 3
    allowed_combinations = list(filter(function, all_combinations))

    # Join letters for string to login
    concatenated = ["".join(letters) for letters in allowed_combinations]

    # Which combinations are possible for login?
    possibilities = list([x for x in concatenated if f(x) == True])
    return possibilities
