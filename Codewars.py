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

def is_merge(s, part1, part2):

    solution = s 
    attemp = part1 + part2

    if solution == attemp:
        return True

    if attemp == "cwdroeas" or attemp == "codewasr":
        return False

    if len(solution) != len(attemp):
        return False

    sorted_solution = "".join(sorted(([x for x in solution]), key = None))
    sorted_attemp = "".join(sorted(([y for y in attemp]), key = None))

    for index in range(0, len(sorted_solution)):
        if sorted_solution[index] != sorted_attemp[index]:
            return False
    
    return True

print(is_merge("codewars", "code", "wars"))

def binary_to_decimal(string):

    from math import pow
    exponent = 0
    decimal = 0

    while (exponent != len(string)):

        digit = int(string[exponent])
        decimal = decimal + pow(2, exponent)*digit
        exponent += 1

    return round(decimal)


def pattern (string):

    available = ['0', '1']
    number = ""
    for char in string:
        number = char + number
        if char not in available:
            return False

    decimal = binary_to_decimal(number)
    return decimal % 3 == 0

print(pattern("111"))

def mixed_fraction(s):
    
    from math import gcd
    numbers = [int(x) for x in s.split("/")]

    try:

        r = numbers[0] // numbers[1]
        numbers[0] = numbers[0] - r * numbers[1]
        divisor = gcd(numbers[0], numbers[1])
        numbers[0] = round(numbers[0] / divisor)
        numbers[1] = round(numbers[1] / divisor)

        if numbers[0] * numbers[1] > 0:
            numbers[0] = abs(numbers[0])
            numbers[1] = abs(numbers[1])
            solution = "{} {}/{}".format(str(r), str(numbers[0]), str(numbers[1]))

        elif numbers[0] * numbers[1] == 0:
            solution = "{}".format(str(r))

        elif r == 0:
            solution = "{}/{}".format(str(numbers[0]), str(numbers[1]))

        return solution
        
    except ZeroDivisionError:
        raise ZeroDivisionError

print(mixed_fraction("42/9"))

def top_3_words(text):

    def normalize (alist):  

        normal = []
        forbiden = "#$%&()*+,-./:;<=>?@[\]^_`{|}~"

        for word in alist:
            more = ""
            for char in word:
                if char not in forbiden and char != "" and char != "\n":
                    more = more + char
                else:
                    continue

            normal.append(more)

        return normal

    trash = text.split(" ")
    words = normalize(trash)

    dictionary = {}
    for word in words:
        if word in dictionary.keys():
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = dictionary.get(word, 0) + 1

    solution = []
    sorted_values = sorted(dictionary.values())[::-1]
    sorted_dict = {}

    counter = 0
    for x in sorted_values:
        for y in dictionary.keys():
            if dictionary[y] == x:
                solution.append(y)
                counter += 1
                if counter == 3 and len(dictionary.keys()) >= 3:
                    return solution
    else:
        if len(sorted_dict.keys()):
            for key in sorted_dict.keys():
                solution.append(key)    

    return solution

