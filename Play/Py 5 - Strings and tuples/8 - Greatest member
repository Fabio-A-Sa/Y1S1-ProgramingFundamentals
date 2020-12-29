# Created on November, 2020
# @author: Fábio Araújo de Sá

def ascii_code(item):
    
    ascii_codea = 0 # initial
    
    for x in item:
        
        if type(item)==str:   
            ascii_codea = ascii_codea + ord(x)

        else:
            ascii_codea = ascii_codea + ascii_code(x)
            
    return ascii_codea

def greatest_member(a_tuple):
    result = []
    for i in a_tuple:
        result.append(ascii_code(i))
    return a_tuple[result.index(max(result))]

a_tuple = (('ab', 'dez', ('1',)), ('ab', 'de', ('1',)), 'defg', 'jkab')
print(greatest_member(a_tuple))
