from string import ascii_lowercase as abc

def score(word):

    score = 0
    for char in word:
        score = score + int(abc.find(char)+1)
    return score

def high(x):
    
    words = [x for x in x.lower().split(" ")]
    max_word = ""
    max_score = 0

    for word in words:

        max_word = word if score(word) > max_score else max_word
        max_score = score(word) if score(word) > max_score else max_score

    return max_word


print(high('what time are we climbing up the volcano'))