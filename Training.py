def compute_sum(n):

    numbers = ""
    for number in range(1, n+1):
        numbers += str(number)
    total = 0
    for number in numbers:
        total += int(number)

    return total

print(compute_sum(12))