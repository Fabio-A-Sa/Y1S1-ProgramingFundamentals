def multiples_of7(n):

    for x in range(n):
        if x%7 == 0:
            # Generator
            yield x
