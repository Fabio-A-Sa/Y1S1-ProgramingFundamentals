def spin_words(sentence):

    words = sentence.split(" ")
    solution = ""
    for word in words:
        if len(word) < 5:
            solution += word + " "
        else:
            compound = ""
            for char in word:
                compound = char + compound
            solution += word + " "
    
    return solution.strip()