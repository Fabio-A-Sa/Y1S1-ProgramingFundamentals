def two_sort(array):

    array = sorted(array, key = lambda x : str(x))
    word = array[0]
    solution = ""
    for letter in word:
        solution = solution + letter + "***"

    return solution[:len(solution)-3]

print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))