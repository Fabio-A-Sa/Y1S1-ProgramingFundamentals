# Created on January, 2021
# @author: Fábio Araújo de Sá

def longest_prefix(words):

    if len(words) == 1:
        return words[0]
    
    else:

        words.sort()
        cobaia = words[0]

        for i in range(len(words)):
            if cobaia not in words[i]:
                cobaia = cobaia[:len(cobaia)-1]
            else:
                continue


        return cobaia
