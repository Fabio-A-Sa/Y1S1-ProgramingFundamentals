# Created on April, 2021
# @author: Fábio Araújo de Sá

def find_min(numbers):

    index = 0
    min_number = 10000000000000000

    for i in range(len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
            index = i

    return index

attemps = [[10, 1, 2, 10], [1, 2, 10, 1], [3, 3, -2, 1], [3]]
for attemp in attemps:
    print(find_min(attemp))