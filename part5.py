from string import ascii_uppercase as abc

instructions = "Para Santiago por vezes segue-se o azul e só depois o amarelo. Nas termas recupera-se melhor a cantar."

message1 = "9-13-1-6-21-18-9-19"
message2 = "19-9-13-15-4-1-12-9-19-21-9-19"
message3 = "12-9-18-9-19-1-12-15-4"

def to_letters(numbers, offset):

    astring = ""
    for number in numbers.split("-"):
        astring = astring + str(abc[int(number) - 1 + offset])

    return astring

# A == 1
m1 = to_letters(message1, 1) # JNBGVSJT
m2 = to_letters(message2, 1) # TJNPEBMJTVJT
m3 = to_letters(message3, 1) # MJSJTBMPE

# A == 0
m1 = to_letters(message1, 0) # IMAFURIS
m2 = to_letters(message2, 0) # SIMODALISUIS
m3 = to_letters(message3, 0) # LIRISALOD

def frequency (message):

    dictionary = {}
    for letter in message:
        if letter not in dictionary.keys():
            dictionary[letter] = dictionary.get(letter, 0) + 1
        else:
            dictionary[letter] += 1

    return dictionary

def sum_freqs (rd):

    main_dict = {}
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = 0
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = main_dict[key] + dictionary[key]

    return main_dict

a1 = [int(x) for x in sorted(message1.split("-"), key = lambda x: int(x))]
print(a1, sum(a1))

a2 = [int(x) for x in sorted(message2.split("-"), key = lambda x: int(x))]
print(a2, sum(a2))

a3 = [int(x) for x in sorted(message3.split("-"), key = lambda x: int(x))]
print(a3, sum(a3))

all_messages = [m1, m2, m3]
dicts = []
for message in all_messages:
    print(frequency(message))
    # {'I': 2, 'M': 1, 'A': 1, 'F': 1, 'U': 1, 'R': 1, 'S': 1}
    # {'S': 3, 'I': 3, 'M': 1, 'O': 1, 'D': 1, 'A': 1, 'L': 1, 'U': 1}
    # {'L': 2, 'I': 2, 'R': 1, 'S': 1, 'A': 1, 'O': 1, 'D': 1}
    dicts.append(frequency(message))

print("\nTotal sum: {}".format(sum_freqs(dicts)))
# Total sum: {'I': 7, 'M': 2, 'A': 3, 'F': 1, 'U': 2, 'R': 2, 'S': 5, 'O': 2, 'D': 2, 'L': 3}


