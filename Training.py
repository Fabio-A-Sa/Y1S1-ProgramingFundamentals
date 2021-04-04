def comp(array1, array2):

    if len(array1) != len(array2) or array1 == None or array2 == None or not len(array1) * len(array2):
        return False
    
    from math import pow, sqrt
    flag = True
    for number in array1:
        flag = pow(number, 2) in array2 and flag
    
    for number in array2:
        try:
            flag = sqrt(number) in array1 and flag 
        except:
            return false

    return flag
	