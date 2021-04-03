def reverse_seq(n):
    return [x for x in range(1, n+1)][::-1]

print(reverse_seq(5))

def remove_exclamation_marks(s):
    return s.replace("!", "")