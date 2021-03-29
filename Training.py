def middle_permutation(string):
    
    from itertools import permutations

    letters = []
    for letter in string:
        letters.append(letter)

    possible_attemps = list(permutations(letters))
    middle = possible_attemps[int(round(len(possible_attemps) / 2 - 1))]
    solution = "".join(middle)

    return solution

print(middle_permutation("abc"))
