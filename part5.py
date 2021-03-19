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

# A = 0
m1 = to_letters(message1, 0)
m2 = to_letters(message2, 0)
m3 = to_letters(message3, 0)

def frequency (message):

    dictionary = {}
    for letter in message:
        if letter not in dictionary.keys():
            dictionary[letter] = dictionary.get(letter, 0) + 1
        else:
            dictionary[letter] += 1

    return dictionary

def sum_freqs (random):

    main_dict = {}



    return main_dict

a1 = [int(x) for x in sorted(message1.split("-"), key = lambda x: int(x))]
print(a1, sum(a1))
for item in a1:
    print(abc[item-0])

a2 = [int(x) for x in sorted(message2.split("-"), key = lambda x: int(x))]
print(a2, sum(a2))
for item in a2:
    print(abc[item-1])

a3 = [int(x) for x in sorted(message3.split("-"), key = lambda x: int(x))]
print(a3, sum(a3))
for item in a3:
    print(abc[item-1])

all_messages = [m1, m2, m3]
dicts = []
for message in all_messages:
    print(frequency(message))
    dicts.append(frequency(message))

print("\nTotal sum: {}".format(sum_freqs(dicts)))


