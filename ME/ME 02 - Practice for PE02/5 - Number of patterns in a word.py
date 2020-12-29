# Created on November, 2020
# @author: Fábio Araújo de Sá

def is_pattern(astring):
    
    net = 0
    for i in range(len(astring)-1):
        if astring[i+1] > astring[i]:
            net += 1
        if astring[i+1] < astring[i]:
            net -= 1

    return net == 0


def subpatterns(astring):
    
    counter = 0

    for step in range(2, len(astring) + 1):
    
        for char_index in range(0, len(astring) - step + 1):
    
            sub_str = astring[char_index:char_index+step]
            if is_pattern(sub_str):
                counter += 1
            else:
                continue

    return f"The string '{astring}' contains {counter} substring patterns."
