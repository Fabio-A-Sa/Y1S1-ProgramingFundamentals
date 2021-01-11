# Created on January, 2021
# @author: Fábio Araújo de Sá

def find_me(f, limits):


    all_numbers = list([x for x in range(limits[0], limits[1])]) if type(limits) is tuple else limits
    n = len(all_numbers)//2

    left = all_numbers[:n]
    right = all_numbers[n:]

    if f(all_numbers[n]) == 0:
        # Found it!
        return 1
    
    if f(right[0]) == -1:
        return 1 + find_me(f, left)

    # Else
    return 1 + find_me(f, right)
