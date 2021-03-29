def find_it(seq):

    dictionary = {}

    for number in seq:
        if number not in dictionary.keys():
            dictionary[number] = dictionary.get(number, 0) + 1
        else:
            dictionary[number] += 1
    for number, times in dictionary.items():
        if times % 2 == 1:
            return number

    return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))