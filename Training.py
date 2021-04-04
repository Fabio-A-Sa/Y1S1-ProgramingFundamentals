
def order(sentence):

    def sort_rule (pair):
        return pair[1]

    all_pairs = []
    words = sentence.split(" ")
    for word in words:
        number = 0
        for char in word:
            try:
                number = int(char)
            except:
                continue
        all_pairs.append((word, number))

    pairs = sorted(all_pairs, key = sort_rule)

    solution = ""
    for pair in pairs:
        solution += pair[0] + " "

    return solution.strip()

print(order("4of Fo1r pe6ople g3ood th5e the2"))