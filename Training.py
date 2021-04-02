def top_3_words(text):

    def normalize (alist):  

        normal = []
        forbiden = "#$%&()*+,-./:;<=>?@[\]^_`{|}~"

        for word in alist:
            more = ""
            for char in word:
                if char not in forbiden and char != "" and char != "\n":
                    more = more + char
                else:
                    continue

            normal.append(more)

        return normal

    trash = text.split(" ")
    words = normalize(trash)

    dictionary = {}
    for word in words:
        if word in dictionary.keys():
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = dictionary.get(word, 0) + 1

    solution = []
    sorted_values = sorted(dictionary.values())[::-1]
    sorted_dict = {}

    counter = 0
    for x in sorted_values:
        for y in dictionary.keys():
            if dictionary[y] == x:
                solution.append(y)
                counter += 1
                if counter == 3 and len(dictionary.keys()) >= 3:
                    return solution
    else:
        if len(sorted_dict.keys()):
            for key in sorted_dict.keys():
                solution.append(key)    

    return solution

text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

print(top_3_words(text))