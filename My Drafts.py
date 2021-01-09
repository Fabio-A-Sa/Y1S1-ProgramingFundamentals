# Created on October, 2020
# @author: Fábio Araújo de Sá

print("Hello world!")

a = "Hello"
b = a + " world!"
print(b)

a = int(input())
b = int(input())
c = a -(-b)
print(c)

a = int(input())
b = a - 5
c = int(input())
d = c * 2
e = b + d
print(e)

constant = 10
a = int(input())
b = int(input())
print(constant * (a + b))

import math
x = int(input())*math.pi/180
a = math.sin(x)
b = math.cos(x)
r = round((18*18*a*b)/5)
print(r)

distance = 313
hour_integer = int(input())
minutes_integer = int(input())/60

hours_data= hour_integer + minutes_integer
velocidade = distance/hours_data

v = round(velocidade)
print(v)

pi = 3.14159
r = float(input())
area = pi*r*r
print(round(area, 2))

import math
length = int(input())
hipo = math.sqrt(2*(length**2))
print(round(hipo, 2))

a = int(input())
b = int(input())
# se for ímpar, caso contrário anula:
c = (2-(a-b)%2)*(a+b)
# se for par, caso contrário anula:
d = ((a-b)%2)*(a*b)

h = int(input())
m = int(input())

if h < 18:
    if m < 9:
        hh = h+6
        mm = m+51
    else:
        hh = h+7
        mm = m-9
        
else:
    if m < 9:
        hh = h+6-24
        mm = m+51
    else:
        hh = h+7-24
        mm = m-9


hhh = str(hh)
mmm = str(mm)

if mm < 10:
    if hh < 10:
        print("0" + hhh + ":0" + mmm)
    else:
        print(hhh + ":0" + mmm)
else:
    if hh < 10:
        print("0" + hhh + ":" + mmm)
    else:
        print(hhh + ":" + mmm)

distance = int(input())
litres = float(input())
cost = float(input())

total_cost = (((distance*litres)/100)*cost)
print(round(total_cost, 2))

price = int(input())
received = int(input())

troco = received - price

