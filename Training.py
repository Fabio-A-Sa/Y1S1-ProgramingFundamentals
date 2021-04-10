def make_a_window(num): 
    
    begin = (3 + 2 * num) * '-' + '\n'
    end = (3 + 2 * num) * '-'
    middle = '|' + num * '-' + '+' + num * '-' +  '|' + '\n'
    static = '|' + num * '.' + '|' + num * '.' + '|' + '\n'

    print(begin + num*static + middle + num*static + end)


print(make_a_window(10))