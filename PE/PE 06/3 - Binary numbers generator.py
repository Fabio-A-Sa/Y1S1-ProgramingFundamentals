# Created on April, 2021
# @author: Fábio Araújo de Sá

from math import pow

def decimal_to_binary (number):

    string = ""
    while (number):
        aux = number % 2
        number = (number - aux) // 2
        string = str(aux) + string

    return int(string) 

def binary_to_decimal (number):

    total = 0
    power = 0
    while (number):

        last_digit = number % 10
        total = total + last_digit * pow(2, power)
        power += 1
        number = number // 10

    return int(total)

def binary_range(start, end):

    solution = [start]
    min_number = binary_to_decimal(start) + 1
    max_number = binary_to_decimal(end)

    for number in range (min_number, max_number):
        solution.append(decimal_to_binary(number))
    
    for number in solution:
        yield number

attemps = [[0, 101], [10, 111], [101, 1010], [10001, 11000]]
for attemp in attemps:
    start = attemp[0]
    end = attemp[1]
    print(binary_range(start, end))