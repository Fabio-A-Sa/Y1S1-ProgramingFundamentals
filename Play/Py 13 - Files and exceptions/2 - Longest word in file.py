# Created on January, 2021
# @author: Fábio Araújo de Sá

def longest(filename):

    longest_word = []
    length = 0

    with open(filename, "r") as this_file:
        for line in this_file:
            search = line.split(" ")
            for word in search:
                if len(word) > length:
                    longest_word.append(word)
                    length = len(word)

    return longest_word[-1]