a = round(troco//50)
b = round((troco - a*50)//20)
c = round((troco - a*50 - b*20)//10)
d = round((troco - a*50 - b*20 - c*10)//5)

print(a, b, c, d)

import math
def time_until_lost_connection(direction_A, direction_B):
    
    # Constantes

    velocidade = 5 # km/h ou 5/60 km/minuto
    distancia_maxima = 35 # km em linha reta
    pi = math.pi

    # Passagem de graus para radianos

    ra = direction_A*pi/180
    rb = direction_B*pi/180
    
    # Cálculo da distância entre A e B
    
    total_distance = math.sqrt(1225/((math.cos(rb)-math.cos(ra))**2+(math.sin(rb)-math.sin(ra))**2))
    time = (total_distance*60)/5
    
    return round(time, 3)

def sum_multiples(n):
    
    soma = 0
    
    # Definir intervalo
    
    for numero in range(1,n+1):
        if numero%3==0 or numero%5==0:
                soma = soma + numero
                
    return soma

print("up202007658")

print("/usr/users2/2020/up202007658/fpro")

Hello!

5.00/10

All rights reserved


word1 = str(input())
word2 = str(input())
word3 = str(input())
word4 = str(input())
word5 = str(input())
word6 = str(input())
word7 = str(input())
word8 = str(input())
word9 = str(input())

print(word1, word2, word3, word4, word5, word6, word7, word8, word9)

tag = str(input())
text = str(input())

print ( "<" + tag + ">" + text + "</" + tag + ">")

n = int(input())

n1 = n
n2 = n + n*10
n3 = n + n*10 + n*100

result = n1 + n2 + n3

print(result)

###

n = str(input())

#strings e concatenação
n1 = n
n2 = n + n
n3 = n + n + n 

#string to integer
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

result = n1 + n2 + n3

print(result)

###

p = float(input())
n = float(input())
r = float(input())

a = (p*((1+r/n)**n)**2)     
print(round(a, 3))

import datetime
now = datetime.datetime.now()
h = int(now.hour)
m = int(now.minute)

if h < 16:
    if m < 30:
        hh = h+8
        mm = m+30
    else:
        hh = h+9
        mm = m-30
        
else:
    if m < 30:
        hh = h+8-24
        mm = m+30
    else:
        hh = h+9-24
        mm = m-30
      
    
hhh = str(hh)
mmm = str(mm)


if mm < 10:
    if hh < 10:
        print("0" + hhh + ":0" + mmm)
    else:
        print(hhh + ":0" + mmm)
else:
    if hh < 10:
        print("0" + hhh + ":" + mmm)
    else:
        print(hhh + ":" + mmm)
        
number = int(input())
soma = 0

for i in range(1, number+1):
    if number%i == 0:
        soma = soma + i
        
print(soma)

LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

if 101>LE>-1 and 101>RE>-1 and 101>PE>-1 and 101>TE>-1:
    if PE<40 or TE<40:
        print("RFC")
       
    else:
        grade = (LE + RE + 5 * PE + 3 * TE) / 50 + 0.01
        print(round(grade))
       
else:
    print("Input error")

i = 4
while i<50:
    print(i)
    i = i + 3
    
n = str(int(input()))
total = str(1234567890987654321)
if n in total:
    print("Looping number")
else:
    print("Not a looping number")

number = float(input("Number? "))
a = number
b = 0

while True:
    medio = (a + b) / 2 #Ponto Médio de a e b
    if (medio*medio == number) or (round(a, 5) - round(b, 5) == 0):
        # Quando o médio é o valor ideal:
        print(round(medio, 5))
        break
    elif medio*medio > number:
        # Limita o intervalo à esquerda da raiz quadrada
        a = medio
    else:
        # Limita o intervalo à direita da raiz quadrada
        b = medio

import math

somatorio = 0

for K in range(0, 51):
    somatorio = somatorio + (math.factorial(4  * K) * (1103 + 26390 * K)) / (math.factorial(K)**4 * 396**(4*K))
inversopi = (2 * 2**.5 / 9801) * somatorio

pi_normal = 1 / inversopi
print(round(pi_normal, 8))

def C(n,r):
    
    n_result = 1
    r_result = 1
    n_menos_r_result = 1
    
    for i in range(1, n+1):
        n_result = n_result*i
    
    for i in range(1, r+1):
        r_result = r_result*i
    
    for i in range (1, (n-r)+1):
        n_menos_r_result = n_menos_r_result*i
    
    combination = n_result/ (r_result*n_menos_r_result)
    
    return(round(combination))

L = int(input("Give me a L: "))
S = int(input("Give me a S: "))
R = L

if R <= S:
    L = R
    R = S
    S = L
   
while True:
    if S <= R:
        R = R - S
        continue
    if not R:
        break
    L = R
    R = S
    S = L

print(S)

lower = int(input("Give me a lower number: "))
upper = int(input("Give me a upper number: "))
n = 1
prime_numbers = "Prime numbers between " +  str(lower) +  " and " +  str(upper) +  " are:"

# Para garantir números só positivos
if lower < 0:
    lower = 2 # Nem 0 nem 1 são primos
if upper < lower:
    print("Lower number is bigger then upper, error!")

# Cálculo dos números primos
# Preenchimento da string prime_numbers
for i in range (lower, upper+1):
    for s in range (2, i):
        if (i%s) == 0:
            break
    else:
        # Number to string
        prime_numbers = prime_numbers + " " + str(i)# Add space between prime numbers
        
# Frase correta
print(prime_numbers)

num = int(input("Number? "))
result = 0
temporario = num

while temporario > 0:
    unid = temporario % 10
    result = result * 10 + unid
    temporario = temporario // 10

print(result)

num = int(input("Number? "))
divisores = 0

for i in range(1, num+1, 1):
    if num % i == 0:
        divisores = divisores + 1
        
if divisores > 2:
    print("False")
else:
    print("True")
    
number = int(input("Number? "))

for i in range(1, number+1, 1):
    if i%3 == 0:
        if not (i%3 == 0 and i%5 == 0):
            i = str("Fizz")
            print(i, end=" ")
        

    elif i%5 == 0:
        if not (i%3 == 0 and i%5 == 0):
            i = str("Buzz")
            print(i, end= " ")
        
    else:
        print(i, end= " ")
        
n1 = int(input())
n2 = int(input())
n3 = 0
n4 = n2
while n4 > 0:
    n3 = n3 + 1
    n4 = n4//10
        

result = n1*(10**n3) + n2
print(result)

numb = int(input("Number? "))
x = numb/2
xx = 0

while round(x, 2) != round(xx, 2):
    # Aproximação a duas casas decimais#
    xx = (x + (numb/x))/2
    x = (xx + (numb/xx))/2
    
print(round(x, 2))

def validate(grade):
    value = (type(grade) == type(1) or type(grade) == type(1.5)) and (100 >= grade >= 0)
    # É verdadeiro se o número estiver entre 0 e 100 e se for int ou float
    return(value)

def dogs(h_age):
    
    if h_age <= 2:
        d_age = h_age * 10.5
    else:
        d_age = 21 + 4*(h_age-2)
    
    
    return(d_age)

import math

def solver(a,b,c):
    
    delta = (b**2 - 4*a*c)
    
    if delta > 0:
        solution1 = (-1*b+math.sqrt(delta))/(2*a)
        solution2 = (-1*b-math.sqrt(delta))/(2*a)
    
        if solution1 == solution2:
            return [solution1]
        
        if solution2 > solution1:
            return [solution1, solution2]
        else:
            return [solution2, solution1]
        
    elif delta == 0:
        solution = (-1*b)/(2*a)
        return [solution]
        
    else:
        return [] # Lista vazia
    
def get_positions(setence, word_list):
    
      sentence = setence.split()
      string_final = []
     
      for a in range(0, 2): # Words in sentence
          for b in range(0, 3): # Words in word_list
          
                if sentence[a] == word_list[b]:
                    string_final.append(b) # Add b value
                    break        
               
      if len(string_final) == 2: # Finish
        return str(string_final[0]) + " " + str(string_final[1])
    
      else:
        return "" # Nothing


def pascal(n):
    string_final = ""
    import math
    for i in range (0, n): # Row
        for j in range (i+1): #Line
            string_final = string_final + str(int(math.factorial(i) / (math.factorial(j) * math.factorial(i-j))))
            if i > j:
                string_final = string_final + " "   
        string_final = string_final + "\n"      # New line                       
    
    return string_final
                                

def collatz(n):
    aux = n
    final_str = ""
    
    while aux > 1:
        final_str = final_str + str(aux) + ","
        
        if (aux%2 == 1):
            aux = (aux * 3 + 1)
        
        elif (aux%2 == 0):
            aux = round(aux//2)
        
    
    return (final_str + "1")

def caesar(message):
    
    import math
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    result = "" # Empty string to accumulate
    
    n = 0
    
    for letter in message:
        if letter in alphabet:
            result = result + alphabet[(alphabet.index(letter) - int((((1+math.sqrt(5))**n)-(((1-math.sqrt(5))**n)))/((2**n)*(math.sqrt(5))))) % 26]
        else:
            result = result + letter # In correct order
        n = n + 1
        
    return result

def greatest(num):
    
    num = "".join(sorted(str(num), reverse = True)) # Ascending
    resultado = int(num)
        
    return resultado


def ugly(n):
    
    while n%2 == 0:
        n = n/2
    
    while n%3 == 0:
        n = n/3

    while n%5 == 0:
        n = n/5
                    
    if n == 0:
        return False
    return (n == 1)
        

def sum_numbers(n):
    soma = 0
    for i in range (1, n+1):
        soma = soma + i
    
    return(soma)

def is_perfect(n):
    soma_divisores = 0

    for i in range (1, n):
        if n%i == 0:
            soma_divisores = soma_divisores + i
        else:
            continue
        

    
    return(soma_divisores == n)

def adigits(a, b, c):
    d = 0
    e = 0
    f = 0
    g = a + b + c
    
    d = max(a, b, c)
    f = min(a, b, c)
    e = g - (d+f)
    
    return int(f"{d}{e}{f}")

def mastermind(g1, g2, g3, c1, c2, c3):
    pontuation = 0
    
    if g1 == c1:
        pontuation = pontuation + 3
    if g1 == c2 or g1 == c3:
        pontuation = pontuation + 1
    
    if g2 == c2:
        pontuation = pontuation + 3
    if g2 == c1 or g2 == c3:
        pontuation = pontuation + 1
        
    if g3 == c3:
        pontuation = pontuation + 3
    if g3 == c1 or g3 == c2:
        pontuation = pontuation + 1
    
    if (g1 == g2 or g1 == g3 or g2 == g3) and not (g1 == g2 == g3):
        pontuation = pontuation - 1
    
    if g1 == g2 and g2 == g3:
        pontuation = 6
    
    return(pontuation)

import random
import statistics

pontos_circulo = 0

pontos_sorteados = 0

lista_pi = []

for i in range(100):
    for a in range(1000):
        pontos_sorteados = pontos_sorteados + 1.0

        x = random.uniform(-1,1)
        y= random.uniform(-1,1)

        distancia = x*x + y*y

        if distancia <= 1:
            pontos_circulo = pontos_circulo + 1.0

    proporcao = pontos_circulo / pontos_sorteados

    pi = 4 * proporcao
    lista_pi.append(pi)

b = statistics.stdev(lista_pi,3.1415)
n = 1

while b > 0.005:
    lista_pi = []
    for i in range(100):
        for a in range(10002):
            pontos_sorteados = pontos_sorteados + 1.0

            x = random.uniform(-1,1)
            y= random.uniform(-1,1)

            distancia = x*x + y*y

            if distancia <= 1:
                pontos_circulo = pontos_circulo + 1.0

        proporcao = pontos_circulo / pontos_sorteados

        pi = 4 * proporcao
        lista_pi.append(pi)
    n = n+1

    b = statistics.stdev(lista_pi,3.1415)

media_lista_pi = statistics.mean(lista_pi)

# Python code to implement Conway's Game Of Life
import argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
 
# setting up the values for the grid
ON = 255
OFF = 0
vals = [ON, OFF]
 
def randomGrid(N):
 
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
 
def addGlider(i, j, grid):
 
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255], 
                        [255,  0, 255], 
                        [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider
 
def addGosperGliderGun(i, j, grid):
 
    """adds a Gosper Glider Gun with top left
        cell at (i, j)"""
    gun = np.zeros(11*38).reshape(11, 38)
 
    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255
 
    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255
 
    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255
 
    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255
 
    grid[i:i+11, j:j+38] = gun
 
def update(frameNum, img, grid, N):
 
    # copy grid since we require 8 neighbors 
    # for calculation and we go line by line 
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
 
            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around 
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                          grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                          grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                          grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
 
            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
 
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,
 
# main() function
def main():
 
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
 
    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
     
    # set grid size
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)
         
    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
 
    # declare grid
    grid = np.array([])
 
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)
 
    else:   # populate grid with random on/off -
            # more off than on
        grid = randomGrid(N)
 
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)
 
    # # of frames? 
    # set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
 
    plt.show()
 
# call main
if __name__ == '__main__':
    main()

print(media_lista_pi)

import math

def digits_average(n):
    
    while (n//10 != 0 ):
        number = 0
        i = 1
        while (n//10 != 0):
            a = n%10 #resto
            n = n//10
            b = n%10
            c = math.ceil((a+b)/2) #Arredonda sempre para cima
            number = number + c*i
            i = i *10
        n = number
    return n

def count_chars(a_string):
    
    c_alphabetic = 0
    c_digit = 0
    c_special_symbol = 0
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    a_string = a_string.upper()
    
    for i in range (0, len(a_string)):
        
        if a_string[i] in string:
            c_alphabetic = c_alphabetic + 1
            
        elif a_string[i] in numbers:
            c_digit = c_digit + 1
        
        else:
            c_special_symbol = c_special_symbol + 1
            
    result = (c_alphabetic,) + (c_digit,) + (c_special_symbol,)
    
    return result

def count_until(tup):
    
    if len(tup) == 0:
        return -1
    
    for i in range (0, len(tup)):
        if type(tup[i]) == type((1,)):
            return i
        else:
            if (i == len(tup)-1):
                return -1
            else:
                continue
            
def longest(s):
    
    s = s.split()
    long = 0
    
    for i in range(0, len(s)):
        
        medida = len(s[i])
        
        if medida >= long:
            long = medida
            

    return long  

def map(pos, steps):
    
    (x, y) = pos # Separar a posição inicial em x e y
    
    steps = steps.split("-") # Separar os passos segundo os -
    
    for i in range (0, len(steps)):
        
        if steps[i] == "up":
            y = y + 1
            
        elif steps[i] == "down":
            y = y - 1
            
        elif steps[i] == "left":
            x = x - 1
            
        elif steps[i] == "right":
            x = x + 1
        
        
    return (x,) + (y,)

def repeated_letter(s):
    
    for i in range (0, len(s)):
        for k in range (i+1, len(s)):
            if s[i] == s[k]:
                return s[i]
                break
            else:
                continue
            
  def palindrome_index(s):
    
    new = ""
    new_new = ""
    result = 0
    
    for i in range (0, len(s)):
        
        new = s[:i] + s[i+1:] # new string sem a letra de idex i
        
        if s == s[::-1]:
            result = -1
            break

        elif new == new[::-1]: # Se é igual ao seu inverso
            result = i
            break
        
        else:
            if i == len(s)-1:
                result = -1
            else:
                continue
            
    return result

# s = str(input())
# print(palindrome_index(s))

def remove_leading(ip): 

    ip = ip.split(".") # Lista de números
    new_ip = ""
    
    for i in ip: # i representa um número na lista ip
        
        new_ip = new_ip + ".".join([str(int(i))])  + "." # Junta todos os números com pontos
        
        result = new_ip[0:(len(new_ip)-1)] # Retira o último ponto
        
    return result

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


def ajustes(result):
    
    result = result[1::] # retira a primeira vírgula
    new_list = result.split(",") # lista com itens do tipo "n->m" ou "n->n"
    final = ""
    
    for x in range (0, len(new_list)):
        
        y = round((len(new_list[x])-2)/2) # número de dígitos de n
        
        if new_list[x][:y] == new_list[x][-y:]: #significa que n->n
            new_list[x] = new_list[x][0:y] #substitui por n
            
        else:
            continue
        
    for z in range(0, len(new_list)):  
        final = final + "," + new_list[z]
        
    return final[1::] # retira a primeira vírgula

            
def summary_ranges(a_string):
    
    vazio = ""
    
    if a_string == "":
        return vazio
    
    if len(a_string) == 1:
        return a_string
    
    a_list = a_string.split(",")
    result = ""
    
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while (i < len(a_list)+1) or ((i+j+1) < len(a_list)):
    
        while ((int(a_list[i+j]) - int(a_list[i])) == j):
            if (i+j) == (len(a_list)-1):
                result = result + "," + str(a_list[i]) + "->" + str(a_list[i+j])
                
                return ajustes(result) # chama a outra função que irá retirar a 
                                        # primeira vírgula e substituir casos 
                                        # do tipo "n->n" por "n"
            else:
                j = j + 1
        
        else:
            result = result + "," + str(a_list[i]) + "->" + str(a_list[i+(j-1)])
            i = i + j
            j = 0 # cancel complement

# a_string = str(input("qualquer coisa"))
# print(summary_ranges(a_string))

def rm_letter_rev(ch, a_string):
    
    string_final = ""
    
    for i in range (1, len(a_string)+1):
        
        if a_string[-i] == ch:
            continue
        else:
            string_final = string_final + a_string[-i]
            
    return string_final

def find_dtype(a_tuple, data_type):
    
    new_tuple = ()
    
    for i in range (0, len(a_tuple)):
        if type(a_tuple[i]) == data_type:
            new_tuple = new_tuple + (a_tuple[i],)
        else:
            continue
    
    return new_tuple

    
def palindrome(a_string):
    
      counter = 0
      
      for x in range(0, len(a_string)-1):
          for y in range(x, len(a_string)):
            
              if y > x: # Y anda sempre à frente de X
                  string = a_string[x:y+1]
                  if string == string[::-1]: # Se encontrar uma sequência igual
                      counter = counter + 1
                  else:
                      continue
               
      return f"The string '{a_string}' contains {counter} palindrome substrings."
  
def triplet(a_tuple):
    
    a = 0
    b = 0
    c = 0
    
    empty = ()
    final_tuple = ()
    final_final_tuple = ()

    for x in range (0, len(a_tuple)):
        for y in range (x+1, len(a_tuple)):
            for z in range (y+1, len(a_tuple)):
                
                if ((int(a_tuple[x]) + int(a_tuple[y]) + int(a_tuple[z])) == 0):
                    
                    a = int(a_tuple[x])
                    b = int(a_tuple[y])
                    c = int(a_tuple[z])
                    
                    final_tuple = (a,) + (b,) + (c,)
                    final_final_tuple = final_final_tuple + (final_tuple,)
                    
    if len(final_final_tuple) == 0:
        return empty
    else:
        return final_final_tuple[0]
    
def sort_rule(data):
    avg_grade = 100 - (float(sum(data[2]))) / (len(data[2]))
    return (avg_grade, data[0], data[1])


def sort_grades(records):
    return(tuple(sorted(records, key=sort_rule)))


def rm_letter_rev(ch, a_string):
    
    string_final = ""
    
    for i in range (1, len(a_string)+1):
        
        for letter in a_string:
            if letter == ch:
                string_final = string_final
            else:
                string_final = string_final + a_string[-i]
    
    return string_final
    

def get_positions(setence, word_list):
    
      sentence = setence.split()
      string_final = []
     
      for a in range(0, 2): # Words in sentence
          for b in range(0, 3): # Words in word_list
          
                if sentence[a] == word_list[b]:
                    string_final.append(b) # Add b value
                    break        
               
      if len(string_final) == 2: # Finish
        return str(string_final[0]), str(string_final[1])
    
      else:
        return "" # Nothing


def pascal(n):
    string_final = ""
    import math
    for i in range (0, n): # Row
        for j in range (i+1): #Line
            string_final = string_final + str(int(math.factorial(i) / (math.factorial(j) * math.factorial(i-j))))
            if i > j:
                string_final = string_final + " "   
        string_final = string_final + "\n"      # New line                       
    
    return string_final


def greatest(num):
    
    num = ascending = "".join(sorted(str(number)))
    resultado = int(num)
        
    return resultado

    
def caesar(message):
    
    import math
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    result = "" # Empty string to accumulate
    
    n = 0
    
    for letter in message:
        if letter in alphabet:
            result = result + alphabet[(alphabet.index(letter) - int((((1+math.sqrt(5))**n)-(((1-math.sqrt(5))**n)))/((2**n)*(math.sqrt(5))))) % 26]
        else:
            result = result + letter # In correct order
        n = n + 1
        
    return result




Find My Type

def find_dtype(a_tuple, data_type):
    
    new_tuple = ()
    
    for i in range (0, len(a_tuple)):
        if type(a_tuple[i]) == data_type:
            new_tuple = new_tuple + (a_tuple[i],)
        else:
            continue
    
    return new_tuple


def palindrome(a_string):
    
    n = 0 # Counter
    if len(a_string)%2 == 0:
        l = int((len(a_string))/2)
    else:
        l = int((len(a_string)-1)/2)
    
    for i in range (0, l):
        if a_string[i] == a_string[l-i]:
            n = n + 1
    
    
    final_string = f"The string '{a_string}' contains {n} palindrome substrings"
    return final_string


def triplet(a_tuple):
    
    a = 0
    b = 0
    c = 0
    
    empty = ()
    final_tuple = ()
    final_final_tuple = ()

    for x in range (0, len(a_tuple)):
        for y in range (x+1, len(a_tuple)):
            for z in range (y+1, len(a_tuple)):
                
                if ((int(a_tuple[x]) + int(a_tuple[y]) + int(a_tuple[z])) == 0):
                    
                    a = int(a_tuple[x])
                    b = int(a_tuple[y])
                    c = int(a_tuple[z])
                    
                    final_tuple = (a,) + (b,) + (c,)
                    final_final_tuple = final_final_tuple + (final_tuple,)
                    
    if len(final_final_tuple) == 0:
        return empty
    else:
        return final_final_tuple[0]
        


def palindrome(a_string):
    
      counter = 0
      
      for i in range(0, len(a_string)-1):
          for j in range(i + 1, len(a_string)):
            
              if (a_string[i] == a_string[j]):
                  counter = counter + 1
              else:
                  continue
               
      return f"The string '{a_string}' contains {counter} palindrome substrings."


# Third Public Test
# temos "abbaeae"
# Opções: aa,aa,bb,aa,ee (5, sem repetições)




def sort_grades(records):
    
    solution = [] # Empty tuple
    
    for x in range (0, len(records)): # Student's X Profile
        for y in range (3): # Navegation (0,1,2) on X profile
            for z in range (0, len((records[x])[y])):
                            # Grades of student X if Y == 2
                            # UP Student X if Y == 1
                            # Name of student X if Y == 0
    
                if 
                            
    return (solution)


def sort_grades(records):
    
    solution = [] # Empty tuple
    
    for x in range (0, len(records)): # Student's X Profile
        solution = ((records[x])[3]).sort()

                
                
                            
    return solution


After a lot of studying the function sorted():
    
def averages(record):
    #calculates the average score of each student
    return (sum(record[2])) / len(record[2])

def priority(record):
    #defines the priority for names and up's
    return (record[0],record[1])

def sort_grades(records):
    
    #sorts records by the names and the up's 
    sort_1 = sorted(records, key = priority)
    
    #sorts new records (sort_1) by the averages in descending order (-> reverse = True)
    sort_2 = sorted(sort_1, key = averages, reverse = True)

After a lot of studying the function sorted():

def sort_grades(records):
    
    average_grades = (sum(records[2])) / len(records[2])
    prioridade1 = records[0]
    prioridade2 = records[1]
    
    quase = sorted(records, key = prioridade1)
    quase2 = sorted(quase, key = prioridade2)
    final = sorted(quase2, key = average_grades, reverse = True)
    
    return tuple(final)

# After a lot of studying the function sorted():

def notas(records):
    return (sum(records[2]))/len(records[2])

def prioridade_nome_up(records):
    return (records[0],records[1])

def sort_grades(records):
    
    ordem_primaria = sorted(records, key = prioridade_nome_up)
    final = tuple(sorted(ordem_primaria, key = notas, reverse = True))
    

    return final


def palindrome(a_string):
    
      counter = 0
      
      for x in range(0, len(a_string)-1):
          for y in range(x, len(a_string)):
            
              if y > x: # Because Y is always in front of X
                  string = a_string[x:y+1]
                  if string == string[::-1]: # If sequence ==
                      counter = counter + 1
                  else:
                      continue
               
      return f"The string '{a_string}' contains {counter} palindrome substrings."



After a lot of studying the function sorted():

def notas(records):
    return (sum(records[2]))/len(records[2])

def prioridade_nome_up(records):
    return (records[0],records[1])

def sort_grades(records):
    
    ordem_primaria = sorted(records, key = prioridade_nome_up) # Ordem crescente
    final = tuple(sorted(ordem_primaria, key = notas, reverse = True)) # Ordem decrescente
    
    return final



def count_chars(a_string):
    
    c_alphabetic = 0
    c_digit = 0
    c_special_symbol = 0
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    a_string = a_string.upper()
    
    for i in range (0, len(a_string)):
        
        if a_string[i] in string:
            c_alphabetic = c_alphabetic + 1
            
        elif a_string[i] in numbers:
            c_digit = c_digit + 1
        
        else:
            c_special_symbol = c_special_symbol + 1
            
    result = (c_alphabetic,) + (c_digit,) + (c_special_symbol,)
    
    return result

def count_until(tup):
    
    if len(tup) == 0:
        return -1
    
    for i in range (0, len(tup)):
        if type(tup[i]) == type((1,)):
            return i
        else:
            if (i == len(tup)-1):
                return -1
            else:
                continue

def longest(s):
    
    s = s.split()
    long = 0
    
    for i in range(0, len(s)):
        
        medida = len(s[i])
        
        if medida >= long:
            long = medida
            

    return long    

def map(pos, steps):
    
    (x, y) = pos # Separar a posição inicial em x e y
    diference_x = 0
    diference_y = 0
    
    steps = steps.split("-") # Separar os passos segundo os -
    
    for i in range (0, len(steps)):
        
        if steps[i] == "up":
            y = y + 1
            
        elif steps[i] == "down":
            y = y - 1
            
        elif steps[i] == "left":
            x = x - 1
            
        elif steps[i] == "right":
            x = x + 1
        
        
    return (x,) + (y,)


def repeated_letter(s):
    
    for i in range (0, len(s)):
        for k in range (i, len(s)):
            if s[i] == s[k] and k > s:
                return s[i]
                break
            else:
                continue


def palindrome_index(s):
    
    new = ""
    new_new = ""
    result = 0
    
    for i in range (0, len(s)):
        
        new = s[:i] + s[i+1:] # new string sem a letra de idex i
        
        if s == s[::-1]:
            result = -1
            break

        elif new == new[::-1]: # Se é igual ao seu inverso
            result = i
            break
        
        else:
            if i == len(s):
                result = -1
            else:
                continue
            
    return result

# s = str(input())
# print(palindrome_index(s))        
        


def remove_leading(ip):
    
    ip = ip.split(".") # Separar em números segundo os "."
    new_ip = "" # Resposta final
        
    for i in ip: # Avaliação de cada número no ip
        
        if len(ip[i]) != 1:
            while ip[i][0] == 0
        
        else:
            new_ip = new_ip + ip[i] + "."
            
            
    new_ip_final = new_ip[]
            
    return new_ip



def remove_leading(ip): 

    ip = ip.split(".") # Lista de números
    new_ip = ""
    
    for i in ip: # i representa um número na lista ip
        
        new_ip = new_ip + ".".join([str(int(i))])  + "." # Junta todos os números com pontos
        
        result = new_ip[0:(len(new_ip)-1)] # Retira o ponto final
        
    return result


def summary_ranges(a_string):
    
    a_string = a_string.replace(",", "")
    result = ""
    coisa = "0123456789"
    
    for x in range (0, len(a_string)):
        for y in range (x+1, len(a_string)):
            if a_string[x:y+1] in coisa:
                result = result + "," + a_string[x] + "->" + a_string[y]
            else:
                continue
            
    return result
    
# a_string = str(input())
# print(summary_ranges(a_string))



Será que chumbo?

print("Bem vindo à FEUP")
print("Por favor selecione uma cadeira: MDIS, FPRO, ALGE", end="")
cadeira = (str(input())).upper()
print("Responda com SIM ou NAO às seguintes questões:")

if cadeira == "MDIS":
    print("Desculpa, ∀x ( AlunoDeMDIS(x) → Chumbado(x) )")
    
elif cadeira == "FPRO":
    resposta = (str(input("Gostas de tartarugas? "))).upper()
    if resposta == "SIM":
        print("CHUMBADO")
        print("F para a tua nota")
    else:
        print("Quintas de manhã")

elif cadeira == "ALGE":
    resposta = (str(input("Gostas da Apple? "))).upper()
    if resposta == "NAO"
        print("Ó Siri, chumba já este aluno!")
        
    

5 do RE05 segundo o senhor professor

def qualquer_cena(item):
    max_grade = 100
    mean = max_grade - (float(sum(item[2]))) / max(len(item[2]), 1)
    return (mean, item[0], item[1])

def sort_grades (records):
    return tuple(sorted(records, key=qualquer_cena, reverse=False)




Play05 08

def ascii_code(coisas):
    
    total = 0
    
    if type(coisas) == str: # If coisas is a word    
        for item in coisas:
            total = total + ord(coisas)
    else: #If coisas is a number
        for item in coisas:
            total = total + ascii_code(coisas)
    return total

def greatest_member(a_tuple):
    
    result = [] # Empty list
    
    for algo in a_tuple:
        result.append(ascii_code(algo)) # Add a biggest ascii
    return a_tuple[result.index(max(result))]


def summary_ranges(a_string):
    
    a_string = a_string.replace(",", "") # remove commas
    result = "" # final string
    
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while ((i+j) < len(str(a_string))):
        
        while int(a_string[i+j]) == int(int(a_string[i]) + j):
                j = j + 1
        
        else:
            result = result + "," + str(a_string[i]) + "->" + str(a_string[i+(j-1)])
            i = i + j
    
    return result[1::]

Play05 09

def summary_ranges(a_string):
    
    a_list = a_string.split(",") # list with numbers
    result = "" # final string
    
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while ((i-1) < len(a_list)):
        
        while int(a_list[i+j]) == int(int(a_list[i]) + j):
                j = j + 1
        
        else:
            result = result + "," + str(a_list[i]) + "->" + str(a_list[i+(j-1)])
            i = i + j
            j = 0 # complement null
    
    return result[1::] # without first comma






def ajustes(result):
    
                result = result[1::] # retira a primeira vírgula
                new_list = result.split(",") # lista com itens do tipo "n->m" ou "n->n"
                final = ""
                
                for x in range (0, len(new_list)):
                
                    y = round((len(new_list[x])-2)/2) # número de dígitos de n
                        
                    if new_list[x][:y] == new_list[x][-y:]: #significa que n->n
                        new_list[x] = new_list[x][0:y] #substitui por n
                        
                    else:
                        continue
                
                for z in range(0, len(new_list)):
                    
                    final = final + "," + new_list[z]
                            
                return final[1::] # retira a primeira vírgula
    

PE01

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1%2 == 1:
    result = n2*n3
else:
    result = n2 - n3

print(result)

i = int(input())

if i%2 != 1:
    print(i**2)
else:
    if i%7 == 0:
        if i%11 == 0:
            print(3*i+2)
        else:
            if i%3 == 0:
                if i%5 == 0:
                    print(-i)
                else:
                    print (5-i)
            else:
                print(0)
            
    
    else:
        print(i-2)
    

import math
shape = str(input())

if (shape == "sphere"):
    radius = float(input())
    
    volume = (4/3)*math.pi*(radius**3)

elif (shape == "cylinder") or (shape == "cone"):
    radius = float(input())
    height = float(input())
    
    if (shape == "cylinder"):
        volume = math.pi*(radius**2)*height
        
    elif (shape == "cone"):
        volume = (1/3)*math.pi*(radius**2)*height

print(round(volume, 1))


number = int(input())
aux = number 
count = 0

while aux > 9: # only one digit
    last_digit = aux%10
    first_digit = aux//10
    aux = last_digit * first_digit
    count = count + 1
print(count)


a = int(input())
b = int(input())

while a < b:
    
    if not (a**2 > (b/2)**2) and not (a % 3 == 0 and a % 5 == 0) and (a % 2 == 0):
        a = a//8
        print(a)
            
    if not (a**2 > (b/2)**2) and not (a % 3 == 0 and a % 5 == 0) and not (a % 2 == 0):
        print(a+1)
    
    a = a + 3
    

def summary_ranges(a_string):
    
    a_list = a_string.split(",") # list with numbers
    result = "" # final string
    
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while ((i+j+1) < len(a_list)):
        
        while ((int(a_list[i+j]) - int(a_list[i])) == j):
            if (i+j) == (len(a_list)-1):
                result = result + "," + str(a_list[i]) + "->" + str(a_list[i+j])
                
                # retira a primeira vírgula substitui casos do tipo "n->n" por "n"
                                       
                result = result[1::] # retira a primeira vírgula
                new_list = result.split(",") # lista com itens do tipo "n->m" ou "n->n"
                final = ""
                
                for x in range (0, len(new_list)):
                
                    y = round((len(new_list[x])-2)/2) # número de dígitos de n
                        
                    if new_list[x][:y] == new_list[x][-y:]: #significa que "n->n"
                        new_list[x] = new_list[x][0:y] #substitui por n
                        
                    else:
                        continue
                
                for z in range(0, len(new_list)):
                    
                    final = final + "," + new_list[z]
                            
                return final[1::] # retira a primeira vírgula
            
            else:
                j = j + 1
        
        else:
            result = result + "," + str(a_list[i]) + "->" + str(a_list[i+(j-1)])
            i = i + j
            j = 0 # cancel complement


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

# a_tuple = (('ab', 'dez', ('1',)), ('ab', 'de', ('1',)), 'defg', 'jkab')
# print(greatest_member(a_tuple))



rotating

Write a Python function rotate_list(l) that, given a list l of length >= 3, 
shifts its elements to the left 3 times, returning the new list. 
If an element is at the beginning, it should circle back to the end.

for the list l=[1,2,3,4,5,6], the result is the list [4,5,6,1,2,3]
for the list l=[1,2,3,4,5,6,7,8], the result is the list [4,5,6,7,8,1,2,3]


def rotate_list(l):
    
    final = l.copy()
    [x,y,z] = l[0:3]
    final.remove(x)
    final.remove(y)
    final.remove(z)
    
    final.append(x)
    final.append(y)
    final.append(z)
        
    return final

l = list(input())
print(rotate_list(l))

pattern

Write a function pattern_hunting(l1, l2, p) 
that given two equal length lists of strings l1 and l2 and a pattern (string) p, 
builds a new list with elements from the original lists 
where the pattern occurs not in that element, 
but the corresponding (i.e. same index) element in the other list. 
The resulting list should be ordered alphabetically in descending order.

- for the list l1=['a string', 'two strings', 'not here'], 
another list l2=['choose me', 'me too', 'but not me'] 
and the pattern p='string', 
    the result is the list ['me too', 'choose me']
    
- for the list l1=['not found', 'pattern here', 'skip', 'next... or not?'], 
another list l2=['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere'] 
and the pattern p='pattern', 
    the result is the list ['not found', 'next... or not?', 'i want to be chosen']

def pattern_hunting(l1, l2, p):

    result = [] # empty list
    
    for element in range(0, len(l1)):
        
        if p in l1[element]:
            result.append(l2[element])
            
        elif p in l2[element]:
            result.append(l1[element])
    
    final = sorted(result, reverse=True)
    
    return final

# l1=['not found', 'pattern here', 'skip', 'next... or not?']
# l2=['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere']
# p='pattern'
# print(pattern_hunting(l1, l2, p))

Orthogonal matrices 

Write a function is_orthogonal(mx) that given a square matrix 
(list of lists where each list represents a row), 
determines if the matrix is orthogonal, 
returning the appropriate boolean value. 
A matrix M is orthogonal if MMᵀ = I 
(i.e. the product of M by its transpose is equal to the identity matrix). 
The identity matrix is a square matrix in which all the elements 
of the principal diagonal are ones and all other elements are zeros.

- for the matrix mx=[[-1, 0], [0,1]], the output should be True
- for the matrix [[-2,3], [4,-1]], the output should be False

def is_orthogonal(mx):
    
    diagonal_ok = True
    others_ok = True
    diagonal = 0
    resto = 0
    
    for i in range (0, len(mx)):
        for j in range (0, len(mx)):
        
            if i == j:
                
                for k in range(0, len(mx[i])):
                    diagonal = diagonal + mx[i][k] * mx[j][k]
                
                diagonal_ok = diagonal_ok and (diagonal == 1)
                diagonal = 0
                
            else: 
                
                for k in range(0, len(mx[i])):
                    resto = resto + mx[i][k] * mx[j][k]
                
                others_ok = others_ok and (resto == 0)
                resto = 0
                
    return ( diagonal_ok and others_ok )

# mx = [[-2,3], [4,-1]]
# print(mx)
# print(is_orthogonal(mx))



N-th lowest

Write a Python function nth_lowest(lnum, n) 
that, given a list of numbers lnum and a positive integer n, 
returns the n-th lowest value in the list. 

Assume n always holds a valid value 
(i.e. does not include a number less or equal to one) 
and that the list never has repeated values.

for the list lnum=[42, 234, 135, 21, 232, 12312, -2343] and n=2, 
    the result is the number 21
    
for the list lnum=[73,100,23,18,84,61,56,75,92,38,54,73,3,13] and n=12, 
    the result is the number 84
    
def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n-1]
    
lnum = [42, 234, 135, 21, 232, 12312, -2343]
n=2
print(nth_lowest(lnum, n))

numbers = [1, 3, 4, 2] 
  
# Sorting list of Integers in ascending 
numbers.sort() 
  
print(numbers) 



Last Man Standing

In a circle of people, represented by a list of integers alist, 
a game will take place. 

Counting will start at the beginning of the list, 
and after counting a certain number of people, specified by step, 
the person where the counting stopped is out of the game.

Write a Python function last_man_standing(alist, step) 
that returns the last person left on the circle.

Example:
    Input: [3, 4, 1, 6, 2, 5, 7], 3	
    Output: 6
    
Order of elimination of people: 1, 5, 4, 2, 7, 2, 3 

first we will import the subprocess module
import subprocess

# now we will store the profiles data in "data" variable by 
# running the 1st cmd command using subprocess.check_output
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# now we will store the profile by converting them to list
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# using for loop in python we are checking and printing the wifi 
# passwords if they are available using the 2nd cmd command
for i in profiles:
    # running the 2nd cmd command to check passwords
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                        'key=clear']).decode('utf-8').split('\n')
    # storing passwords after converting them to list
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    # printing the profiles(wifi name) with their passwords using 
    # try and except method 
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))


