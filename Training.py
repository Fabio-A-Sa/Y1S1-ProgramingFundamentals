from string import ascii_uppercase, ascii_lowercase

def make_upper_case(s):

    solution = ""
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            solution += ascii_uppercase[index]
        else:
            solution += char
            
    return solution