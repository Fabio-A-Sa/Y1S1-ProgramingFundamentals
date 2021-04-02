def next_bigger(n):

    from itertools import permutations

    numbers = []
    for number in str(n):
        numbers.append(str(number))

    all_cases = list(permutations(numbers))
    new_numbers = []
    for pair in all_cases:
        string = ""
        for item in pair:
            string = string + item
        new_numbers.append(int(string))

    new_numbers = sorted(new_numbers, key = lambda x : x)
    for number in new_numbers:
        if number > n:
            return number

n = 2021
print(next_bigger(n))