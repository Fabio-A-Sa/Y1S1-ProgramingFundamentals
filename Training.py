dict =  {    
            0:0, 
            1:1, 
            2:1,
        }
def fibonacci(n):

    if n in dict.keys():
        return dict[n]
    else:
        dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return dict[n]

print(fibonacci(50))