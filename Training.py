def factorial (number) :

    if number == 1 or number <= 0:
        return 1
    else:
        return number * factorial (number-1)

def make_combination (n, r):

    result = int(factorial(n) / (factorial(n-r) * factorial(r)))
    return result

def get_participants(handshakes):

    if handshakes == 0:
        return 1
    elif handshakes == 1:
        return 2
    elif handshakes == 2:
        return 3
    else:

        counter = 3
        while (True):

            attemp = make_combination(counter, 2)
            if attemp >= handshakes:
                break
            else:
                counter += 1
        
        return counter

print(get_participants(6))