def all_deleted(alist):
    answer = (len(alist) == 1)
    return answer

def last_man_standing(alist, step):
    
    parcial = ""
    comprimento = len(alist)
    contador = step - 1
    
    while all_deleted(alist) == False:
        
        if contador%comprimento == 0: # remove o último da lista
            
            next_deleted = alist[comprimento-1]
            parcial = parcial + str(next_deleted)
            alist.remove(next_deleted)
            contador = contador - 1 + step
            comprimento = comprimento - 1
            
        else:
       
            next_deleted = alist[contador%comprimento-1]
            parcial = parcial + str(next_deleted)
            alist.remove(next_deleted)
            contador = contador - 1 + step
            comprimento = comprimento - 1
    
    return alist[0]

alist = [3, 4, 1, 6, 2, 5, 7]
step = 3
print(last_man_standing(alist, step))




def all_deleted(alist):
    answer = (len(alist) == 1)
    return answer

def last_man_standing(alist, step):
    
    contador = step - 1
    
    while all_deleted(alist) == False:
        
        while contador > len(alist):
            contador = contador - len(alist) # dá voltas ao circulo
    
        if contador < len(alist):
            
            next_deleted = alist[contador]
            alist.remove(next_deleted)
            contador = contador - 1 + step
            
        else: # contador = len(alist)
            
            next_deleted = alist[0]
            alist.remove(next_deleted)
            contador = step - 1
            
    return alist[0]

alist = [8, 5, 3, 4, 2, 9, 1]
step = 3
print(last_man_standing(alist, step))


Write a Python function fib(n) that returns a list 
of the first n Fibonacci numbers. 

The next number in a Fibonacci sequence 
is defined as the sum of the previous two numbers, 
and the first two numbers are defined as 0 and 1, respectively.

fib(1) should return the list: [0]
fib(5) should return the list: [0, 1, 1, 2, 3]


def fib(n):
    
    result = [0, 1] # initial values
    soma_2_anteriores = 0
    
    if n == 1:
        return [0]
    
    elif n == 2:
        return result
    
    else:
        for i in range (n-2):
            soma_2_anteriores = int(result[i]) + int(result[i+1])        
            result.append(soma_2_anteriores)
        return result

# n = 20
# print(fib(n))


Fetching the middle

Write a Python function fetch_middle(llists) that, given a list of lists llists, 
returns a new list containing the middle element from each list in llists. 
If the list's length is even, consider the middle element to be the average 
between its two central elements (i.e. for the list [1, 2, 3, 4], 
the middle element would be (2+3)/2 = 2.5).

Example:
    Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]	
    Output: [2, 5, 8.5]

def fetch_middle(llists):
    
    from math import floor as m
    
    result = [] # empty list
    middle_element = 0
    a = 0
    b = 0
    
    for x in range (0, len(llists)):
        
        comprimento = int(len(llists[x]))
        
        if comprimento%2 == 0: # se o número de elementos for par
        
            a = round((comprimento/2)-1)
            b = round(comprimento/2)
            middle_element = round(((llists[x][a]+llists[x][b])/2), 1)
            result.append(middle_element)
        
        else: # se o número de elementos for ímpar
            b = m(comprimento/2)
            a = llists[x][b]
            result.append(a)
        
    return result
            
# llists = [[1, 80, 100, 2, 8], [4, 52, 6], [7, 81, 90, 10]]
# print(fetch_middle(llists))


Bagdiff

Write a Python function bagdiff(xs, ys) 
that returns items from the first list (xs) 
that are not eliminated by a matching element in the second list (ys). 
An item in the second list may "knock out" just one matching item 
in the first list.

Example:
        Input: 	[5, 7, 11, 11, 11, 12, 13], [7, 8, 11]	
        Output: [5, 11, 11, 12, 13]
    

def bagdiff(xs, ys):
    
    for item in xs:
        if item in ys:
            xs.remove(item)
    
    return xs

xs = [5, 7, 11, 11, 11, 12, 13]
ys = [7, 8, 11]
print(bagdiff(xs, ys))


def quadratica(n):
    
    result = []
    
    for x in range (1,n):
        for y in range (1,n):
            for z in range (1,n):
                
                if ((x**2 + y**2 + z**2) == n):
                    result.append(x)
                    result.append(y)
                    result.append(z)
                    break
                
                    
    return result

n = 153
print(quadratica(n))



# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,10,1]]
# result is 3x4
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)

def acronimo(nome):
    
    result = ""
    
    alist = nome.split(" ")

    for i in range(0, len(alist)):
        
          result = result + alist[i][0]
        
    return result.upper()

nome = str(input("What's your sentense?: "))
print(acronimo(nome))




def min_path(path):
    
    for i in range (0, len(path)):
        for j in range (i+1, len(path)-2):
            
            if path[i] == "UP":
                if path[j] == "DOWN":
                    path.remove(path[i])
                    path.remove(path[j])
            elif path[i] == "DOWN":
                if path[j] == "UP":
                    path.remove(path[i])
                    path.remove(path[j])            
            elif path[i] == "LEFT":
                if path[j] == "RIGHT":
                    path.remove(path[i])
                    path.remove(path[j])            
            elif path[i] == "RIGHT":
                if path[j] == "LEFT":
                    path.remove(path[i])
                    path.remove(path[j])           
            
    return path




def min_path(path):
    
    i = 0
    
    while (i < len(path)-2):
        
        if path[i] == "LEFT": 
            if path[i+1] == "RIGHT":
                path.remove(path[i])
                path.remove(path[i])
            else:
                i = i + 1
    
        if path[i] == "RIGHT":
            if path[i+1] == "LEFT":
                path.remove(path[i])
                path.remove(path[i])
            else:
                i = i + 1
    
        if path[i] == "UP":
            if path[i+1] == "DOWN":
                path.remove(path[i])
                path.remove(path[i])
            else:
                i = i + 1
    
        if path[i] == "DOWN":
            if path[i+1] == "UP":
                path.remove(path[i])
                path.remove(path[i])
            else:
                i = i + 1
              
        
    return path





def min_path(path):
    
    a = path.index("LEFT")
    b = path.index("RIGHT")
    c = path.index("UP")
    d = path.index("DOWN")
    
    if b == a + 1:
        path.remove(path[b])
        path.remove(path[a])
        
    elif a == b + 1:
        path.remove(path[a])
        path.remove(path[b])
        
    elif c == d + 1:
        path.remove(path[c])
        path.remove(path[d])
        
    elif d == c + 1:
        path.remove(path[d])
        path.remove(path[c])
        
    else:
        return path
        
    
path = ['UP', 'DOWN', 'UP', 'LEFT', 'RIGHT']
print(min_path(path))

def min_path(path):

    i = 0
    j = len(path)

    while i < j-1:
        
        if (path[i] == "RIGHT" and path[i+1] == "LEFT") or (path[i] == "LEFT" and path[i+1] == "RIGHT"):
            path.remove(path[i])
            path.remove(path[i])
            i = i + 1
            j = j - 2
            
        elif (path[i] == "UP" and path[i+1] == "DOWN") or (path[i] == "DOWN" and path[i+1] == "UP"):
            path.remove(path[i])
            path.remove(path[i])
            i = i + 1
            j = j - 2
             
        else:
            i = i + 1
            continue
            
    return path
            
            
            
path = ['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']
print(min_path(path))


def manipulator(l, cmds):
    
    result = "" # Empty string
    
    for instruction in cmds:
        
        instruction = instruction.split(" ") # list com a instrução separada
                                              # dos números pretendidos
        
        if instruction[0] == "insert":
            l.insert(int(instruction[1]), int(instruction[2]))
        
        elif instruction[0] == "remove":
            l.remove(int(instruction[1]))
        
        elif instruction[0] == "append":
            l.append(int(instruction[1]))
            
        elif instruction[0] == "sort":
            l.sort()

        elif instruction[0] == "pop":
            l.pop()
            
        elif instruction[0] == "reverse":
            l.reverse()
            
        elif instruction[0] == "print":
            result = result + str(l) + " "
    
    result.rstrip() # Delete a last space 
    return result



def jump(l):
    
    i = 0
    counter = 0
    
    if l[l[i]] == - 1 and len(l) > 1:
        counter = counter + 1
        i = i + 2
        
    else:
        if len(l) > 1:
            i = i + 1
    
    
    return counter

l = [5, 7, 6, 3, 2, -1, 4, 1]
print(jump(l))


def zipar(number, index):
    
    answer = []
    for x in number:
        for y in index:
            answer.append(zip(x, y))
            
    return answer


def local_minima(alist, n):
       
    number = []
    index = []
    
    for i in range (0, len(alist)):
        
        if i < n-2: # extremo inferior
        
            for j in range (1, round((n-1)/2)+1): # if 5, 2 parta cada lado
        
                if 

                else:
                    continue
        
        elif i > (len(alist)-(n-2)): # extremo superior
            
            
        
        else: # recheio
            
            
        
        else:
            continue

        
        
    
    return zipar(number, index)

alist = [10, 3, 3, 14, 5, 7, 4]
n = 3
print(local_minima(alist, n))


def mult(M, N):
    
    result = ""
    
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                result[i][j] += M[i][k] * N[k][j]
    
    return result

M =[[1, 2], [4]]
N = [2, 0], [1, 2]
print(mult(M, N))


def ajusts(blist):

    for q in range (0, len(blist)):
        
        blist[q] = blist[q].lower() # all in lower case
        blist[q] = blist[q].replace(" ", "") # delete space between words
    
    return blist

def anagrams(alist):

    a = "" # caso necessite
    b = "" # "" ""
    c = "" # "" ""
    answer = []
    pairs = []
    blist = alist.copy()
    ajusts(blist)
        
    for i in range (0, len(blist)-3):
        for j in range (i+1, len(blist)-2): 
            for k in range (j+1, len(blist)-1):
            
                a = blist[i]
                b = blist[j]
                c = blist[k]
                
                if sorted(a) == sorted(b) == sorted(c): # alist[i] and alist[j] are anagrams
                   
                    pairs.append(alist[i])
                    pairs.append(alist[j])
                    pairs.append(alist[k])
                    answer.append(pairs)
                    pairs = [] # Turn into a empty list again
                    
                else:
                    continue
    
    return answer

alist = ['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']
print(anagrams(alist))

def ajustes(blist):
    
    for q in range (0, len(blist)):
        blist[q] = blist[q].lower() # all in lower case
        blist[q] = blist[q].replace(" ", "") # delete space between words
        
    for s in range (0, len(blist)):
        
        word = ''.join(sorted(blist[s]))
        blist[s] = word # ordem alfabética
        
    return blist


def anagrams(alist):

    answer = []
    pairs = []
    blist = alist.copy()
    ajustes(blist)
    
    for i in range (0, len(blist)-1):
        for j in range (i+1, len(blist)):

            if blist[i] == blist[j]:
        
                w1 = alist[i]
                w2 = alist[j]
        
                pairs.append(w1)
                pairs.append(w2)

        
            else:

                answer.append(pairs)
                pairs = []
    
    return answer

alist = ['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']
print(anagrams(alist))


def ajustes(blist):
    
    for q in range (0, len(blist)):
        blist[q] = blist[q].lower() # all in lower case
        blist[q] = blist[q].replace(" ", "") # delete space between words
        
    for s in range (0, len(blist)):
        
        word = ''.join(sorted(blist[s]))
        blist[s] = word # ordem alfabética
        
    return blist


def anagrams(alist):

    answer = []
    pairs = []
    blist = alist.copy()
    ajustes(blist)
    clist = zip(blist, alist)

    
         
    return clist

alist = ['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']
# blist = ['eeehsty', 'aet', 'eeehsty', 'aachrs', 'aet', 'aachrs', 'aet']
print(anagrams(alist))

def fazível(M, N): # Será que é possível calcular?

    a = len(M)
    b = len(M[0])
    
    c = len(N)
    d = len(N[0])
    
    return (a == d or b == c)

def mult(M, N):
    
    result = []
    pairs = []
    soma = 0
    
    if fazível(M, N):
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                for k in range(len(M[0])):
                    soma = soma + (M[k][i] * N[i][k])
                pairs.append(soma)
                
            result.append(pairs)
            pairs = []
            soma = 0
            
    return result


