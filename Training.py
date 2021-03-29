def find_it(seq):

    dictionary = {}

    for number in seq:
        if number not in dictionary.keys():
            dictionary[number] = dictionary.get(number, 0) + 1
        else:
            dictionary[number] += 1
    for number, times in dictionary.items():
        if times == 1:
            return number

    return None
