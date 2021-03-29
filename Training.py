def binary_to_decimal(string):

    from math import pow
    exponent = 0
    decimal = 0

    while (exponent != len(string)):

        digit = int(string[exponent])
        decimal = decimal + pow(2, exponent)*digit
        exponent += 1

    return round(decimal)


def pattern (string):

    available = ['0', '1']
    number = ""
    for char in string:
        number = char + number
        if char not in available:
            return False

    decimal = binary_to_decimal(number)
    return decimal % 3 == 0

print(pattern("111"))