M = [[1, 2], [3, 4]]
N = [[2, 0], [1, 2]]
print(mult(M, N))

def fazível(M, N): # Será que é possível calcular?

    a = len(M)
    b = len(M[0])
    
    c = len(N)
    d = len(N[0])
    
    return (a == d or b == c)

def mult(M, N):
    
    result = []
    pairs = []
    soma = 0
    
    if fazível(M, N):
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                soma = 0
                for k in range(3):
                    soma = soma + (M[i][j] * N[j][i])
                pairs.append(soma)
            
    return pairs


M = [[1, 2], [3, 4]]
N = [[2, 0], [1, 2]]
print(mult(M, N))




def matriz_resultado(linhas, colunas):
    # Criação de uma matriz com um número certo de "casas" para preencher
    
    result = []
    while len(result) < linhas:
        result.append([])
        while len(result[-1]) < colunas:
            result[-1].append(0.0)
 
    return result


def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    
    return (a == d and b == c)


def mult(M, N):

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        result = matriz_resultado(a, d)
        for i in range(a):
            for j in range(d):
                total = 0
                for k in range(b):
                    total += M[i][k] * N[k][j]
                result[i][j] = total
                
        return result
     
    else:
        return []


def jump(l):
    
    i = 0
    counter = 0
    i = l[i]
    
    while i != -1:
        counter = counter + 1
        i = l[i]
        
    return counter



def local_minima (alist, n):
    
    result = []
    avaliados = round((n-n%2)/2) # Números avaliados para cada lado
    
    for (i, number) in enumerate(alist):
        
        direita = alist[i+1:i+1+avaliados]
        esquerda = alist[i-avaliados:i]
        
        if result == [] or (i - result[-1][1] > avaliados): 
            
            if direita == []: # Se está no fim da lista
            
                if number < min(esquerda) or min(esquerda) == number:
                    result.append((number, i)) # Add tuple
                    
            elif esquerda == []: # Se está no início da lista
            
                if number < min(direita) or min(direita) == number:
                    result.append((number, i)) # Add tuple
                    
            else: # Está no meio da lista, sem ser nas pontas
                
                if (number <= min(esquerda) and number <= min(direita)):
                    result.append((number, i)) # Add tuple
                    
    return result
                

alist = [2, 10, 1, 1, 7, 20, 1]
n = 5
print(local_minima(alist, n))


def ajustes(blist):
    
    for q in range (0, len(blist)):
        blist[q] = blist[q].lower() # all in lower case
        blist[q] = blist[q].replace(" ", "") # delete space between words
        
    for s in range (0, len(blist)):
        
        word = ''.join(sorted(blist[s]))
        blist[s] = word # ordem alfabética
        
    return blist


def ordem(answer):
    return answer[0].lower()
    

def anagrams(alist):

    answer = []
    blist = alist.copy()
    ajustes(blist)
    filtro = []
    
    for i in range (len(blist)):
        
        temporário = []
        
        if alist[i] in filtro:
            continue
        else:
            temporário.append(alist[i])
            
        for j in range (i+1, len(blist)):
            
            if blist[i] == blist[j] and (alist[j] not in answer):
                temporário.append(alist[j])
                filtro.append(alist[j])
                temporário = sorted(temporário)
                
        answer.append(temporário)
        
    return sorted(answer, key=ordem)

alist = ['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']
# blist = ['eeehsty', 'aet', 'eeehsty', 'aachrs', 'aet', 'aachrs', 'aet']
print(anagrams(alist))


def local_minima (alist, n):
    
    result = []
    avaliados = round((n-n%2)/2) # Números avaliados para cada lado
    
    for (i, number) in enumerate(alist):
        
        if i-avaliados < 0:
            esquerda = alist[0:i]
        else:
            esquerda = alist[i-avaliados:i]
        
        direita = alist[i+1:i+1+avaliados]
        
        if result == [] or (i - result[-1][1] > avaliados): 
            
            if direita == []: # Se está no fim da lista
            
                if number < min(esquerda) or min(esquerda) == number:
                    result.append((number, i)) # Add tuple
                    
            elif esquerda == []: # Se está no início da lista
            
                if number < min(direita) or min(direita) == number:
                    result.append((number, i)) # Add tuple
                    
            else: # Está no meio da lista, sem ser nas pontas
                
                if (number <= min(esquerda) and number <= min(direita)):
                    result.append((number, i)) # Add tuple
                    
    return result

def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    return (b == c)


def mult(M,N):
    
    matriz_produto = []

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        
        for i in range(len(M)):
            
            linha = []
            
            for j in range(len(N[0])):
                soma = 0
                for k in range (len(M[0])):
                    soma = soma + M[i][k] * N[k][j]
                        
                linha.append(soma)
            matriz_produto.append(linha)
            
        return matriz_produto
    
    else:
        return matriz_produto
    
def prod(M, N, l, c, p):
    prod = (M[l][p] * N[p][c])
    return prod



def matriz_resultado(linhas, colunas):
    # Criação de uma matriz com um número certo de "casas" para preencher
    
    result = []
    while len(result) < linhas:
        result.append([])
        while len(result[0]) < colunas:
            result[-1].append(0.0)
 
    return result


def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    return (b == c)


def mult(M, N):

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        result = matriz_resultado(a, d)
        for i in range(a):
            for j in range(d):
                total = 0
                for k in range(b):
                    total += M[i][k] * N[k][j]
                result[i][j] = total
                
        return result
     
    else:
        return []
    
    
    def matriz_resultado(linhas, colunas):
    # Criação de uma matriz com um número certo de "casas" para preencher
    
    result = []
    while len(result) < linhas:
        result.append([])
        while len(result[-1]) < colunas:
            result[-1].append(0.0)
 
    return result


def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    return (b == c)


def mult(M, N):

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        result = matriz_resultado(a, d)
        for i in range(a):
            for j in range(d):
                total = 0
                for k in range(b):
                    total += M[i][k] * N[k][j]
                result[i][j] = total
                
        return result
     
    else:
        return []


def map(pos, steps):
    
    (x, y) = pos
    
    alist = steps.split("-")
    
    for i in range(len(alist)):
        
        if alist[i] == "up":
            y = y + 1
        elif alist[i] == "down":
            y = y - 1
        elif alist[i] == "left":
            x = x - 1
        else: # alist[i] == "righ"
            x = x + 1
            
    return (x, y)

# pos = (0, 0)
# steps = "up-up-left-right-up-up"
# print(map(pos, steps))




def greatest(num):
    
    num = str(num)
    alist = num.split()
    num_result = ""
    sorted(alist, reverse=True)
    
    for i in range (len(alist)):
        
        num_result.append(alist[i])
      
    return int(num_result)

num = 310910
print(greatest(num))



def greatest(num):
    
    num = list(str(num))
    result = []
    num_final = 0
    
    for i in range(len(num)):
        result.append(int(max(num)))
        num.remove(max(num))
        
    for j in range(len(result)):
        
        num_final = num_final*10 + (result[j])
        
    
    return num_final
    

num = 99
print(greatest(num))



def exactly(s):
    
    t = ""
    answer = ""
    algo = ""
    numeros = 0
    result = f"The sequence {s} is {answer} with {algo}: {t}"
    counter = 0
    

    for i in range (len(s)):
        
        if type(s[i]) != (type(1) or "?"):
            
            continue
        
        if type(s[i]) == "?":
            counter = counter + 1
            
        elif type(s[i]) == type(1):
            numeros = numeros*10 + s[i]
            
    return (counter, numeros)

s = "acc?7??sss?3rr1??????5???5"
print(exactly(s))



def sorted_genealogia(l):
    
    alist = ["sibling", "parent", "cousin", "grandparent"]
    return sorted(l[0][1], key=alist)


def sorted_all(algo):
    
    nome, relação = algo
    algo = ("sibling" , "parent" , "cousin" , "grandparent").index(relação)

    return algo, nome


def genealogy(l):
    return sorted(l, key=sorted_all)

l = [("maria", "parent"), ("matilde", "grandparent"),
("geraldes", "grandparent"), ("carlos", "sibling"),
("paulo", "sibling"), ("artur", "grandparent"),
("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")]
print(genealogy(l))

def fib(n):
        
    from math import sqrt as r
    number = int((((1+r(5))**n)-((1-r(5))**n))/((2**n)*r(5)))
                 
    return number

def caesar(message):
    
    result = ""
    message.upper()
    
    n = 0
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for letter in message:
        
        if letter in alphabet:
            result = result + alphabet[(alphabet.index(letter) + fib(n))%26]
            
        else:
            result = result + letter
        
        n = n + 1
    
    return result.upper()

message = "HELLO WORLD!"
print(caesar(message))



def iterate_rev(names, numbers, emails):
    
    answer = ""
    result = ""
    alist = []
    
    for i in range(0, len(names)):
                    
        result = str(names[i]) + " - " + str(numbers[i]) + " - " + str(emails[i])
        alist.append(result)
        result = ""
    
    alist.reverse()
        
    for j in range(0, len(alist)):
        answer = answer + alist[j] + "/n"
        
        
    return answer
        
    
                    


names = ("ana", "bernando", "carlos")
numbers = (938421028, 916381961, 939090082)
emails=("ana.serra@gmail.com","b1999@hotmail.com", "up201945321@fe.up.pt")

print(iterate_rev(names, numbers, emails))


def groups(students):
    
    group = ()
    
    for i in range (len(students)-2):
        
        for j in range(i+1, len(students)-1):
            
            for k in range(j+1, len(students)):
                
                group = group + ((students[i], students[j], students[k]),)
                
    return group
            
students = ("Ana", "Bernardo", "Carla", "Daniel")
print(groups(students))



def order_digits(n):
    
    n = list(str(n))
    alist = []
    result = ()
    
    for i in range(len(n)):
        alist.append(int(max(n)))
        n.remove(max(n))
    
    sorted(alist, reverse=True)
    
    for item in alist:
        result = result + (item,)
    
    return result

n = 9013322
print(order_digits(n))


def sort_rule(item):
    return (100 - max(item[1]), len(item[1]), item[0])


def sort_leaders(records):
    return tuple(sorted(records, key=sort_rule, reverse=False))

# records = (('João', (80, 90, 100)), ('Ana', (90, 100)), ('José',
# (100,)), ('Ana', (50, 90)), ('Rui', (50, 90)))
# print(sort_leaders(records))
    
    

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



def iterate_rev(names, numbers, emails):
    
    result = ""
    
    for i in range(len(names)):
        result = "{} - {} - {}\n{}".format(names[i], numbers[i], emails[i], result)

    return result

# names = ("ana", "bernardo", "carlos")
# numbers = (938421028, 916381961, 939090082)
# emails=("ana.serra@gmail.com", "b1999@hotmail.com", "up201945321@fe.up.pt")
# print(iterate_rev(names, numbers, emails))


def groups(students):

    result = ()
    
    for i in range(0, len(students)):
        for j in range(i+1, len(students)):
            for k in range(j+1, len(students)):
                
                result = result + ((students[i], students[j], students[k]), )
    
    return result


# students = ('Ana', 'Bernardo', 'Carla', 'Daniel')
# print(groups(students))


def order_digits(n):
    
    n = list(str(n))
    alist = []
    result = ()
    
    for i in range(len(n)):
        alist.append(int(max(n)))
        n.remove(max(n))
    
    sorted(alist, reverse=True)
    
    for item in alist:
        result = result + (item,)
    
    return result

# n = 9013322
# print(order_digits(n))


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



def matriz_resultado(linhas, colunas):
    # Criação de uma matriz com um número certo de "casas" para preencher
    
    result = []
    while len(result) < linhas:
        result.append([])
        while len(result[-1]) < colunas:
            result[-1].append([])
 
    return result


def fazível (a, b, c, d):
    # Verifica se a matriz produto é possível
    return (b == c)


def mult(M, N):

    a = len(M)
    b = len(M[0])
    c = len(N)
    d = len(N[0])
    
    if fazível(a, b, c, d):
        result = matriz_resultado(a, d) # Matriz solução vazia
        for i in range(a):
            for j in range(d):
                total = 0
                for k in range(b):
                    total = total + M[i][k] * N[k][j]
                result[i][j] = total
                
        return result
     
    else:
        return []


def fact(n):
    
    if n == 1:
        return 1
    else:
        return (n*fact(n-1))
    
print(fact(100))


Re7


def sparse_dot_product(dict1, dict2):
    
    soma = 0
    
    for key1 in dict1:
        for key2 in dict2:
            
            if key1 == key2:
                soma = soma + dict1[key1] * dict2[key2]
            else:
                soma = soma + 0
    
    return soma

dict1 = {1: 3, 7: 1}
dict2 = {1: 3, 7: 1}
print(sparse_dot_product(dict1, dict2))


Roman to decimal

def roman_to_integer(a_string):
    
    decimal = 0
    a_string = a_string.upper()
    
    dicta = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    for letter in a_string:
        
        if letter in dicta.keys():
            decimal = decimal + dicta[letter]
        else:
            continue
    
    return decimal

# a_string = "vii"
# print(roman_to_integer(a_string))



2

def collisions(alist):
    
    blist = [] # Vai conter as somas de dígitos de cada número
    clist = [] # Vai conter os %8 de blist
    final_dict = {} # dicionário formado pela clist
    
    for number in alist:
        
        if len(str(number)) == 1:
            blist.append(number)
            continue
        
        else:
            soma = 0
            while number > 9:
                digit = number%10
                soma = soma + digit
                number = number//10
             
            soma = soma + number    
            blist.append(soma)
            soma = 0 # Null
            
            
    for number in blist:
        clist.append(number%8)
        
    # formar o dicionário correspondente
    
    for number in clist:
        final_dict[number] = final_dict.get(number, 0) + 1 
    
    return final_dict

# alist = [15, 3, 10, 72, 9, 8, 20, 12]
# print(collisions(alist))



Roman to decimal

def roman_to_integer(a_string):
    
    decimal = 0
    a_string = a_string.upper() # Só pa confirmar
    
    dicta = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    
    # A letra está no dicionário -> traduz
    
    for i in range(len(a_string)):
            
        if i > 0 and dicta[a_string[i]] > dicta[a_string[i-1]]:
            # Casos do tipo IV, IX ... 
                
            decimal = decimal +  dicta[a_string[i]] - (dicta[a_string[i-1]] + dicta[a_string[i-1]])
            # Retira o valor adicionado anteriormente ao decimal e a diferença entre i e i-1
        
        else:
            # Casos do tipo normal: III, VIII, XVIII
            decimal = decimal + dicta[a_string[i]]

    return decimal

a_string = "vii"
print(roman_to_integer(a_string))


4 Isomorfic strings

def same_size(astring1, astring2):
    return (len(astring1) == len(astring2))


def is_isomorphic(astring1, astring2):
    
    dict1 = {} # letras de astring 1
    dict2 = {} # letras de astring 2
    
    for i, value in enumerate(astring1):
        if value in dict1:
            
            if astring2[i] != dict1[value]:
                return False
        else:
            dict1[value] = astring2[i]
            
        if astring2[i] in dict2:
            
            if value != dict2[astring2[i]]:
                return False
        else:
            dict2[astring2[i]] = value
            
    return True


def isomorphic(astring1, astring2):
    
    alist = []
    blist = []
    letras_pares = ()
    pairs = []
    
    if same_size(astring1, astring2):
        
        for letter in astring1:
            alist.append(letter)
            
        for letter in astring2:
            blist.append(letter)
            
        for x in range(len(alist)):
            for y in range(len(blist)):
                if x == y:
                    letras_pares = (alist[x], blist[y])
                else:
                    continue
                
            if letras_pares not in pairs:
                pairs.append(letras_pares)
        
        resposta_verdadeira = f"'{astring1}' and '{astring2}' are isomorphic because we can map: {pairs}"
        resposta_falsa = f"'{astring1}' and '{astring2}' are not isomorphic"
        
        return resposta_verdadeira if is_isomorphic(astring1, astring2) else resposta_falsa
    
    return #None

# astring1 = 'turtle'
# astring2 = 'tletur'
# print(isomorphic(astring1, astring2))


def logic(s, operations):
    
    for key in operations.keys():
        set_local = operations[key]
        
        if len(set_local) > len(s):
            
            if key == 'and':
                s = set_local.intersection(s)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = set_local.difference(s)
                
            else: # key == "xor"
                s = set_local ^ s 
                
        else:
            
            if key == 'and':
                s = s.intersection(set_local)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = s.diference(set_local)
                
            else: # key == "xor"
                s = s ^ set_local           
        
    return s

s = {1, 2, 3}
operations = {'and': {1}}
print(logic(s, operations))

string = "banana"
print(string[::-1])

for idx, letter in enumerate(string):
    string = string[:idx] + string[idx+1:]
    if string[idx] == "a":
        print(string[:idx] + string[idx+1:])

print("zebra" < "banana")

print("Zebra" < "banana")

print("zebra" < "Banana")



astring = "wordqualquer"
lista = []
for letter in astring:
    if letter not in lista:
        lista.append(letter) 
    
    
print(lista)
    

from math import pi as p

def circle_stats(r):
    """ Return (circumference, area) of a circle of radius r """
    circumference = 2 * p * r
    area = p * r * r
    return (circumference, area)

print(circle_stats(1))


tup1 = (12, 34.56)

  # Following action is not valid for tuples
print(tup1[0])

  # So let's create a new tuple as follows

print(tup1)

def sort_inverse(alist):
    return alist.reverse()

alist = [1, 2, 3, 4, 5]

print(sorted(alist, key=sort_inverse))


def logic(s, operations):
    
    for key in operations.keys():
        set_local = operations[key]
        
        if len(set_local) > len(s):
            
            if key == 'and':
                s = set_local.intersection(s)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = set_local.difference(s)
                
            else: # key == "xor"
                s = set_local ^ s
                
        else:
            
            if key == 'and':
                s = s.intersection(set_local)
                
            elif key == 'or':
                s = s | set_local
                
            elif key == 'not':
                s = s.diference(set_local)
                
            else: # key == "xor"
                s = s ^ set_local           
        
    return s

