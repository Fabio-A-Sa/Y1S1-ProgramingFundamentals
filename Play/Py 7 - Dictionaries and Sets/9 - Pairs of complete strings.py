# Created on December, 2020
# @author: Fábio Araújo de Sá

def complete_pairs(s1, s2):
    
    from string import ascii_lowercase as abc
    solution = []
    
    for string_1 in s1:
        for string_2 in s2:
            a_string = string_1 + string_2
            if set(abc) < set(a_string) or set(a_string) == set(abc):
                solution.append(a_string)
    
    solution = set(solution)
    return solution
