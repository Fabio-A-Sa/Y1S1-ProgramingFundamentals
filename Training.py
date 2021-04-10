def to_binary (number):

    string = ""
    while (number):

        aux = number % 2
        string = str(aux) + string
        number = (number - aux) // 2

    return string

def swap(s,n):

    binary = to_binary(n)
    while (len(binary) < len(s)):
        binary += binary
    
    keys = ""
    key_counter = 0
    for i in range(len(s)):
        if s[i] == " ":
            keys += " "
        else:
            keys += binary[key_counter]
            key_counter += 1

    solution = ""
    for index in range(len(s)):

        letter = s[index]
        if keys[index] == '1':
            letter = letter.swapcase()
        solution += letter

    print(keys)
    print(s)
    print(solution)
    return solution

print(swap('the quick broWn fox leapt over the fence', 11))