lista = []
for i in range(1000):
    
    if len(lista)<100:
        lista.append(i)
        
print(lista)

name = 'Fábio Araújo de Sá'

#print(name)
#print(name[0])
def formal(name):
    name = name.split()
    last_name = name[len(name)-1]
#    print(last_name[0])
    result =str(last_name)+", "
    teste = result
    for l in name:
#        print(l[0]+".")
        if l.istitle():
            lista_tit = l[0]
            if lista_tit == last_name[0]:
                continue
            else:
                teste +=lista_tit+". "
    return teste
        
treino = formal(name)
print(treino)


name = 'Augusto Sousa Coutinho'

def formal(name):
    
    
    alist = name.split()
    result = ""
    
    result = result + alist[-1] + ", "
    
    for i in range(0, len(alist)-1):
        result = result + alist[i][0].upper() + ". "
    
    
    
    return result

print(formal(name))
    
    
    
def rm_letter_rev(l, astr):
    l = l.upper()
    for letter in astr:
        if letter.isalpha() and ((letter.upper() or letter.lower()) == l or letter == " "):
            astr = astr.replace(letter, "")
        else:
            astr = astr.replace(l, "")
        
    return astr[::-1]

l='a'

astr = 'a nut for a jar of tuna'

result = rm_letter_rev(l,astr)

print(result)    


    
from itertools import permutations as p

def brute_force(f, l):
    l1= [i[0]+i[1]+i[2] for i in p(l,3)]
    return list(filter(f,l1))

print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))
    
import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.fillcolor("red")
tess.pensize(3)



for a in xs:
    drawBar(tess, a)

wn.exitonclick()
    
def unique(atuple):#my initial idea
    l_tuple = atuple
    l_tuple = set(l_tuple)
    l_tuple = tuple(sorted(l_tuple))
    return l_tuple

def unique2(atuple):#miguel's help
    return tuple(sorted(set(atuple)))

def my_unique(atuple):
    
    resposta = ()
    for number in atuple:
        if number not in resposta:
            resposta = (number,) + resposta
            
    return tuple(sorted(resposta, reverse=True))
    
atuple = (8, 8, 1, 3, 1, 3, 5)
print(my_unique(atuple))
    

def inner(u,v):
    result = 0
    for i in range(len(u)):
        result +=u[i]*v[i]
    return result

u= [1, 2, 3, 4, 5]
v= [2, 3, 4, 5, 6]
print(inner(u,v))

def aux_checker(matrix,word,row,letter):
    #base case
    if not word:
        return True
    elif word:
        for rows in range(row-1,row+2):
            for lines in range(letter-1,letter+2):
                if lines >= 0 and rows >= 0 and rows < len(matrix) and lines < len(matrix) and word[0] == matrix[rows][lines]:
                    matrix[rows][lines] == ''
                    if not aux_checker(matrix,word[1:],rows,lines):
                        continue
                    else:
                        return aux_checker(matrix,word[1:],rows,lines)

def soup(matrix,word):
    for row in range(len(matrix)):
        for letter in range(len(matrix[row])):
            if matrix[row-1][letter-1] == word[0]:
                #call to the recursive function
                if aux_checker(matrix,word[1:],row-1,letter-1):
                    return f"{chr(ord('A')+row-1)}{letter}"

mx = (('X', 'A', 'B', 'N', 'T', 'O'),
      ('Y', 'T', 'N', 'R', 'I', 'T'),
      ('U', 'P', 'O', 'M', 'D', 'S'),
      ('I', 'O', 'H', 'U', 'O', 'O'),
      ('R', 'T', 'E', 'L', 'Q', 'X'),
      ('I', 'W', 'J', 'K', 'P', 'Z'))
print(soup(mx, 'HELLO'))

PE02

def is_armstrong(n):     
    
    aux = n
    soma = 0
    
    while aux:
        
        soma = soma + (aux%10)**3
        aux = aux//10
    
    return (soma == n)

def reverse_subtuples(alist):
    
    clist = []
    for i in range(len(alist)):
        blist = list(alist[i])
        blist.reverse()
        clist.append(tuple(blist))
    
    return clist

def which_are_in(l1, l2):
    
    result = []
    
    for item1 in l1:
        for item2 in l2:
            if item1 in item2:
                if item1 not in result:
                    result.append(item1)
                
    
    
    return sorted(result)

def moving_average(alist, n):
    
    result = []
    
    if len(alist) < 3 or n < 3:
        return result
    
    else:
    
        nei = n//2
        for i in range(nei, len(alist)-nei):
            soma = 0
            for j in range(1, nei+1):  
                soma = soma + alist[i+j] + alist[i-j]
            average = round(soma/(nei*2), 2)    
            result.append(average)
            
        return result 
    
    
def genealogy(l1):
    
    pat_sibling = [] # colocar os nomes "iguais"
    pat_parent = []
    pat_cousin = []
    pat_grandparent = []
    total = []
    
    
    for i in range(len(l1)):
        
        if l1[i][1] == "sibling":
            pat_sibling.append(l1[i][0])
            
        elif l1[i][1] == "parent":
            pat_parent.append(l1[i][0])
            
        elif l1[i][1] == "cousin":
            pat_cousin.append(l1[i][0])
            
        elif l1[i][1] == "grandparent":
            pat_grandparent.append(l1[i][0])
            
    
    answer1 = (sorted(pat_sibling), "sibling")
    answer2 = (sorted(pat_parent), "parent")
    answer3 = (sorted(pat_cousin), "cousin")
    answer4 = (sorted(pat_grandparent), "grandparent")
    
    total.append(answer1)
    total.append(answer2)
    total.append(answer3)
    total.append(answer4)
    
#    for j in range(len(total)):
#        if total[j][0] == []:
#            total.remove(total[j])

    for item in total:
        
        if item == ([], "sibling"):
            total.remove(item)
        elif item == ([], "parent"):
            total.remove(item)
        elif item == ([], "cousin"):
            total.remove(item)
        elif item == ([], "grandparent"):
            total.remove(item)

    for item in total:
        
        if item == ([], "sibling"):
            total.remove(item)
        elif item == ([], "parent"):
            total.remove(item)
        elif item == ([], "cousin"):
            total.remove(item)
        elif item == ([], "grandparent"):
            total.remove(item)
        
        
    return total


Play 7
Academy Awards
key in d - chamar as keys
key in d.value() - chamar os valores das keys


def academy_awards(alist):
    
    result = {}
    for item in alist:
        result[item[1]] = result.get(item[1], 0) + 1 

    return result

def lost_element(s1, s2):
    n = s1.difference(s2) if len(s1) > len(s2) else s2.difference(s1)
    return n.pop()


s1 = {1, 4, 5, 7, 9}
s2 = {4, 5, 7, 9}

print(lost_element(s1, s2))

def most_frequent(alist):
    
    result = {}
    chaves = []
    for item in alist:
        result[item] = result.get(item, 0) + 1
        
    for (key, value) in result.items():
        if result[key] == max(result.values()):
            chaves.append(key)
        
    return max(chaves)

alist = [-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]
# result = {-1: 4, 2: 2, 5: 2, 3: 3, 4: 3}
print(most_frequent(alist))


4

def ordem(result):
    return result[1]

def sort_by_value(dict):
    
    result = []
    atuple = ()
    for key, value in dict.items():
        atuple = (key, value)
        result.append(atuple)
    
    return sorted(result, key=ordem)


dict = {"Magenta":"#FF00FF", "Red": "#FF0000", "White":"#FFFFFF"}
print(sort_by_value(dict))


5

def change(money):
    
    porquinho_mealheiro = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    
    for dinheiro, quantidade in porquinho_mealheiro.items():
        
        porquinho_mealheiro[dinheiro] = quantidade + money//dinheiro
        money = round(money%dinheiro, 2)
    
    return porquinho_mealheiro

print(change(7.71))

Create a python function 13331 p exeplo

MDIS em Excell

def is_prime(n):
    # Usando o algoritmo do Crivo de Eratóstenes
    
    from math import sqrt as r
    
    prime_list = [2]
    answer = True
    
    for x in range(3, round(r(n))+1):
        for y in range (2, x):
            if x % y == 0:
                break
        else:
            prime_list.append(x)
            
    for number in prime_list:
        answer = answer and (n % number != 0)    
    
    return "O número não é primo!" if answer == False else "O número é primo!"

n = int(input("Valor: "))
print(is_prime(n))


Play7 - 06

def fight(heroes, villain):
    
    # Escolha dos heróis para lutar
    heroes_that_fight = []
    for heroe in heroes:   
        if heroe['category'] == villain['category']:
            heroes_that_fight.append(heroe)
    
    #Luta
    bons_venceram = False
    for heroe in heroes_that_fight:
        
            if heroe["health"] < villain["health"]:
                villain["health"] = villain["health"] - round(((heroe["health"])/2), 2)
                bons_venceram = bons_venceram and False
            
            else:
                bons_venceram = bons_venceram or True
                break
            
    name_good = heroe["name"]
    score_good = heroe["score"] + 1
    good_wins = f"{name_good} defeated the villain and now has a score of {score_good}"
    bad_wins = villain['name'] + " prevailed with "+ str(villain["health"]) + "HP left"
    
    return good_wins if bons_venceram else bad_wins

heroes = [{'name': 'Genos', 'health': 5500, 'category': 'S', 'score': 0}, {'name': 'King', 'health': 7000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}]
villain = {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}
print(fight(heroes, villain))

7

def treasure(clues):
    
    tesouro = (0, 0)
    while tesouro in clues:
        # retirar a key correspondente
        tesouro = clues.pop(tesouro)
    
    return tesouro

clues = {(-1, 1): (0, 0), (0, 0): (1, 0), (1, 0): (-1, 1)}
print(treasure(clues))

8

def ajustes(budget, products, wishlist, preço_total):
  
    # Ordem da lista: valor menor --> valor maior
    preços_ordenados = sorted(products.items(), key = lambda a: a[1])
    
    # Nova combinação das compras
    comprados = wishlist.copy()
    for produto, valor in preços_ordenados:
        if produto in comprados.keys():
            
            while preço_total > budget and comprados[produto] > 0 and produto in wishlist:
                preço_total -= valor
                comprados[produto] += -1
                
            # Eliminar o produto do set quando este já não existe
            if comprados[produto] == 0:
                del comprados[produto]
                
    return comprados
    
def budgeting(budget, products, wishlist):
    
    preço_total = 0
    for produto, quantidade in wishlist.items():
        preço_total = preço_total + products[produto]*quantidade
    
    return wishlist if preço_total < budget else ajustes(budget, products, wishlist, preço_total)
    
budget = 1200
products = {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}
wishlist = {'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}
print(budgeting(budget, products, wishlist))



9

def complete_pairs(s1, s2):
    
    from string import ascii_lowercase as abc
    solution = []
    
    for string_1 in s1:
        for string_2 in s2:
            a_string = string_1 + string_2
            if set(abc) < set(a_string) or set(a_string) == set(abc):
                solution.append(a_string)
    
    solution = set(solution)
    return solution

s1 = {'graby', 'yesbg'}
s2 = {'atqswrlxhikeczfnpjdvmou'}
print(complete_pairs(s1, s2))


10


def tf_count(N, n, times):
    # Calculates tf * idf form
    
    from math import log as l
    idf = l(N/n) if n!= 0 else 0
    
    return round(idf*times, 3)

def tfidf(documents):
    
    # Sorted words by occurrence without repetition
    words = []
    for sentence in documents:
        sentence = sentence.lower()
        palavras_separadas = sentence.split()
        for word in palavras_separadas:
            if word not in words:
                words.append(word.lower())
    
    # A dict with all of words
    tf_idf = {}
    for word in words:
        tf_idf[word] = tf_idf.get(word, "something_beautifull")

    # Counter 1 - How many times the "word" appears in the documents' sentences?
    def qtd(word):
        
        n = 0
        for sentence in documents:
            sentence = sentence.lower()
            if word in sentence.split():
                n = n + 1
            else:
                continue
            
        return n
        
    # Counter 2 - How many times the "word" appears in each documents' sentences?
    for word in words:
        counter = []
        for sentence in documents:
            sentence = sentence.lower()
            times = 0
            for x in range(len(sentence.split())):
                if (sentence.split())[x] == word:
                        times = times + 1
                else:
                    continue
            N = len(documents)
            counter.append(tf_count(N, qtd(word), times))
        tf_idf[word] = counter
    
    return tf_idf


documents = ['To be or not to be', 'Impossible is a word to be found only in the dictionary of fools', 'There is nothing impossible to him who will try']
print(tfidf(documents))


RE08 Recursion

1 Flatten

def flatten(alist):
    
    final_list = []
    
    for item in alist:
        
        if type(item) is list:
            final_list = final_list + flatten(item)
        
        else:
            final_list.append(item)
            
    return final_list


alist = ['Hello', [2, [[], False]], [True]]
print(flatten(alist))


2 Calculator

def calculator(expr):
    
    empty_tuple = ()
    for conta in expr:
        
        if type(conta) == type(empty_tuple):
            # Se ainda não chegou ao fim da recursão
            empty_tuple = empty_tuple + (calculator(conta), ) # Separa em partes
            
        else:
            # Se já chegou à parte mínima
            resultado = 0
            empty_tuple = empty_tuple + (conta, )
            
            if len(empty_tuple) == 3: # (Number=0, operação=1, number=2)
                # Contas
                
                if empty_tuple[1] == "*": # Multiplicação
                    resultado = resultado + empty_tuple[0] * empty_tuple[2]
                
                if empty_tuple[1] == "+": # Adição
                    resultado = resultado + empty_tuple[0] + empty_tuple[2]
                    
                if empty_tuple[1] == "-": # Subtração
                    resultado = resultado + empty_tuple[0] - empty_tuple[2]
            
            
    return expr if type(expr) != type(()) else resultado

expr = ((1, '+', 2), '*', 3)
print(calculator(expr))



def rec_multiplicative_persistence(n):
    
    c = 0
    
    if len(str(n)) == 1:
        return c
    
    else:
        aux = 1
        aux = (n % 10) * aux
        n = n // 10
        n = aux
        c = c + 1
        return c + rec_multiplicative_persistence(n)    

print(rec_multiplicative_persistence(39))

Defining function
def persistence(n):

    my_n = str(n) #Converting to string (iterable)*
    first_time = True #Boolean variable for while-loop*
    digit_list = [] #Initial empty list*
    product = 1 #In order to calculate product in filled list*
    count = 0 #Count of multiplicative persistence*

    if n < 10 and n > -10: #Base cases*
        count += 1
        return 1

    else:
        while first_time or len(digit_list) > 1:   #If first time or until number of digits greater than 1*
            first_time = False#No longer first time*
            for digit in my_n:
                digit_list.append(digit) #Append digits to list
            for digit in digit_list:
                product *= int(digit)  #Calculate product

            count += 1 #Increase count*

            break  #Exit while loop

        persistence(product)  #recursive operation

        return count

print(persistence(39))



num = int(input(123))
count = 0
while num > 9:
    aux = 1
    while num != 0:
        aux = (num % 10) * aux
        num = num // 10
        num = aux
        count += 1
print(count)


def rec_multiplicative_persistence(n):
    
    contador = 0
    
    if len(n) == 1:
        return contador
    else:
        contador = contador + 1
        return retira_numeros(n)
    
    return contador

def contador(n):
    
    c = 0
    
    if
        c = c + 1
        
    return c



def rec_multiplicative_persistence(n):
    
    if len(str(n)) == 1:
        return 0
    else:
        return 1 + retira_numeros(n)

def retira_numeros(n):
    
    if len(str(n)) == 1:
        return n
    else:
        return n%10 * retira_numeros(n//10)

print(rec_multiplicative_persistence(12334567))


Test Recursion 4 Files

    
def file_finder(dirs, file_name):
    
    if dirs == file_name:
        # Se encontrar logo o pretendido:
            return file_name
         
    for i in dirs[1:]:
        # entra no segundo pedaço:
        if file_finder(i, file_name) != None:
            # Se houver algum documento dentro:
            a = dirs[0]
            b = file_finder(i, file_name)
            return f"{a}/{b}"
            # String que determina o diretório com barras

dirs = ["home",
          ["Documents",
              [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
              [ "Python", "hello_world.py", "readme.md" ],
          ],
          ["Downloads",
              [ "Movies",
                [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                "1.avi", "22", "001.mp4"
              ],
          ],
          "tmp.txt", "page.html"
        ]

file_name = "BreakingBad.mp4"

print(file_finder(dirs, file_name))


def letras(matrix, x, y, word):
    
    não_continua = True
    
    if matrix[x][y] == word[0]:
        
        if len(word) == 1:
            return não_continua # Acaba aqui
        
        else:
            
            vizinhança_procurada = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
            
            for (z, t) in vizinhança_procurada:
                
                if matrix[z][t] == word[1] and z >= 0 and t >=0:
                    return não_continua and letras(matrix, z, t, word[1:])
                else:
                    continue
                
                
def coordenadas(x, y):
    
    from string import ascii_letters as abc
    
    coordenada_x = abc[x]
    coordenada_y = y + 1
    
    return f"{coordenada_x}{coordenada_y}"


def soup(matrix, word):
    
    n_linhas = len(matrix)
    n_colunas = len(matrix)
    
    for x in range(n_linhas): 
        for y in range(n_colunas):  
            if letras(matrix, x, y, word): # Se encontrar a palavra pretendida
                
                return coordenadas(x, y).upper()
        
    
matrix = (('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'), ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z'))
word = 'PORTO'
print(soup(matrix, word))
    
    
    
def rec_multiplicative_persistence(n):
    
    if len(str(n)) == 1:
        return 0
    else:
        passo_seguinte = retira_numeros(n)
        return 1 + rec_multiplicative_persistence(passo_seguinte)

def retira_numeros(n):
    
    if len(str(n)) == 1:
        return n
    else:
        return n%10 * retira_numeros(n//10)

print(rec_multiplicative_persistence(277777788888899))


    
def calculator(expr):
    
    if type(expr) == type(1): #Se for um inteiro
        return expr
    
    else:
        
        seguinte = expr[1] # Se houver mais tuples
        
        if seguinte == '+': # Soma
            return calculator(expr[0]) + calculator(expr[2])
        
        elif seguinte == '*': # Multiplicação
            return calculator(expr[0]) * calculator(expr[2])
        
        elif seguinte == '-': # Subtração
            return calculator(expr[0]) - calculator(expr[2])


def letras(matrix, x, y, word):
    
    não_continua = True
    
    if matrix[x][y] == word[0]:
        
        if len(word) == 1:
            return não_continua # Acaba aqui
        
        else:
            
            vizinhança_procurada = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1),(x-1,y),(x+1,y)]
            
            for (z, t) in vizinhança_procurada:
                
                if matrix[z][t] == word[1] and z >= 0 and t >=0:
                    return não_continua and letras(matrix, z, t, word[1:])
                else:
                    continue
                
                
def coordenadas(x, y):
    
    from string import ascii_letters as abc
    
    coordenada_x = abc[x]
    coordenada_y = y + 1
    
    return f"{coordenada_x}{coordenada_y}"


def soup(matrix, word):
    
    n_linhas = len(matrix)
    n_colunas = len(matrix)
    
    for x in range(n_linhas): 
        for y in range(n_colunas):  
            if letras(matrix, x, y, word): # Se encontrar a palavra pretendida
                
                return coordenadas(x, y).upper()
            

RE09


def sort_by_f(alist):
    return sorted(alist, key=lambda x: 5-x if x>= 5 else x)

def square_r(number):
    return number**2

def map_reduce(n1, n2):
    
    from functools import reduce as r
    
    numbers = [number for number in range(n1, n2) if number%2 == 1] # All odd numbers between n1 and n2
    squares = list(map(square_r, numbers)) # Sqrt using map
    
    soma_or_multi = r((lambda x, y: x * y if x*y<50 else x+y), squares)

    return soma_or_multi


n1 = 10
n2 = 24
print(map_reduce(n1, n2)) 
        
    
def pegar_nas_coisas_importantes(orders):
    return (item[0], item[1], item[3]) for item in orders
    
def invoice_totals(orders, min):
    
    final_list = list(map(pegar_nas_coisas_importantes, orders))
    
    return final_list

    
orders = [[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8]]
min = 500
print(invoice_totals(orders, min))
    

def generator(intlist):
    
    alist = []
    blist = [alist.append(number) for number in (range(n1, n2) for (n1, n2) in intlist)]
    
    return blist

intlist=[(1,1), (3,5), (10,15)]
print(generator(intlist))




def coisa(x, y, min):
    return (x*y if x*y>min else x*y+10)
    
def invoice_totals(orders, min):
    return [(item[0], coisa(item[2], item[3], min)) for item in orders]

    
orders = [[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8]]
min = 500
print(invoice_totals(orders, min))
    
    
def conc(l1,l2):
    # Add/conc item in l2 and item in l1 if item[0] in l1 not in item[0] in l2
    alist = [x for x in l2] + [y for y in l1 if (y[0] not in (z[0] for z in l2))]  
    return alist 
    
def override(l1, l2):
    # Sorted by firts letter in tuple
    return sorted(conc(l1, l2), key = lambda x: x[0] )


l1 = [('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')]
l2 = [('a', 'c'), ('b', 'd')]

print(override(l1, l2))
    
def retirar(x, y, z):
    return reduce_map_filter()


def reduce_map_filter(args):
    
    if type(args[2]) == type(()):
        return reduce_map_filter(args[2])
  
    
    else:
    
        if args[0] == "filter" :
            # Faz a função filter de args[1] sobre a lista args[2]
            return list(filter(args[1], args[2]))
        
        
        if args[0] == "map" :
            # Faz a função args[1] sobre a lista args[2]
            return list(map(args[1], args[2]))
    
        
        if args[0] == "reduce" :
            # Reduz a função args[1] sobre a lista arg[2]
            from functools import reduce as r
            return int(r(args[1], args[2]))
    
    
def double(s):
    return s + s
double = double
print(double("coiso"), double("isto"))    
    

def chegou_ao_mínimo(something):
    return type(something[-1]) == type([1,2,3])


def reduce_map_filter(args):

    final = args
    
    if chegou_ao_mínimo(args):
        # Se chegar ao fim da recursão e encontrar uma lista no item 3:

        if args[-3] == "filter" :
            # Faz a função filter de args[1] sobre a lista args[2]
            return list(filter(args[1], args[2]))
                
                
        if args[-3] == "map" :
            # Faz a função args[1] sobre a lista args[2]
            return list(map(args[1], args[2]))
            
                
        if args[-3] == "reduce" :
            # Reduz a função args[1] sobre a lista arg[2]
            from functools import reduce as r
            return int(r(args[1], args[2]))
        
        
    else:
        if type(final[-1]) == type(("something")): # Is it is a tuple
            final = reduce_map_filter(args[-1])
        
    
args = ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3]))
print(reduce_map_filter(args))
    
    
from math import pi, cos, sin
    
astring = ""
resultados = []
a = ["0", "pi/6", "pi/4", "pi/3", "pi/2", "2*pi/3", "3*pi/4", "pi"]
angulos = [0, pi/6, pi/4, pi/3, pi/2, 2*pi/3, 3*pi/4, pi]

for angulo in angulos:
    resultados.append(round(1 + cos(angulo), 3))
    
final_list = list(zip(a, resultados))
    
for a, resultado in final_list:
    print(a + "  ||  " + str(resultado))


def chegou_ao_mínimo(something):
    return type(something[-1]) == type([1,2,3])

def reduce_map_filter(args):
    
    final = args
    
    if chegou_ao_mínimo(final):
        # Se chegar ao fim da recursão e encontrar uma lista no item 3:

        if final[0] == "filter" :
            # Faz a função filter de args[1] sobre a lista args[2]
            return list(filter(final[1], final[2]))
                
                
        if final[0] == "map" :
            # Faz a função args[1] sobre a lista args[2]
            return list(map(final[1], final[2]))
            
                
        if final[0] == "reduce" :
            # Reduz a função args[1] sobre a lista arg[2]
            from functools import reduce as r
            return int(r(final[1], final[2]))

    else:
        passo_seguinte = final[-1]
        l = reduce_map_filter(passo_seguinte)
        return reduce_map_filter((final[0],final[1],l))

args = ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3]))
print(reduce_map_filter(args))


