def mixed_fraction(s):
    
    from math import gcd
    numbers = [int(x) for x in s.split("/")]

    try:

        r = numbers[0] // numbers[1]
        numbers[0] = numbers[0] - r * numbers[1]
        divisor = gcd(numbers[0], numbers[1])
        numbers[0] = round(numbers[0] / divisor)
        numbers[1] = round(numbers[1] / divisor)

        if numbers[0] * numbers[1] > 0:
            numbers[0] = abs(numbers[0])
            numbers[1] = abs(numbers[1])
            solution = "{} {}/{}".format(str(r), str(numbers[0]), str(numbers[1]))

        elif numbers[0] * numbers[1] == 0:
            solution = "{}".format(str(r))

        elif r == 0:
            solution = "{}/{}".format(str(numbers[0]), str(numbers[1]))

        return solution
        
    except ZeroDivisionError:
        raise ZeroDivisionError


print(mixed_fraction("42/9"))
