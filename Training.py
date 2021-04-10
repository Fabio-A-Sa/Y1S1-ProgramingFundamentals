def decipher_message(message):
    
    from math import sqrt
    qtd = int(sqrt(len(message)))
    
    square = []
    line = ""
    for letter in message:
        line += letter
        if len(line) == qtd:

            chars = []
            for char in line:
                chars.append(char)

            line = ""
            square.append(chars)

        else:
            continue

    solution = ""
    counter = 0

    while (counter != qtd):

        for chars in square:
            solution += chars[counter]
        counter = counter + 1
 
    print(solution)        

print(decipher_message('ArNran u rstm5twob  e ePb'))