x = map(lambda x: 2*x, [1,2,3]) #lazy
l = list(x)
print(l)
print(l)

import sympy
print(sympy.isprime(12334455))

from math import sqrt as r
# Quase uma fatorização do número n de acordo com o Crivo de Eratóstenes
n = 1610978767
for i in range(2, round(r(n))+1):
    if n%i == 0:
        print (i)

print(pow(12, 11, 17))

# from math import gdc as mdc
# print(mdc(27,1))

from functools import reduce
def auxiliar_reduce_map_filter(args):
    final = args
    # Não consegues mudar o args mas sim uma cópia dele. O arg é "imutável".
    if type(final[2]) is not tuple:
        if (final[0]) == "map":
            return list(map(final[1], final[2]))
        
        elif (final[0]) == "filter":
            return list(filter(final[1], final[2]))
            
        elif (final[0]) == "reduce":
            return int(reduce(final[1], final[2]))
            # No último teste púplico retorna um número e não uma lista.
            # Ou seja, de return list passa para return int (número inteiro)
    
    else:
        final = final[2] # A parte que o programa vai tratar agora vai ser a parte do tuple
        conta_posterior = auxiliar_reduce_map_filter(final) # O programa vai resolver o que está lá dentro
        return auxiliar_reduce_map_filter((final[0], final[1], conta_posterior))
        # Resolve depois tudo: chamando a função, a operação e o número que saiu da conta anterior
        
args = ('reduce', lambda a,b: a+b, ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3])))
print(auxiliar_reduce_map_filter(args))

import statistics
import random
import math

#SQUARE 2x2
square_lenght = 2
square_area = square_lenght**2

#CIRCLE 
r_circle = 1

#NEEDLES IN CIRCLE
def needles_in(amount):
    needles_circle = 0
    for i in range (0, amount, 1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt((x**2) + (y**2)) < r_circle:
            needles_circle += 1
    return needles_circle

#MONTE CARLO FORMULA
def monte_carlo(needles_square):
    return (square_area * needles_in(needles_square)) / needles_square

def main():
    print(monte_carlo(54168168516))

if __name__ == "__main__":
    main()

                 Recursion - Play 08

def gcd_rec(n1, n2):
    
    resto = n1%n2
    if resto == 0:
        return n2
    
    else:
        return gcd_rec(n2,resto)

# Other option without recursion
# def gcd_rec(n1, n2):
#     from math import gcd as euclid
#     return euclid(n1,n2)


def is_odd(a, b):
    b = b - 1
    resto = (juggler(a,b))%2
    return resto != 0

def juggler(n, p):
    
    if p == 0:
        return n
    
    else:
        from math import floor as f
        
        if is_odd (n, p):
            return f((juggler(n, p-1))**(3/2))
        else:
            return f((juggler(n, p-1))**(1/2))
        
def sum_digits_rec(n):
    
    if len(str(n)) == 1:
        return n 
    
    else:
        return n%10 + sum_digits_rec(n//10)

def separação(atuple):
    
    total = []  
    total.append(atuple)
    atuple = list(atuple)
    
    for item in atuple:
        if type(item) != type(("f","a","b")):
            continue
        else:
            subtotal = biggest_member(item) # Fragmentação
            total.append(item)
            total.append(subtotal)
            
    return total

def biggest_member(atuple):

    all_tuples = separação(atuple)
    item_max = all_tuples[0]
    
    for item in all_tuples:
        if len(item) > len(item_max):
            item_max = item
    
    return item_max
        
atuple = ((6, (10, 20, 5, 7, 50, 10, 70, -2), 8, 9, 10, 11), 5, (2, 3, 1))
print(biggest_member(atuple))


def find_treasure(pos, steps):
    
    if len(steps) == 0:
        return pos
    
    else:
        (x, y) = pos
        
        if steps[0] == "up":
            y = y + 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
        if steps[0] == "down":
            y = y - 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps) 
        if steps[0] == "left":
            x = x - 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
        if steps[0] == "right":
            x = x + 1
            steps.remove(steps[0])
            return find_treasure((x,y), steps)
    
    
def last_man_standing(alist, step, initial_idx=0):
    
    if len(alist) == 1:
        return alist[0]
    
    else:
        idx = (step-1+initial_idx)%(len(alist))
        alist.remove(alist[idx])
        return last_man_standing(alist, step, idx)

Python3 implementation of the  
above approach  
  
# Function to print the output  
def printTheArray(arr, n):  
  
    for i in range(0, n):  
        print(arr[i], end = " ")  
      
    print() 
  
# Function to generate all binary strings  
def generateAllBinaryStrings(n, arr, i):  
  
    if i == n: 
        printTheArray(arr, n)  
        return
      
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)  
  
# Driver Code  
if __name__ == "__main__":  
  
    n = 4
    arr = [None] * n  
  
    # Print all binary strings  
    generateAllBinaryStrings(n, arr, 0)  
  
dict_numbers = {1:2, 2:3}
def no_consecutives1(k):
    # Fibonacci sequence with dict

    if k in dict_numbers:
        return dict_numbers[k]
    
    else:
        valor = no_consecutives1(k-1) + no_consecutives1(k-2)
        dict_numbers[k] = valor
        
        return dict_numbers[k]
        
# print(no_consecutives1(999))



def permutations(atuple):
    
    all_permutations = []
    
    for x in range(0, len(atuple)):
        for y in range(x, len(atuple)):
            for z in range(y, len(atuple)):
                all_permutations.append((atuple[x], atuple[y], atuple[z]))
    return set(all_permutations)

atuple = ('hello', 'world')
print(permutations(atuple))



def permutations(atuple):
    
    alist = []
    
    if len(atuple) == 1:
        return atuple
    
    else:
        primeira = atuple[0]
        resto = atuple[1:]
        alist.append(primeira)
        alist.append(permutations(resto))
    
    return alist

atuple = ('hello', 'world')
print(permutations(atuple))