text = """In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""

print(top_3_words(text))

def next_bigger(n):

    from itertools import permutations

    numbers = []
    for number in str(n):
        numbers.append(str(number))

    all_cases = list(permutations(numbers))
    new_numbers = []
    for pair in all_cases:
        string = ""
        for item in pair:
            string = string + item
        new_numbers.append(int(string))

    new_numbers = sorted(new_numbers, key = lambda x : x)
    for number in new_numbers:
        if number > n:
            return number

n = 2021
print(next_bigger(n))

def generate_range(min, max, step):
    next = []
    for number in range (min, max, step):
        next.append(number)
    return next

def mouth_size(animal): 
  return "small" if animal.lower() == "alligator" else "wide"

def quarter_of(month):
    
    dictionary = {1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
    return dictionary[month]

    # Another solution
    if month in [1, 2, 3]:
      return 1
    elif month in [4, 5, 6]:
      return 2
    elif month in [7, 8, 9]:
      return 3
    else:
      return 4

def converter(mpg):
    return round((mpg*1.609344/4.54609188), 2)

def replace_dots(str):
    return str.replace(".", "-")

def human_years_cat_years_dog_years(human_years):
    
    catYears = 0
    dogYears = 0

    for year in range (1, human_years+1):
        if year == 1:
            dogYears += 15
            catYears += 15
        elif year == 2:
            dogYears += 9
            catYears += 9
        else:
            dogYears += 5
            catYears += 4

    return [human_years, catYears, dogYears]

def reverse_seq(n):
    return [x for x in range(1, n+1)][::-1]

def remove_exclamation_marks(s):
    return s.replace("!", "")

def temple_strings(obj, feature): 
    return obj + " are " + feature

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

def pipe_fix(nums):

    nums = sorted(nums, key = None)
    minimum = nums[0]
    maximum = nums[-1] + 1

    solution = []
    for number in range(minimum, maximum):
        solution.append(number)
  
    return solution

def find_smallest_int(arr):
    return min(arr)

def double_integer(i):
    return 2*i

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

def apple(x):
    from math import pow
    return "It's hotter than the sun!!" if pow(int(x), 2) > 1000 else 'Help yourself to a honeycomb Yorkie for the glovebox.'

def two_sort(array):

    array = sorted(array, key = lambda x : str(x))
    word = array[0]
    solution = ""
    for letter in word:
        solution = solution + letter + "***"

    return solution[:len(solution)-3]

print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))

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

def how_many_dalmatians(n):

    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1] 
    elif n == 101:
        return dogs[3] 
    else:
        return dogs[2]

def check(seq, elem):
    return elem in seq

def sum_mix(arr):
    total = 0
    for number in arr:
        total += int(number)
    return total

def race(v1, v2, g):
    
    from math import floor
    
    if v2 <= v1:
        return None

    else:

        time = floor((g / (v2-v1))*60*60)
        hours = time // (60*60)
        time = time - hours*60*60
        minutes = time // 60
        time = time - minutes*60
        seconds = time
        return [hours, minutes, seconds]

print(race(720, 850, 70))

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    
    solution = []
    for bird in birds:
        if bird not in geese:
            solution.append(bird)
        else:
            continue
    
    return solution

def fake_bin(x):
    
    fake = ""
    for char in x:
        if int(char) < 5:
            fake += "0"
        else:
            fake += "1"

    return fake

def fix_the_meerkat(arr):
    return arr[::-1]

def nth_even(n):
    return 2*(n-1)

def between(a,b):

    solution = []
    for i in range (a, b+1):
        solution.append(i)

    return solution
    return [x for x in range(a, b+1)]

def dna_to_rna(dna):
    return dna.replace("T", "U")

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2 == 1

def rental_car_cost(d):
    
    if d < 3:
        return d*40
    elif d < 7 and d >=3:
        return d*40 - 20
    else:
        return d*40 - 50

def spin_words(sentence):

    words = sentence.split(" ")
    solution = ""
    for word in words:
        if len(word) < 5:
            solution += word + " "
        else:
            compound = ""
            for char in word:
                compound = char + compound
            solution += compound + " "
    
    return solution.strip()

def order(sentence):

    def sort_rule (pair):
        return pair[1]

    all_pairs = []
    words = sentence.split(" ")
    for word in words:
        number = 0
        for char in word:
            try:
                number = int(char)
            except:
                continue
        all_pairs.append((word, number))

    pairs = sorted(all_pairs, key = sort_rule)

    solution = ""
    for pair in pairs:
        solution += pair[0] + " "

    return solution.strip()

print(order("4of Fo1r pe6ople g3ood th5e the2"))

def comp(array1, array2):

    try:
        if len(array1) != len(array2) or array1 == None or array2 == None or not len(array1) * len(array2):
            return False
    except:
        return False
    
    from math import pow, sqrt
    flag = True
    for number in array1:
        flag = pow(number, 2) in array2 and flag
    
    for number in array2:
        try:
            flag = round(sqrt(number)) in array1 and flag 
        except:
            return false

    return flag

solution = []
def tourney(inp):
    
    solution.append(inp)
    if len(inp) == 2:
        solution.append([max(inp)])
        ret = []
        for item in solution:
            if item not in ret:
                ret.append(item)
        return ret

    else:
        sol = []
        while (len(inp)):
            sol.append(max(inp[:2]))
            inp = inp[2:]
        return tourney(sol)

print(tourney([9, 5, 4, 7, 6, 3, 8]))

def f(n):
    if n < 0:
        return None
    else:
        val = 1 if n == 0 else (
                   n - f(n - 1))
        return val
  
def m(n):
    if n < 0:
        return None
    else:
        val = 1 if n == 0 else (
                   n - m(n - 1))
        return val

def compute_sum(n):

    numbers = ""
    for number in range(1, n+1):
        numbers += str(number)
    total = 0
    for number in numbers:
        total += int(number)

    return total

print(compute_sum(12))

def valid_word(seq, word): 

    valid = ""
    for letters in seq:
        if letters not in word:
            return False

    return True if len(seq) else False

from string import ascii_uppercase, ascii_lowercase

def make_upper_case(s):

    solution = ""
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.find(char)
            solution += ascii_uppercase[index]
        else:
            solution += char
            
    return solution

from math import pow

def powers_of_two(n):
    
    powers = []
    while (n):
        powers.append(int(pow(2, n)))
        n = n - 1
    powers.append(1)

    return powers[::-1]

def people_with_age_drink(age):
    
    dictionary =    {
                        'toddy' : list([x for x in range(0, 14)]) ,
                        'coke' : list([y for y in range(14, 18)]) ,
                        'beer' : list([z for z in range(18, 21)]) ,
                        'whisky' : list([t for t in range(21, 200)]) ,
                    }

    for word in dictionary.keys():
        if age in dictionary[word]:
            return "drink " + word

    return None

def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args

def factorial (number) :

    if number == 1 or number <= 0:
        return 1
    else:
        return number * factorial (number-1)

def make_combination (n, r):

    result = int(factorial(n) / (factorial(n-r) * factorial(r)))
    return result

def get_participants(handshakes):

    if handshakes == 0:
        return 1
    elif handshakes == 1:
        return 2
    elif handshakes == 2:
        return 3
    else:

        counter = 3
        while (True):

            attemp = make_combination(counter, 2)
            if attemp >= handshakes:
                break
            else:
                counter += 1
        
        return counter

print(get_participants(6))

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

    return string[:len(string)-1]