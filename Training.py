def split_odd_and_even(n):
    
    numbers = str(n)
    alist = []

    string = numbers[0]
    for number in numbers[1:]:  
    
        if int(number) % 2 == int(string) % 2:
            string += number
        else:
            alist.append(string)
            string = number
    
    alist.append(string)
    solution = list([int(x) for x in alist])
    return solution
    
print(split_odd_and_even(123))