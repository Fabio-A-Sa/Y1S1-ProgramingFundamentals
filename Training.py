from math import pow

def powers_of_two(n):
    
    powers = []
    while (n):
        powers.append(int(pow(2, n)))
        n = n - 1

    return powers[::-1]