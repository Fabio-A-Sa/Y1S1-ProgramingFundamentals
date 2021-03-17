# Part 1 -> Decrypt message using a = 0 until j = 9

def decrypt1 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str(abc.find(caracter)))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    numbers = []
    for par in message.split(" "):

        try:
            numbers.append(float(par))
            print(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

    print("Total = {}\nPrimeira parte = {}\nSegunda Parte = {}".format(round(total_1 + total_2, 3), round(total_1, 3), round(total_2, 3)))

    return numbers

def decrypt2 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str((abc.find(caracter)+1)%10))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    numbers = []
    for par in message.split(" "):

        try:
            print(float(par))
            numbers.append(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

    print("Total = {}\nPrimeira parte = {}\nSegunda Parte = {}".format(round(total_1 + total_2, 3), round(total_1, 3), round(total_2, 3)))

    return numbers

def get_coordinates ( alist ) :

    possibilities = []


    return

code = "bch.ga dc.ag bia.jeh bf.jjj hc.gda bf.jjj ea.ahi bc.abb b.aai bbe.ibi gj.hcd cg.jib bcg.jae he.jcb + eh.igh fi.jdd"
numbers = decrypt1(code)
print(get_coordinates(numbers))

 

