def logical_calc(array, op):

    if op == "AND":
        FLAG = True
        for boolean in array:
            FLAG = FLAG and boolean

    elif op == "OR":
        FLAG = False
        for boolean in array:
            FLAG = FLAG or boolean

    else:
        if len(array) == 1:
            FLAG = array[0]
        elif len(array) == 2:
            FLAG = array[0] ^ array[1]  
        else:
            FLAG = array[0] ^ array[1]  
            for index in range (2, len(array)):
              FLAG = FLAG ^ array[index]
           
    return FLAG
