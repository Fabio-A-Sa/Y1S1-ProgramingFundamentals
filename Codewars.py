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

def choose_best_sum(t, k, ls):
    
    from itertools import permutations 

    possible_attemps = list(permutations(ls, k))
    total_sum = [sum(alist) for alist in possible_attemps if int(sum(alist)) <= t]
    maximum = max(total_sum)
    return maximum if maximum <= t else None
    
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
k = 4
t = 230
print(choose_best_sum(t, k, ls))

def counter (string, char):

    counter = 0
    for c in string:
        if c == char:
            counter = counter + 1
        else:
            continue
    return counter

def scramble(s1, s2):
    
    flag = True
    for char in s2:
        flag = flag and (counter(s1, char) >= counter(s2, char) and len(s1) >= len(s2))
        if not flag:
            break
    return flag

print(scramble('rkqodlw', 'world'))
print(scramble('mdhyenfeihyjm', 'pkdayaxhirdwqnfhe'))

def lcs (x, y):

    solution = ""
    big = x if len(x) >= len(y) else y
    small = x if big != x else y
    
    for char in big:
        if char in small:
            solution += char
    return solution

print(lcs( "132535365" , "123456789" ))

def to_underscore(string):

    from string import ascii_lowercase as abc
    ABC = abc.upper()
    words = []
    word = ""

    try:
        number = int(string)
        return str(number)

    except:
        
        for char in str(string):
            if char in abc:
                word = word + char
            elif char in ABC:
                words.append(word)
                word = char
            else:
                word += char
        words.append(word)
    
        solution = ""
        for word in words[1:]:
            solution += word.lower() + "_"

        return solution[:len(solution)-1]

print(to_underscore('TestController'))
print(to_underscore('App7Test'))

def isPP(n):
    
    from math import pow, sqrt
    solution = []

    for i in range (2, int(sqrt(n)+4)):
        for j in range(2, int(sqrt(n)+4)):

            if pow(i, j) == n:
                solution.append(i)
                solution.append(j)
                return solution

            if pow(i, j) > n:
                break
            
        else:
            continue

    return None

def factorial (n):

    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def iter_factorial(n):

    total = 1
    while (n > 1):
        total = total * n
        n = n-1

    return total

def going(n):
    
    denominator = iter_factorial(n)
    numerator = 0
    for number in range(1, n+1):
        numerator = numerator + iter_factorial(number)

    solution = str(numerator/denominator)
    return float(solution[:solution.find(".")+7])

print(going(7))

def find_it(seq):

    dictionary = {}

    for number in seq:
        if number not in dictionary.keys():
            dictionary[number] = dictionary.get(number, 0) + 1
        else:
            dictionary[number] += 1
    for number, times in dictionary.items():
        if times % 2 == 1:
            return number

    return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

def middle_permutation(string):
    
    from itertools import permutations

    letters = []
    for letter in string:
        letters.append(letter)

    possible_attemps = list(permutations(letters))
    middle = possible_attemps[int(round(len(possible_attemps) / 2 - 1))]
    solution = "".join(middle)

    return solution

print(middle_permutation("abc"))

def find_it(seq):

    dictionary = {}

    for number in seq:
        if number not in dictionary.keys():
            dictionary[number] = dictionary.get(number, 0) + 1
        else:
            dictionary[number] += 1
    for number, times in dictionary.items():
        if times == 1:
            return number

    return None

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
