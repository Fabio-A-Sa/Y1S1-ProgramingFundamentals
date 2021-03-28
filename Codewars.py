# Code wars challenges using Python

def generate_hashtag(s):

    if len(s) == 0 or len(s) > 140:
        return False
    else:
        words = [word.capitalize() for word in s.split(" ") if word != " "]
        hastag = "#"
        for word in words:
            hastag += word

        return hastag

s = "    Hello     World   "
print(generate_hashtag(s))