def digits_average(n):
    
    from math import ceil as c
    
    if n < 10:
        return c(n%10)
    
    elif n < 100:
        return c((digits_average(n%10) + digits_average(n//10))/2)
    
    elif n < 1000:
        return c((digits_average(n%100) + digits_average(n//100))/2)
    
    elif n < 10000:
        return c((digits_average(n%1000) + digits_average(n//1000))/2)
    
n = 158
print(digits_average(158))



def evaluate(a, x):
    from functools import reduce as r
    expoentes = [e for e in range(len(a))]
    fatores = [n*(x**e) for n,e in zip(a,expoentes)]
    return r(lambda x,y: x+y, fatores)
    
    
a = [1, 2, 4, 6, 8]
x = 2
print(evaluate(a,x))


def map_filter_reduce(lst, f1, f2, f3):
    
    from functools import reduce as r
    
    final = list(filter(f1, lst))
    semi = list(map(f2, final))
    return int(r(f3, semi))

def map_filter_reduce(lst, f1, f2, f3):
    from functools import reduce as r
    return int(r(f3, list(map(f2, list(filter(f1, lst))))))


def rearrange(l):
    negative_numbers = list(filter(lambda x: x <= 0 , l))
    positive_numbers = list(filter(lambda y: y > 0, l))
    return negative_numbers + positive_numbers

l = [50, -30, 0, -10, 10]
print(rearrange(l))


def generator(intlist):
    numbers = []
    for item in intlist:
        (início, fim) = item
        numbers = numbers + [x for x in range(início, fim+1)]
    for n in numbers:
        yield n
    
intlist = [(0, 0), (2, 2)]
print(generator(intlist))

def generator(intlist):
    numbers = []
    for item in intlist:
        (início, fim) = item
        numbers = numbers + [x for x in range(início, fim+1)]
    yield n for n in numbers:


def to_celsius(t):
    return list(map(lambda c: round(((c-32)/1.8), 1), t))


def to_fahrenheit(t):
    return list(map(lambda f: round(((f*1.8)+32), 2), t))


def paint(n, boards):
   
    boards = sorted(boards)
    
    if n == 1:
        return max(boards)
    
    else:
        tentativas = [(max(boards[:i]) + paint(n - 1, boards[i:])) for i in range(1, len(boards) - n + 2)]
        return tentativas
        
    
n = 3
boards = [60, 70, 10, 20, 40, 50, 10, 40]
print(paint(n, boards))


def permutations(atuple):

    if len(atuple) == 1:
        return set((atuple,))
    
    if len(atuple) == 2:
        new_tuple = ((atuple[0], atuple[1]), (atuple[1], atuple[0]))
        return set(new_tuple)
    
    else:
        permutações = []
        for o in range(len(atuple)):
            original = atuple[o]
            outras_partes = atuple[:o] + atuple[o+1:]
            for s in permutations(outras_partes):
                
                permutações.append(((original), s))
                
    permutações = set(permutações)
    return permutações
    
# atuple = ('A', 'B', 'C')
# print(permutations(atuple))
    
    
def permutations(atuple):

    if len(atuple) == 1:
        return set((atuple,))
    
    if len(atuple) == 2:
        new_tuple = ((atuple[0], atuple[1]), (atuple[1], atuple[0]))
        return set(new_tuple)
    
    else:
        permutações = []
        for o in range(len(atuple)):
            outras_partes = atuple[:o] + atuple[o+1:]
            for s in range(len(permutations(outras_partes))):
                
                permutações.append((atuple[o] + outras_partes[s]))
                
    permutações = set(permutações)
    return permutações
    
atuple = ('A', 'B', 'C')
print(permutations(atuple))

def digits_average(n):
    from math import ceil as c
    
    if n < 10:
        return n%10
    
    if n < 100:
        return c((digits_average(n%10) + digits_average(n//10))/2)
    
    if n < 1000:
        return c((digits_average(n%100) + digits_average(n//100))/2)
    
    if n < 10000:
        return c((digits_average(n%1000) + digits_average(n//1000))/2)
    
    
n = 158
print(digits_average(n))   
    

def avg(n,m):
    if n<10:
        return m
    else:
        m =m*10 + average(n%10, (n//10)%10)
        return avg(n//10,m)
    
def average(a, b):
    from math import ceil as c
    return c((a + b) / 2)

def digits_average(n):
    if n >= 10:
        avg = 0
        power = 0
        if n >= 10:
            avg = avg + average(n % 10, (n//10) % 10) * 10**power
            n //= 10
            power += 1
        n = avg
    return n

n = 158
print(digits_average(n))  


def permutations(alist, step=0):
    
    if len(alist) == 0:
        pass

    if len(alist) == 1:
        return alist[0]
    
    if len(alist) == 2:
        new_list = alist + alist[0] + alist[1]
        return new_list
    
    else: # 3 or more
        permutações = set()
        for idx in range(len(atuple)):
            for other_thing in permutations(atuple[:idx] + atuple[idx+1:]):
                permutações.add(((atuple[idx],) + other_thing))
                
    return permutações
    
# atuple = ('A', 'B', 'C')
# print(permutations(atuple))                 

from math import ceil, floor, pi, e
a = ceil(e)
b = floor(pi)
c = a - b
print(c)

n = 0
while n < 3:
    print("Ho!")
    n = n + 1
print("Merry Cristmas!")

x = "Fábio"
print("Feliz Natal, {0}!".format(x))

from universe import world, love
from me import my.age as a

def candidates(world, a):
    
    women = list[x for x in world if x is (women and (women.age in range(a, a + 3))]
    candidates = filter(lambda y: y is beautifull, women))
    return list(candidates)

def appends(how_many):
    
    candidates()
    me = [] # I am a empty person :(
    n = 0
    while n < how_many:
        for girl in candidates:
            me.append(girl)
            n = n + 1
    
    me_now = me.append(love)
    
    return me_now

how_many = int(input("How many girlfriends you want? "))
print(appends(how_many))

from string import ascii_uppercase as up
message = (list((str(input("Write something: ")).upper()).strip()))
lista = []
for item in message:
    lista.append(up.find(item))
    
print(lista)

from string import ascii_uppercase as u
from time import strftime as y
l = [[5,4,11,8,25],[0,13,14]]
m = " "
c = [m + str(u[b]) for (b in a )]
for a in l:
    for b in a:
        m += str(u[b])
    m += " "
# print(f"{} {}!".format(m.strip(), str(y.(%Y)+1))
print(f"{}!".format(m.strip(), str(y.(%Y)+1))
    
from string import ascii_uppercase as a
from time import strftime as b
c = [[5,4,11,8,25],[0,13,14]]
d = ""
for e in c:
    for f in e:
        d += str(a[f])
    d += " "
print("{} {}!".format(d.strip(), str(int(b("%Y"))+1)))

def fib(n):
    fibo = [0]
    
    if n ==1:
        return fibo[-1]
    
    if n > 1:
        fibo = [0, 1]
    
    while len(fibo) != n:
        
        fibo.append((fibo[-1]+fibo[-2]))
        
    return fibo[-1]

def decode(message):
    
    result = ""
        
    abc = "1234567890qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM"
    
    # HELLO WORLD!
    
    for idx in range(0, len(message)):
        
        if message[idx] in abc:
        
            for i in range(0, len(abc)):
            
                if message[idx] == abc[i]:
                    
                    
                    a = i+fib(idx + 1)
                    while a >= 54+ 10:
                        a = a - 54 -10
                    
                    result += abc[a]
        
        
        else:
            result += message[idx]

    return result

print(decode("Bipp 8k2ÇFxC6 p3 5DIp, n51Eub"))

def number_to_string(num):
    return str(num)

def are_you_playing_banjo(name):
    from string import ascii_uppercase as a
    
    if name[0] not in a:
        return f"{name} does not play banjo"
    else:
        return f"{name} plays banjo"
    return name

def bool_to_word(boolean):
      return "No" if str(boolean) == "False" else "Yes"

def greet(name):
    return f"Hello, {name}!" if name != "Johnny" else "Hello, my love!"

sheep = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(sheep):
    n = 0
    for item in sheep:
        if str(item) == "True":
            n = n + 1
    return n

print(count_sheeps(sheep))

def digitize(n):
    lista = []
    for digit in str(n):
        lista.append(int(digit))
    
    return (reverse(lista))
    
def reverse(lista):

    lista_b = []
    
    for i in range(1, len(lista)+1):
        lista_b.append(lista[-i])
        
    return lista_b

def find_needle(haystack):
    n = 0
    for item in haystack:
        if item == "needle":
            return f"found the needle at position {n}"
            break
        else:
            n = n + 1
            
def always(n=0):
    return lambda: n

def sum_array(a):
    total = 0
    for item in a:
        total = total + item
        
    return total
        
def get_size(w,h,d):
    lista = []
    lista.append(2*(w*h + w*d + h*d))
    lista.append(w*h*d)
    return lista

def rps(p1, p2):
    atuple = (p1, p2)
    1_won = [('scissors', 'paper'), ('paper', 'rock'), ('rock', 'scissors')]
    2_won = [('paper', 'scissors'), ("rock", "paper"), ("scissors", "rock")]
    
    if atuple in 1_won:
        return "'Player 1 won!'"
    elif atuple in 2_won:
        return "Player 2 won!"
    else:
        return "Draw!"

def two_decimal_places(n):
    return round(n, 2)

def stringy(size):

    answer = ""
    base = "10"

    def is(size):
        return "odd" if size%2 == 1 else "even"

    if is(size) == "odd":
        size = size - 1
        for i in range(0, size + 1):
            answer = answer + base
        return int(answer + "1")

     else:
        for i in range(0, size + 1):
            answer = answer + base
        return int(answer)

    for word in words:
        tf_idf[word] = tf_idf.get(word, "something_beautifull")

def most_frequent_item_count(collection):
    dicta = {}
    for numbers in collection:
        dicta[numbers] = dicta.get(numbers, 0)
    
    for number in collection:
        if number in dicta:
            dicta[number] = dicta[number] + 1
    
    return dicta

def _if(bool, func1, func2):
    
    def truthy(): 
        print("True")


    def falsey(): 
        print("False")

    if str(bool) = "True":
        return truthy()
    else:
        return falsey()

def format_money(amount):
    a = round(amount, 3)
    return f"${a}"

   
def convert_to_celsius(temperature):
    celsius = (int(temperature) - 32) * (5/9)
    return celsius

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status}

def find_longest(string):

    spl = string.split(" ")
    longest = 0

    for item in spl:
        if len(item) > longest:
            longest = len(item)
        else:
            continue
    return longest

def correct_tail(body, tail):
    return True if tail == body[-1] else False

def combine_names(name1, name2):
    return "{} {}".format(name1, name2)

def check_alive(health):
    return True if health > 0 else False

def get_grade(s1, s2, s3):
    score = round(((s1 + s2 + s3)/3), 1)

    if 90 <= score <= 100:
        return "A"
    if 80 <= score < 90:
        return "B"
    if 70 <= score < 80:
        return "C"
    if 60 <= score < 70:
        return "D"
    if 0 <= score < 60:
        return "E"
    
def comfortable_word(word):

    Left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
    Right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    l, r = 0, 0

    for letter in word:
        if letter in Left:
            l = l + 1
        if letter in Right:
            r = r + 1

    a = True
    b = False

    return a if (r and l) != 0 else b

def sum_array(*arr):
    a = int(max(arr))
    b = int(min(arr))
    return a + b

def frame(text, char):

    # Which is the longest word?
    longest = 0
    for item in text:
        if len(item) > longest:
            longest = len(item)
    n = int(longest)

    # Begin and final
    base = char*(n+4)

    # Concatenate all lines
    final = ""
    final = final + base + "\n" 
    for item in text:
        if len(item) == n:
            final = final + char + " " + item + " " + char + "\n"
        else:
            cont = n - len(item)
            space = " "
            final = final + char + space + item + (cont-1)*space + char + "\n"

    final = final + base

    return final

def disemvowel(string):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in string:
        i = string.find(letter)
        if letter in vogais:
            string = string[:i] + string[i+1:]
    return string

def solution(st, limit): 
    if len(st) <= limit:
        return st
    else:
        return "{}{}".format(st[0:limit], "...")

def solve(x,y):
    
    from math import sqrt as s
    def primes_until():
        primes = []
        for i in range(2, 150000):
            n = 0
            for j in range(1, round((s(i)))):
                if i%j != 0:
                    continue
                else:
                    n = n + 1
            if n == 0:
                primes.append(i)

        return primes
    return (primes_until())

def build_row_text(index, character):

    a=list('|||||||||')
    a[index]="|"+character+"|"
    return " ".join(a)

def time_convert(num):
    
    # First filter
    if num < 0:
        return "00:00"
        
    # If number is natural
    else:
        hours = num//60
        if hours <= 9:
            hours = "0" + str(hours)
        minutes = num%60
        if minutes <= 9:
            minutes = "0" + str(minutes)
        clock = "{}:{}".format(str(hours), str(minutes))

    return clock

def next_letter(s):

    from string import ascii_letters as abc
    answer = ""

    for letter in s:
        i = abc.find(letter)
        resto = abc[i+1] if letter in abc else letter
        answer = answer + resto
    return answer

def multiple(x):
    if x%3 == 0 and x%5 == 0:
        return "BangBoom"
    if x%3 != 0 and x%5 == 0:
        return "Boom"
    if x%3 == 0 and x%5 != 0:
        return "Bang"
    if x%3 != 0 and x%5 != 0:
        return "Miss"

# Recursion in Codewars: https://www.codewars.com/kata/latest/my-languages?tags=Recursion

def life_path_number(birthdate):
    
    sp = birthdate.split("-")

    def sum_digits(number):

        if len(str(number)) == 1:
            return number

        else:
            return number//10 + sum_digits(number%10)

    lista = []
    for item in sp:
        item = int(item)
        lista.append(int(sum_digits(item)))
    
    new_string = ""
    for n in lista:
        new_string = new_string + str(n)
    new_number = int(new_string)

    while len(str(new_number)) != 1:
        new_number = sum_digits(new_number)

    return new_number

def reverseded_my(n):

    if int(n)//10 == 0:
        return n
    
    else:
        return reverse(n[:-1]) + str(n[-1])

def reverse(n, i = 0):
    return i if n == 0 else reverse(n//10, i*10 + n%10)

def solution(number):
  
    divisors = []
    for i in range(2, number):
        if i%5 == 0:
            divisors.append(i)
        elif i%3 == 0:
            divisors.append(i)
    
    return sum(divisors) 

def find_it(seq):

    d = {}
    
    for item in seq:
        if item not in d:
            d[item] = d.get(item, 0)
    
    for item in d:
        d[item] = d[item] + 1
    
    return d

def reverse_2(n, i = 0):
    return i if n == 0 else reverse_2(n//10, i*10 + n%10)

def solution_2(number):
  
    divisors = []
    for i in range(2, number):
        if i%5 == 0:
            divisors.append(i)
        elif i%3 == 0:
            divisors.append(i)
    
    return sum(divisors) 

def find_it(seq):

    d = {}
    
    # Dictionary
    for item in seq:
        if item not in d:
            d[item] = d.get(item, 0)
    
    # Counting characters
    for item in seq:
        d[item] = d[item] + 1
    
    # Find odd occurrence
    solution = 0
    for key in d:
        if (d[key])%2 == 1:
            solution = key
            break
    return solution

def get_suma(a,b):
    soma = 0
    m = max(a, b)
    m2 = min(a, b)
    for i in range(m2, m+1):
        soma = soma + i
    return soma

def is_triangle(a, b, c):
    big = max(a, b, c)
    return ( big < ( a + b + c - big ))

def to_camel_case(text):

    # Replace strings to splaces and build a list with all words
    text = text.replace("-", " ").replace("_" " ").split(" ")
    for item in text[1:]:
        item = item.capitalize()
    
    # Concatenate all words in text list
    final = ""
    for item in text:
        final = final + str(item)

    return final

def sortede(word):
    return "".join(sorted(word))

def count_sheepset(sheep):
    n = 0
    for item in sheep:
        if str(item) == "True":
            n = n + 1
    return n

def Aare_you_playing_banjo(name):
    
    if name[0] == "r" or name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

def great(name):
    return f"Hello, {name}!" if name != "Johnny" else "Hello, my love!" 

def song_decoder(song):

    l = song.split("WUB")

    answer = ""
    for item in l:
        if item != (""):
            answer = answer + item + " "    
        
    return answer.strip()

def duplicate_count(text):

    # Create a dictionary with all single letters
    d = {}
    text = text.lower()
    for letter in text:
        if letter not in d:
            d[letter] = d.get(letter, 0)

    # How many occurence in each letter?        
    for letter in text:
        if letter in d:
            d[letter] = d[letter] + 1

    # Select letter that occurs more than one time
    answer = 0
    for key in d:
        if d[key] > 1:
            answer = answer + 1
        else:
            continue

    return answer

def anagrams(word, words):
    
    answer = []
    s_word = "".join(sorted(word))
    for w in words:
        if s_word == "".join(sorted(w)):
            answer.append(w)
        else:
            continue

    return answer 

def ints_triangle(a, b, c):
    big = max(a, b, c)
    return ( big < (a+b+c-big))

def gets_sum(a,b):
    soma = 0
    m = max(a, b)
    m2 = min(a, b)
    for i in range(m2, m+1):
        soma = soma + i
    return soma

def find_itse(seq):

    d = {}
    
    # Dictionary
    for item in seq:
        if item not in d:
            d[item] = d.get(item, 0)
    
    # Counting characters
    for item in seq:
        d[item] = d[item] + 1
    
    # Find odd occurency
    solution = 0
    for key in d:
        if (d[key])%2 == 1:
            solution = key
            break
    return solution

def happy_2021(something):
        
    from string import ascii_uppercase as a
    from time import strftime as b
    c = [[5,4,11,8,25],[0,13,14]]
    d = ""
    for e in c:
        for f in e:
            d += str(a[f])
        d += " "
    print("{} {}!".format(d.strip(), str(int(b("%Y"))+1)))
    return None

def count_bits(n):

    # Converter decimal number to binary number
    def decimal_to_binary(n):

        binary = 0
        aux = n
        index = 0
        while aux:
            binary = aux % 2 * 10 ** index + binary
            aux = aux//2
            index = index + 1

        return binary

    # How many 1's are in binary number?
    binary = str(decimal_to_binary(n))
    counter = 0
    for number in binary:
        if number == "1":
            counter = counter + 1

    return counter

def rpsp(p1, p2):
    atuple = (p1, p2)
    won1 = [('scissors', 'paper'), ('paper', 'rock'), ("rock", "scissors")]
    won2 = [('paper', 'scissors'), ("rock", "paper"), ("scissors", "rock")]
    
    if atuple in won1:
        return "Player 1 won!"
    elif atuple in won2:
        return "Player 2 won!"
    else:
        return "Draw!"
def moste_frequent_item_count(collection):

    # Build a dictionary
    dicta = {}
    for numbers in collection:
        dicta[numbers] = dicta.get(numbers, 0)
    
    # How many times a number appears in collection?
    for number in collection:
        if number in dicta:
            dicta[number] = dicta[number] + 1
    
    # Find a number that apears more times in collection
    many = 0
    for key in dicta:
        if dicta[key] > many:
            many = dicta[key]
        else:
            continue
    
    return many

def stringly(size):

    answer = ""
    base = "10"

    # Size is odd or even?
    def is_oe(size):
        return "odd" if size%2 == 1 else "even"

    # Type 101
    if is_oe(size) == "odd":
        size = (size - 1)//2
        for _ in range(0, size):
            answer = answer + base
        return answer + "1"

    # Type 1010
    else:
        size = size//2
        for _ in range(0, size):
            answer = answer + base
        return answer
    
def _if(bool, func1, func2):

    if str(bool) == "True":
        return func1()
    elif str(bool) == "False":
        return func2()

def format_money(amount):

    l = str(amount).split(".")

    if len(l) == 2:
        if len(l[1]) == 2:
            return f"${amount}"
        elif len(l[1]) == 1:
            return f"${amount}0"
    else:
        return f"${amount}.00"

def isDigit(string):
    
    test = "0123456789.+-  */,()         "
    
    n = 0 # Counter of issues
    for digit in string:
        if digit not in test:
            n = n + 1
        else:
            continue
    
    # Other clever solution
    try:
        float(string)
        return True
    except ValueError:
        return False

      def sum_of_intervals(intervals):

    all_numbers = []
    for item in range(len(intervals)):
        if intervals[item] != intervals[item-1]:
            for number in range(item):
                all_numbers.append(number)
        else:
            continue
    
    total = len(all_numbers)
    return total

def increment_string(strng):

    values = "0123456789"

    if strng[-1] in values:
        return strng[:-1] + str(int(strng[-1]) + 1)
    else:
        return strng + str(1)

def order_weight(strng):

    # Recursive function that return sum of all digits
    def sum_digits(number):
        if len(str(number)) == 1:
            return number
        else:
            return number%10 + sum_digits(number//10)

    # Key sorted
    def st(list)
        return list[0]

    # Buil sum of all numbers
    all_numbers = strng.split(" ")
    sum_numbers = []
    for item in all_numbers:
        sum_numbers.append(int(sum_digits(int(item))))

    # Sorted lists
    new = []
    for x, index1 in sum_numbers:
        for y, index2 in all_numbers:
            if index1 == index2:
                new.append(tuple(x, y))
    
    new = new.sort(key=st)
    
    # Final list
    final = []
    for thing in new:
        (x, y) = thing
        final.append(y)

    # Transform answer in a string
    answer = ""
    for item in final:
        answer = answer + str(item) + " "

    return answer.strip()

def ajustes(result):
    
    result = result[1::] # retira a primeira vírgula
    new_list = result.split(",") # lista com itens do tipo "n->m" ou "n->n"
    final = ""
    
    for x in range (0, len(new_list)):
        
        y = round((len(new_list[x])-2)/2) # número de dígitos de n
        
        if new_list[x][:y] == new_list[x][-y:]: #significa que n->n
            new_list[x] = new_list[x][0:y] #substitui por n
            
        else:
            continue
        
    for z in range(0, len(new_list)):  
        final = final + "," + new_list[z]
        
    return final[1::] # retira a primeira vírgula

            
def solution(args):

    vazio = []
    
    if args == []:
        return vazio
    
    if len(args) == 1:
        return args
    
    result = ""
    a_list = args
    i = 0 # initial index value
    j = 0 # initial complement value
    
    while (i < len(a_list)+1) or ((i+j+1) < len(a_list)):
    
        while ((int(a_list[i+j]) - int(a_list[i])) == j):
            if (i+j) == (len(a_list)-1):
                result = result + "," + str(a_list[i]) + "-" + str(a_list[i+j])
                
                return ajustes(result) # chama a outra função que irá retirar a 
                                       # primeira vírgula e substituir casos 
                                       # do tipo "n->n" por "n"
            else:
                j = j + 1
        
        else:
            result = result + "," + str(a_list[i]) + "-" + str(a_list[i+(j-1)])
            i = i + j
            j = 0 # cancel complement
    
    return result 

def format_duration(seconds):
    
    years = seconds//(365*24*60*60)
    days = (seconds - years*(365*24*60*60))//(24*60*60)
    hours = (seconds - years*(365*24*60*60) - days*(34*60*60))//(60*60)
    minutes = (seconds - years*(365*24*60*60) - days*(34*60*60) - hours*(60*60))//60
    secondss = seconds - years*(365*24*60*60) - days*(34*60*60) - hours*(60*60) - minutes*60
    
    if years != 0:
        return f"{years} year, {days} day, {hours} hour, {minutes} minutes and {seconds} seconds"
    if days != 0:
        return f"{days} day, {hours} hour, {minutes} minutes and {seconds} seconds"
    if hours != 0:
        return f"{hours} hour, {minutes} minutes and {seconds} seconds"
    if minutes != 0:
        return f"{minutes} minutes and {seconds} seconds"
    if secondss != 0:
        return f"{secondss} seconds"
    
def zeros(n):

    # Recursive factorial
    def factorial(n):

        if n == 1:
            return n
        else:
            return n * factorial(n-1)

    # How many zeros in factorial?
    if n == 0:
        return 0
    else:
        result = factorial(n)
        counter = 0
        for digit in str(result):
            if digit == "0":
                counter = counter + 1 
            else:
                continue

        return counter

def deep_count(a):

    counter = 0
    for i in a:
        if type(i) is list:
            counter = counter + depp_count(i)
        else:
            counter = counter + 1

    return counter
     
   def search_linear(xs, target):
    """ Don't do this!  """
    """ Find and return the index of target in sequence xs """
    for v in xs:
        if v == target:
            return xs.index(v)
    return -1

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    i = 0
    while i < len(xs):
        if xs[i] == target:
            return i
        else:
            i += 1
    return -1
      
def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    i = -1
    for v in xs:
        i += 1
        if v == target:
            return i
    return -1


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1


def remove_adjacent_dups(xs):

    ls = ["Joe", "Zoe", "Joe", "Angelina", "Zuki", "Thandi", "Zuki"]
    result = []
    most_recent_elem = None
    for e in ls:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result

def remove_adjacent_dups_2(xs):

    ls = ["Joe", "Zoe", "Joe", "Angelina", "Zuki", "Thandi", "Zuki"]
    result = []
    for element in ls:
        if element not in result:
            result.append(element)
            
    return sorted(result, key=None)

      def square_odds(values):

    all_numbers = [int(x) for x in values.split(",")]
    all_squares = [str(x**2) for x in all_numbers if x%2==1]
    result = ",".join(all_squares)
    return result

def comprehensions(i, j):

    # To get all numbers, including j
    j = j + 1
    from math import sqrt as r

    first_part = [x for x in range(i, j) if (((str(x))[-1] == "8") or ((str(x))[-1] == "3"))]
    second_part = [round((r(x)),2) for x in range(i, j)]
    third_part = {x: chr(x) for x in range(i, j)}

    return tuple((list(first_part), tuple(second_part), dict(third_part)))

def brute_force(f, l):

    # For the resolution of the exercise I consulted how to make combinations using comprehensions. 
    # I found this site that helped me with the task:
    # https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
    
    from itertools import product as p

    n = len(l)
    all_combinations = list(p(l, repeat = 3))

    # Combinations whose length is equal to 3 using filter
    function = lambda j: len(j) == 3
    allowed_combinations = list(filter(function, all_combinations))

    # Join letters for string to login
    concatenated = ["".join(letters) for letters in allowed_combinations]

    # Which combinations are possible for login?
    possibilities = list([x for x in concatenated if f(x) == True])
    return possibilities

#f = lambda x: abs(int(x)) == 1 if x.isdigit() else False
#l = ['-', '0', '1', '2']
#print(brute_force(f, l))

def multiples_of7(n):

    # All multiples of 7 in nterval [0, n[ (n not include)
    all_possibilities = [x for x in range(0, n) if x%7 == 0]

    # Generator
    for item in all_possibilities:
        yield item

def odd_range(start, stop, step):

    # All odd numbers between start and stop
    numbers = [x for x in range(start, stop) if x%2 == 1]

    # Step increment with index
    total = len(numbers)
    odd_numbers = [numbers[index] for index in range(0, total, step)]

    # Generator
    for item in odd_numbers:
        yield item
      
def to_celsius(t):
    temperatures = [round(((c-32)/1.8), 2) for c in t]
    return list(temperatures)

def to_fahrenheit(t):
    temperatures = [round(((f*1.8)+32), 2) for f in t]
    return list(temperatures)

def get_composites(n):

    all_numbers = [x for x in range(4, n+1)]
    primes_until_n = [y for y in all_numbers if all( y % z != 0 for z in range(2, y))]
    composites_filter = lambda c: c not in primes_until_n

    result = filter(composites_filter, all_numbers)

    # Genetator
    for number in list(result):
        yield number

def evaluate(a, x):

    expoentes = [e for e in range(len(a))]
    fatores = [n*(x**e) for n,e in zip(a,expoentes)]

    return sum(fatores)

def rearrange(l):
    negative_numbers = list((x for x in l if x <= 0))
    positive_numbers = list((x for x in l if x > 0))

    return negative_numbers + positive_numbers

def batch_norm(alist, batch_size):

    while len(alist) != 0:

        lote = alist[:batch_size]    
        alist = alist[batch_size:]
        n = sorted(lote.copy())

        if len(lote)%2 == 1:

            mediana = n[len(lote)//2]

            yield list([number - mediana for number in lote])

        else:
            
            a = n[(len(lote)//2)-1]
            b = n[len(lote)//2]
            mediana = (a+b)/2

            yield list([number - mediana for number in lote])

def average(a, b):
    from math import ceil as c
    return c((a + b) / 2)

def digits_average(n):
    if n >= 10:
        avg = 0
        power = 0
        if n >= 10:
            avg = avg + average(n % 10, (n//10) % 10) * 10**power
            n //= 10
            power += 1
        n = avg list
    return n

def average(a, b):

    from math import ceil as c
    result = c((a+b)/2)
    return result

def next_number(n):

    if n < 100: # Only 2 digits
        return average((n%10), ((n//10)%10))
    else: # More than 2 digits
        return average(n % 10, (n//10) % 10) + next_number(n//10) * 10
        
def digits_average(n):

    if n < 9: # Only one digit
        return n
    else: # Two or more
        return digits_average(next_number(n))

def poss(n, boards):

    # All possibilities to paint all boards
    qtd = len(boards) + 2 - n
    all_possibilities = []
    for x in range(1, qtd):
        possibility = paint(n-1, boards[x:]) + max(boards[:x])
        all_possibilities.append(possibility)
    
    return all_possibilities

def paint(n, boards):

    if n == 1:
        return max(boards)
    else:
        return min(poss(n, boards))

def permuta(alist, step=0):

    all_permutations = []

    if len(alist) == 1:
        # Base case
        return list([alist])
    
    if len(alist) == 2:
        return [alist, [alist[1], alist[0]]]

    if len(alist) == step:
        all_permutations.append(alist)

    if len(alist) > 2:
        a = step
        b = len(alist)
        for item in range(a, b):
            cop = alist.copy()
            cop[item] = alist[a]
            cop[a] = alist[item]
            all_permutations += permuta(cop, 1+a)
        
        return all_permutations

def não_falido(money, products, wishlist):

    gasto = 0
    for item in wishlist:
        quantidade = wishlist.get(item)
        preço = products.get(item)
        gasto = gasto + preço*quantidade

    return True if (gasto < money or money == gasto) else False

def knapsack(money, products, wishlist):

    all_possibilities = []

    if não_falido(money, products, wishlist):
        # Found the best solution
        return wishlist
    
    # Rearranging
    for item in wishlist:
        solution = wishlist.copy()
        if wishlist.get(item) != 0:
            if products.get(item) > money:
                # Can't buy them
                solution[item] = 0
            else:
                # Can't buy them all
                solution[item] = solution[item] - 1
            
            all_possibilities.append(solution)

    for possibility in all_possibilities:
        if não_falido(money, products, possibility):
            continue
        else:
            # Error
            for item in possibility:
                nova = knapsack(money, products, item)
                all_possibilities.append(nova)
    
    all_prices = []
    for possibility in all_possibilities:
        quantidade = wishlist.get(possibility)
        preço = products.get(possibility)
        gasto = gasto + preço*quantidade
        all_prices.append(gasto)

    final = {}
    for item, qtd in enumerate(all_possibilities.index(max(all_prices)).itens()):
        if qtd != 0:
            final = final + {item:qtd}

    return final

      def treasure(clues):

    pos = (0, 0)
    while pos in clues:
        old_pos = pos
        pos = clues[pos]
        del clues[old_pos]

    return pos

    # clues = ({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)})
    # print(treasure(clues))

def evaluate(a, x):

    coeficientes = list([x**i for i in range(len(a))])
    polinómio = [n*x for x, n in zip(coeficientes, a)]

    return sum(list(polinómio))

    # a = [1, 2, 4]
    # x = 5
    # print(evaluate(a, x))

def recursive_dot(l1, l2):

    total = 0

    for item1, idx1 in enumerate(l1):
        for item2, idx2 in enumerate(l2):
            if (type(item1) == int) and (type(item2) == int) and (idx1 == idx2):
                total = total + item1*item2
            else:
                if idx1 == idx2:
                    total = total + recursive_dot(item1, item2)

    return total

def recursive_dot2(l1, l2):

    if type(l1) == int:
        return l1*l2

    if len(l1) == 0:
        return 0

    return recursive_dot2(l1[0], l2[0]) + recursive_dot2(l1[1:], l2[1:])

    # l1 = [1, [2, 3]]
    # l2 = [4, [5, 6]]
    # print(recursive_dot2(l1, l2))

def reclist(alist):

    new_list = []

    for item in alist:
        if type(item) != list:
            new_list.append(item)
        else:
            new_list = new_list + reclist(item)

    return new_list

def interleave(alist1, alist2):

    final = []
    alist1 = reclist(alist1)
    alist2 = reclist(alist2)

    for item1 in alist1:
        for item2 in alist2:
            idx1 = alist1.index(item1)
            idx2 = alist2.index(item2)
            if idx1 == idx2:
                final.append(item1)
                final.append(item2)
            else:
                continue

    return final

    # alist1 = [1, [4,2]]
    # alist2 = [3, [7,4]]
    # print(interleave(alist1, alist2))  

def min_path2(matrix, a, b, visited=[]):

    IMPOSSIBLE = 99999 # Max value

    if a == b: # final position
        return 0

    if a[0] < 0 or a[0] >= len(matrix): # outside matrix lines
        return IMPOSSIBLE

    if a[1] < 0 or a[1] >= len(matrix[0]): # outside matrix columns
        return IMPOSSIBLE

    if matrix[a[0]][a[1]]: # an obstacle
        return IMPOSSIBLE

    if a in visited: # already visited
        return IMPOSSIBLE

    # find a min path
    mindist = IMPOSSIBLE
    possible = [(0,1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1), (0,-1), (1,-1)]

    for p in possible:
        l, c = a[0]+p[0], a[1]+p[1]
        # try the direction
        d = 1 + min_path2(matrix, (l, c), b, visited+[a])
        # see if it's the best so far
        if d < mindist:
            mindist = d
    return mindist

    # mx = [
        # [False]*4,
        # [False, True, False, False],
        # [False, True, False, False],
        # [False]*4
        ]
    # min_path(mx, (2, 0), (0, 3))

      def sinhe(item):
    return item[1]

def reorder(l):

    l = sorted(l, key=sinhe)

    solution = ""
    for item in l:
        solution = solution + item[0]
    
    return solution

    # l = [('g', 3), ('d', 1), ('o', 2)]
    # print(reorder(l))

def process(commands):

    s = commands[0]

    for op, t in zip(commands[1::2], commands[2::2]):

        if op == '|': 
            s = s | t

        if op == '&': 
            s = s & t

        if op == '-': 
            s = s - t

        if op == 'x': 
            # Cartesian product
            r = set()
            for i in s:
                for j in t:
                    r.add((i, j))
                s = r
    return s

def count_digits(n):

    if len(str(n)) == 1:
        return {}
    d = count_digits(n//10)
    d[n%10] = d.get(n%10, 0) + 1

    return d
        
    # n = 27287
    # print(count_digits(n))

def fsm(transitions, input):

    current_state = 0
    for c in input:

        if c not in transitions[current_state]:
            return -1

        current_state = transitions[current_state][c]

    return current_state

    # transitions = [
    #                 {'a': 1}, # state 0
    #                 {'b': 2}, # state 1
    #                 {'a': 1, 'b': 2} # state 2
    #             ]               

    # input = "a"
    # print(fsm(transitions, input))

def simplify(expr):

    if type(expr) != tuple:
        return expr

    if expr[0] == '¬':

        e = expr[1]

        if type(e) == tuple:

            if e[0] == '¬':
                return simplify(e[1])

            if e[0] == '∧':
                e1 = simplify(('¬', e[1]))
                e2 = simplify(('¬', e[2]))
                return ('∨', e1, e2)

            if e[0] == '∨':
                e1 = simplify(('¬', e[1]))
                e2 = simplify(('¬', e[2]))
                return ('∧', e1, e2)

        return expr

    return (expr[0], simplify(expr[1]), simplify(expr[2]))

    # expr = ('¬', ('∧', 'a', ('¬', 'b')))
    # print(simplify(expr))
      
def reclist(alist):

    new_list = []

    for item in alist:
        if type(item) != list:
            new_list.append(item)
        else:
            new_list = new_list + reclist(item)

    return new_list

def recursive_dot(l1, l2):

    l1 = reclist(l1)
    l2 = reclist(l2)

    total = 0
    for n1 in l1:
        for n2 in l2:
            one = l1.index(n1)
            two = l2.index(n2)
            if one == two:

                total = total + n1*n2

    return total

    # a = [1, [2, 3]]
    # b = [4, [5, 6]]
    # print(recursive_dot(a, b))
    # c = [[5, 3, 1], [2, 4]]
    # d = [[4, 2, 0], [1, 3]]
    # print(recursive_dot(c, d)) 

def rec(n, m):

    if n > m:
        atuple = (m, n)
    else:
        atuple = (n, m)

    return atuple

def cube_sum(n, m):
    
    alist = list([x for x in range(n+1, m+1)])
    blist = list([x for x in range(m+1, n+1)])

    cube_a = list([x**3 for x in alist]) 
    cube_b = list([x**3 for x in blist])

    return sum(cube_a) if alist != [] else sum(cube_b)

    # print(cube_sum(4, 0))
    # print(cube_sum(5, 10))


def position(alphabet):
    
    from string import ascii_lowercase as abc

    n = abc.find(alphabet) + 1
    return f"Position of alphabet: {n}"


def four_seasons(d):

    season = ""
    if d in range(90, 180):
        season = "Summer"
    elif d in range(180, 270):
        season = "Winter"
    elif d in range(270, 360):
        season = "Spring"
    else:
        season = "Autumn"

    return f"{season} Season"

def descompactar(alist):

    total = []
    for item in alist:

        if type(item) != list:
            total.append(item)
        
        else:
            total = total + descompactar(item)

    return total

def sum_nested(lst):
    a = descompactar(lst)
    b = sum(a)

    return b

    # alist = [1, [2, 3, []]]
    # print(sum_nested(alist))
      
def reverse(n, i = 0):
    return i if n == 0 else reverse(n//10, i*10 + n%10)

def plus(number):
    alist = [int(n) for n in str(number)]
    return list(alist)

def aux(matrix, word, row, col):
    if word == '':
        return True
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    if matrix[row][col] == word[0]:
        if aux(matrix, word[1:], row, col+1):
            return True
        elif aux(matrix, word[1:], row, col-1):
            return True
        elif aux(matrix, word[1:], row+1, col):
            return True
        elif aux(matrix, word[1:], row-1, col):
            return True
        elif aux(matrix, word[1:], row+1, col+1):
            return True
        elif aux(matrix, word[1:], row-1, col+1):
            return True
        elif aux(matrix, word[1:], row+1, col-1):
            return True
        elif aux(matrix, word[1:], row-1, col-1):
            return True
    return False

def soup(matrix, word):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if aux(matrix, word, row, col):
                return chr(row + 65) + str(col + 1)

def per(atuple):

    alist = list([tuple((x, y, z)) for x in atuple for y in atuple for z in atuple if x != z and z != y and y != z])
    return alist

def s(something):
    a = set()
    a.add(7)
    a.add(8)
    a.add(9)
    a.add(8)
    a.remove(9)
    return a

def swap_case(astr):
    return astr.swapcase()

def unique_values(alist):
    
    aset = set()
    
    for dictionary in alist:
        for key in dictionary:
            if dictionary[key] not in aset:
                aset.add(dictionary[key])
                
    return aset

def rec(alist):
    
    blist = []
    for item in alist:
        if type(item) != list:
            blist.append(item)
            
        else:
            blist = blist + rec(item)
            
    return blist

def rec_count(alist):
    
    blist = rec(alist)
    
    adict = {}
    for item in blist:
        adict[item] = adict.get(item, 0) + 1
        
    return adict

def maximo_divisor(n1, n2):
    
    import math
    return math.gcd(n1, n2)

def calculator(expr):
    
    if len(expr) == 2:
        return expr
    
    else:
        
        operator = expr[1]
        
        if operator == "*":
            a = calculator(expr[0])
            b = calculator(expr[2])
            c = maximo_divisor(a[0]*b[0], a[1]*b[1])
            d = (((a[0]*b[0])//c), ((a[1]*b[1])//c))
            return d
        
        if operator == "/":
            a = calculator(expr[0])
            b = calculator(expr[2])
            c = maximo_divisor(a[0]*b[1], a[1]*b[0])
            d = (((a[0]*b[1])//c), ((a[1]*b[0])//c))
            return d


