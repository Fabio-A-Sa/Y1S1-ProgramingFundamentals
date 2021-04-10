def make_sentences(parts):
    
    alist = list([x for x in parts if x != "."]) + ['.']
    sentence = alist[0]

    for word in alist[1:]:  
        if word != '.' and word != ',':
            sentence += " " + word
        else:
            sentence += word
    return sentence

sentence = ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.']
print(make_sentences(sentence))