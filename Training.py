def is_vow(inp):

    vowels =  {
                97: 'a', 
                101: 'e',
                105: 'i',
                111: 'o', 
                117: 'u',
              }
    
    exp = []
    for item in inp:
        if item in vowels.keys():
            item = vowels[item]
        exp.append(item)
        
    return exp