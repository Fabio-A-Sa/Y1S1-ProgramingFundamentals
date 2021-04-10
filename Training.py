def inside_out(st):
    
    alist = list([x for x in st.split(" ")]) if len(st) > 1 else [st]
    string = ""

    for word in alist:
        
        result = ""

        if len(word) % 2 == 0:

            left_characters = [word[x] for x in range(0, int(len(word) / 2))]
            right_characters = [word[y] for y in range(int(len(word) / 2), len(word))]

            for char in left_characters[::-1]:
                result += char
            for char in right_characters[::-1]:
                result += char

        else:
            
            if len(word) > 1:

                lose_character = word[int(len(word) / 2)]
                left_characters = [word[x] for x in range(0, int(len(word) / 2))]
                right_characters = [word[y] for y in range(int(len(word) / 2) + 1, len(word) )]

                for char in left_characters[::-1]:
                    result += char
                result += lose_character
                for char in right_characters[::-1]:
                    result += char
            
            else:
                result = word

        string += result + " "

    if st[0] == " " and st[len(st)-1] == " ":
        string = " " + string
        
    elif st[0] != " " and st[len(st)-1] == " ":
        string = " " + string

    elif st[0] == " " and st[len(st)-1] != " ":
        string = " " + string[::len(str)-2]

    else:
        continue

    return string

print(inside_out('what time are we climbing up the volcano'))