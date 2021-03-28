

def counter (string, char):

    counter = 0
    for c in string:
        if c == char:
            counter = counter + 1
        else:
            continue
    return counter

def scramble(s1, s2):
    
    flag = True
    for char in s2:
        flag = flag and (counter(s1, char) >= counter(s2, char))
    return flag

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))