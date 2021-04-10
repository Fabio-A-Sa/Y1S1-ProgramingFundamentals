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

def brute_force(f, l):

    # All combinations whose lenght is 3
    all_combinations = list([(x, y, z) for x in l for y in l for z in l])
    concatenated = list(["".join(possibility) for possibility in all_combinations])

    # Filter with the function f
    result = list([possibility for possibility in concatenated if f(possibility) == True])

    return result

    # l = ['-', '0', '1', '2']
    # f = lambda x: abs(int(x)) == 1 if x.isdigit() else False
    # print(brute_force(f, l))

def odd_range(start, stop, step):

    # First odd number in range (start, stop)
    number = 0
    for i in range(start, stop):
        if i%2 == 1: # Odd number
            number = i
            break
    
    # Steps until stop
    step = 2 * step
    result = []
    for n in range(number, stop, step):
        result.append(n)
    
    # Generator
    for item in result:
        yield item

    # start = 0
    # stop = 20
    # step = 2
    # print(odd_range(start, stop, step))

def multiples_of7(n):

    if n < 0:
        return None

    if n == 0:
        return n

    else:
        # All multiples of 7 in nterval [0, n[ (n not include)
        all_possibilities = [x for x in range(0, n) if x%7 == 0]

        # Generator
        for item in all_possibilities:
            yield item

    # n = 0
    # print(multiples_of7(n))

def square_odds(values):

    if values == ("" or ","):
        return ""

    if type(values) != str:
        return ""

    if values == "0":
        return ""

    else:

        all_numbers = [int(x) for x in values.split(",")]
        all_squares = [str(x**2) for x in all_numbers if x%2==1]
        result = ",".join(all_squares)
        return result

    # print(square_odds("0"))

def which_room(name):
    
    # A dict with all allowed exam's classrooms
    classrooms = {  
                    'B104': ("Adam Gershenson Nogueira", "Fábio Cunha Morais"),
                    'B201': ("Felipe Siqueira Espinheira", "Gustavo Miguel Soeiro Machado"),
                    'B207': ("Henrique Oliveira Silva", "José Marcelino Zacarias Júnior"),
                    'B208': ("José Maria Borges Pires do Couto e Castro", "Nuno André Gomes França"),
                    'B213': ("Nuno Francisco Moreira dos Santos", "Walter Muhanyele Massango") 
                 }

    # Name normalization
    name = name.strip()
    name_list = name.split(" ")

    # Find a correct classroom
    correct_classroom = ""
    counter = 0
    for key in classrooms.keys():

        # Initial conditions
        start = ((classrooms[key])[0]).split(" ")
        end = ((classrooms[key])[1]).split(" ")
        name_search = name_list[counter]

        # Search
        if name_search >= start[counter] and name_search <= end[counter]:
            correct_classroom = key

    # Get answers    
    answer_1 = "A tua sala é a {}".format(correct_classroom)
    block = correct_classroom[0]
    floor = correct_classroom[1]
    door = int(correct_classroom[2:])
    answer_2 = "Exame no bloco {}, piso {} e na porta {}".format(block, floor, door)
    
    return "{}{}{}{}{}".format(answer_1, "\n", "Informações adicionais:", "\n", answer_2)

    # name = str(input("Qual o teu nome? \n"))
    # print(which_room(name))

      def lecture_random(something):

    # random.Random().randrange(a, b) for generate one random number between a and b
    from random import Random as r
    all_possibilities = r().randrange(1, 100)
    odd_possibilities = r().randrange(1, 100, 2)
    even_possibilities = r().randrange(1, 100, 3)

    # Shuffle range
    normal = list(range(1, 50))
    r().shuffle(normal)
    return normal

def lecture_timed(something):

    def somador(alist):

        total = 0
        for item in alist:
            total = total + int(item)

        return total

    import time
    # the subfunction time.time() takes time before and after running a function
    all_numbers = range(1, 1000000)
    t_initial = time.time()
    soma = somador(all_numbers)
    t_final = time.time()
    time_interval = round((t_final - t_initial), 10)

    return "This functions times {} seconds to sum all numbers until 1000000.{}The result is {}, a big number!".format(time_interval, "\n", soma)

def lecture_math(something):

    # Import functions of math built-in module
    from math import sin, cos, tan, pi, e, sqrt
    # Now I can make counts without "math" before assignment!
    a = sin(0.585)
    return a

      def qual_o_preço_desta_montra_final_haaaaaa(money, products, wishlist):

    total = 0 
    for coisa in wishlist:
        quantidade = wishlist[coisa]
        preço = products[coisa]
        total = total + quantidade * preço
        
    return tuple((total, False)) if total > money else tuple((total, True))

def normalization(alist):

    standardized = []

    for adict in alist:
        dictio = adict.copy()
        for key in dictio:
            if adict[key] == 0:
                del dictio[key]
        standardized.append(dictio)

    return standardized

def knapsack(money, products, wishlist):

    all_possibilities = []
    best_combination = 0
    best_solution = {}

    if (qual_o_preço_desta_montra_final_haaaaaa(money, products, wishlist))[1]:
        return wishlist # Found one possible solution
    
    # Rearranging
    else:
        for item in wishlist:

            solution = wishlist.copy()

            if wishlist.get(item) != 0:

                if solution[item] == 1:
                    # solution[item] - 1 == 0
                    del solution[item]

                elif products.get(item) > money:
                    # Can't buy them
                    del solution[item]

                else:
                    # Can't buy them all
                    solution[item] = solution[item] - 1
                
                possibility = qual_o_preço_desta_montra_final_haaaaaa(money, products, solution)

                if possibility[1] == True:
                    if possibility[0] > best_combination:

                        best_combination = possibility[0]
                        best_solution = solution
                        all_possibilities.append(best_solution)
                
                else:

                    other_possibility = knapsack(money, products, solution)

                    if type(other_possibility) is dict:

                        other_sum = qual_o_preço_desta_montra_final_haaaaaa(money, products, other_possibility)

                        if other_sum[1] == True:
                            if other_sum[0] > best_combination:
                                
                                best_combination = other_sum[0]
                                best_solution = other_possibility
                                all_possibilities.append(best_solution)

    return (normalization(all_possibilities))[-1]

def bubble_sort(alist):

    s = len(alist)
    aux = 0

    if s == (0 or 1):
        return alist

    else:
        for x in range(s):

            counter = 0
            flag = True

            while counter + 1 < s :
                if alist[counter] > alist[counter+1]:
                    aux = alist[counter+1]
                    alist[counter+1] = alist[counter]
                    alist[counter] = aux
                    flag = flag and False
                counter = counter + 1

            if flag == True:
                # Not changed any more values
                return alist

    # alist = [5, 1, 2, 8, 2.5]
    # print(bubble_sort(alist))
    
def key_reverse (aset):
    return aset[0]

def mdis_relação_binária(A, B):

    alist = list([tuple((x, y)) for x in A for y in B])
    alist.sort(key=key_reverse)
    return set(alist)

    # A = {"a", "b", "c", "d"}
    # B = {1, 2, 3, 4}
    # print(mdis_relação_binária(A, B))

def multiples_of7(n):

    for x in range(n):
        if x%7 == 0:
            # Generator
            yield x

      def aux(f):
    return f if type(f) is list else f()

def bitonic_point(f):

    alist = aux(f)

    if len(alist)%2 == 1:
        middle = (len(alist)+1)//2
    else:
        middle = len(alist)//2

    left = alist[:middle]
    right = alist[middle:]

    if alist[middle - 1] < alist[middle] and alist[middle] > alist[middle + 1]:
        # Atingiu o pico
        return alist[middle]

    if alist[middle-1] < alist[middle]:
        # O número procurado está depois
        return bitonic_point(right)
    
    if alist[middle] > alist[middle + 1]:
        # O número procurado está antes
        return bitonic_point(left) 

    # f = list(range(0, 10)) + list(range(20, 2, -1))
    # print(bitonic_point(f))

def aux(f):
    return f if type(f) is list else f()

def count_zeros(f):

    alist = aux(f)
    total = 0

    if len(alist) == 1:
        # Caso base
        return total

    else:
            
        if len(alist)%2 == 1:
            middle = int((len(alist)+1)//2)
        else:
            middle = int(len(alist)//2)

        left = alist[:middle]
        right = alist[middle:]

        if alist[middle] != 0:
            # Os zeros estão mais à frente
            total = total + count_zeros(right)

        if alist[middle] == 0:
            # Inclui tudo para a frente mais um pedaço de trás
            total = total + len(right) + count_zeros(left)

    return total

    # f = lambda: [1, 1, 1, 0, 0]
    # print(count_zeros(f))
      
 def ordem(something):
    # Coordenada x 
    return something[0]

def ordenação(alist):
    return sorted(alist, key=ordem)

def distâncias(ponto1, ponto2):

    from math import sqrt as raiz
    x1 = ponto1[0]
    x2 = ponto2[0]
    y1 = ponto1[1]
    y2 = ponto2[1]

    distance = round(raiz((x1 - x2)**2 + (y1 - y2)**2))
    return distance

def separação(alist):

    n = len(alist)
    if n%2 == 1:
        middle = (n-1)//2
    else:
        middle = n//2

    left = alist[:middle]
    right = alist[middle:]

    return (left, right)

def rec_distance(alist, best_distance = 10000000000000):

    

    return best_distance

def closest_pair(points):

    points = ordenação(points)
    
    left = separação(points)[0]
    right = separação(points)[1]

    min_distance_left = rec_distance(left)
    min_distance_right = rec_distance(right)

    return left, right

points = [(2498, 7397), (2168, 8117), (2168, 6677), (1496, 1976), (8893, 9240), (288, 9467), (7465, 8080), (4588, 1774), (4178, 8118), (3459, 7224)]
print(closest_pair(points))
      
def days_until_empty(C, l):
    
    dias_passados = 0
    agua_no_tanque = C

    while agua_no_tanque > 0:

        dias_passados = dias_passados + 1
        agua_no_tanque = C - dias_passados if agua_no_tanque + l >= C else agua_no_tanque + l - dias_passados
        
    return dias_passados

def find_me(f, limits):


    all_numbers = list([x for x in range(limits[0], limits[1])]) if type(limits) is tuple else limits
    n = len(all_numbers)//2

    left = all_numbers[:n]
    right = all_numbers[n:]

    if f(all_numbers[n]) == 0:
        # Found it!
        return 1
    
    if f(right[0]) == -1:
        return 1 + find_me(f, left)

    # Else
    return 1 + find_me(f, right)

def binary_tree(key, tree):

    if key == tree[0]:
        return tree[1]

    else:

        if key < tree[0]:
            next_function = tree[2]()
            return binary_tree(key, next_function)

        else:
            # If key > tree[0] or tree[0] == key
            next_function = tree[3]()
            return binary_tree(key, next_function)

def midpoint(p1, p2):
    mid = (p1 + p2) / 2
    return mid 

def bisect(f, n, lower=0, upper=1, total=0, aprox=0):

    if n == total:
        result = round(aprox, 5)
        return result

    else:

        aprox = midpoint(lower, upper)

        if f(lower)*f(aprox) < 0:
            return bisect(f, n, lower, aprox, total+1, aprox)
        else:
            return bisect(f, n, aprox, upper, total+1, aprox)

def longest_prefix(words):

    if len(words) == 1:
        return words[0]
    
    else:

        words.sort()
        cobaia = words[0]

        for i in range(len(words)):
            if cobaia not in words[i]:
                cobaia = cobaia[:len(cobaia)-1]
            else:
                continue


        return cobaia

    # words = ['apple', 'apply', 'ape', 'april']
    # print(longest_prefix(words))

      def notebook_23(something):

    from time import perf_counter as t
    alist = list([x for x in range(191)])
    with open("first.txt", "w") as myfile:
        for i in range(181):
            t0 = t()
            myfile.write("Qualquer coisa número: {}{}".format(alist[i], "\n"))
            t1 = t()
            myfile.write("Tempo gasto: {}{}".format(t1-t0, "\n"))
    
    with open("first.txt") as f:
        content = f.read()

    words = content.split()
    answer = "File ok. {}There are {} words in the file.".format("\n", len(words))

    return answer
      
    
 from time import perf_counter as t

def longest_prefix(words):

    t0 = t()
    if len(words) == 1:
        return words[0]
    
    else:

        total = 0
        words.sort()
        cobaia = words[0]

        for i in range(len(words)):
            if cobaia not in words[i]:
                cobaia = cobaia[:len(cobaia)-1]
                total = total + 1
            else:
                continue
        
        t1 = t()
        palavras = len(words)
        tempo = t1 - t0
        answer = "Prefixo comum: {}{}Número de ciclos: {}{}Total de palavras procuradas: {}{}Tempo de pesquisa: {} segundos".format(cobaia, "\n", total, "\n", palavras, "\n", round(tempo, 4))
        return answer

    # print("+++++++++++++++++++++++++++++")
    # print(longest_prefix(words))
    # print("+++++++++++++++++++++++++++++")
      
def longest_prefix(words):

    from time import perf_counter as t
    
    words = words*10000
    t0 = t()
    if len(words) == 1:
        return words[0]
    
    else:

        total = 0
        words.sort()
        cobaia = words[0]

        for i in range(len(words)):
            if cobaia not in words[i]:
                cobaia = cobaia[:len(cobaia)-1]
                total = total + 1
            else:
                continue
        
        t1 = t()
        palavras = len(words)
        tempo = t1 - t0
        answer = "Prefixo comum: {}{}Número de ciclos: {}{}Total de palavras procuradas: {}{}Tempo de pesquisa: {} segundos".format(cobaia, "\n", total, "\n", palavras, "\n", round(tempo, 4))
        return answer
      
def maldade_do_T(maldade, média_das_notas):

    while não_chumbarem_todos:

        if média_das_notas > 0:
            return maldade_do_T(maldade + 1, média_das_notas - 1)

def maximum_depth(alist):

    if len(alist) == 0:
        return 1

    if len(alist) == 1:
        return len(str(alist))//2

    else:
        return (len(str(alist))-2*(len(alist)-1))//2

def maximum_depth(l):

    total = 0
    if len(l) == 0:
        return 1

    if len(l) == 1:
        return str(l).count("[")

    else:

        total = 0

        for item in l:
            if len(item) == 0:
                total = total + 1
            if len(item) == 1:
                total = total + str(item).count("[")
            else:
                total = total + maximum_depth(item)
        return total

def combinations(alist):

    combinations = list([(x, y) for x in alist for y in alist if x != y])
    return combinations

def is_coliding(atuple):

    def A_B(atuple):

        # A is to the left of B
        ret_A = atuple[0]
        ret_B = atuple[1]

        first_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        second_condition = ret_A['y1'] in range (ret_B['y2'], ret_B['y1'])

        third_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        fourth_condition = ret_A['y2'] in range (ret_B['y2'], ret_B['y1'])

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    def B_A(atuple):

        # B is to the left of A
        ret_A = atuple[1]
        ret_B = atuple[0]

        first_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        second_condition = ret_A['y1'] in range (ret_B['y2'], ret_B['y1'])

        third_condition = ret_A['x2'] in range (ret_B['x1'], ret_B['x2'])
        fourth_condition = ret_A['y2'] in range (ret_B['y2'], ret_B['y1'])

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    return A_B(atuple) or B_A(atuple)

def number_of_collisions(objects):

    prob_colisions = combinations(objects)

    total = 0
    for item in prob_colisions:

        if is_coliding(item):
            total = total + 1
        else:
            continue

    return total

    # objects = [{'x1': 37, 'y1': 560, 'x2': 48, 'y2': 634}, {'x1': 456, 'y1': 391, 'x2': 539, 'y2': 404}, {'x1': 407, 'y1': 536, 'x2': 468, 'y2': 589}, {'x1': 538, 'y1': 500, 'x2': 633, 'y2': 573}, {'x1': 343, 'y1': 584, 'x2': 407, 'y2': 606}, {'x1': 334, 'y1': 177, 'x2': 371, 'y2': 220}, {'x1': 239, 'y1': 111, 'x2': 325, 'y2': 159}, {'x1': 512, 'y1': 343, 'x2': 540, 'y2': 356}, {'x1': 544, 'y1': 341, 'x2': 578, 'y2': 439}, {'x1': 33, 'y1': 143, 'x2': 57, 'y2': 237}, {'x1': 200, 'y1': 403, 'x2': 260, 'y2': 458}, {'x1': 454, 'y1': 102, 'x2': 516, 'y2': 160}, {'x1': 522, 'y1': 59, 'x2': 578, 'y2': 133}, {'x1': 68, 'y1': 546, 'x2': 112, 'y2': 594}, {'x1': 251, 'y1': 354, 'x2': 268, 'y2': 390}, {'x1': 234, 'y1': 564, 'x2': 260, 'y2': 619}, {'x1': 130, 'y1': 473, 'x2': 163, 'y2': 507}, {'x1': 556, 'y1': 225, 'x2': 630, 'y2': 287}, {'x1': 181, 'y1': 145, 'x2': 232, 'y2': 234}, {'x1': 455, 'y1': 122, 'x2': 516, 'y2': 154}, {'x1': 490, 'y1': 359, 'x2': 545, 'y2': 422}, {'x1': 514, 'y1': 503, 'x2': 613, 'y2': 520}, {'x1': 264, 'y1': 470, 'x2': 290, 'y2': 518}, {'x1': 146, 'y1': 262, 'x2': 157, 'y2': 320}, {'x1': 117, 'y1': 503, 'x2': 155, 'y2': 515}, {'x1': 52, 'y1': 280, 'x2': 91, 'y2': 348}, {'x1': 119, 'y1': 99, 'x2': 191, 'y2': 192}, {'x1': 554, 'y1': 588, 'x2': 636, 'y2': 658}, {'x1': 441, 'y1': 287, 'x2': 478, 'y2': 332}, {'x1': 123, 'y1': 60, 'x2': 185, 'y2': 118}, {'x1': 440, 'y1': 193, 'x2': 484, 'y2': 260}, {'x1': 232, 'y1': 136, 'x2': 248, 'y2': 187}, {'x1': 96, 'y1': 225, 'x2': 174, 'y2': 301}, {'x1': 291, 'y1': 27, 'x2': 311, 'y2': 75}, {'x1': 247, 'y1': 348, 'x2': 257, 'y2': 438}, {'x1': 491, 'y1': 548, 'x2': 570, 'y2': 613}, {'x1': 375, 'y1': 100, 'x2': 420, 'y2': 152}, {'x1': 375, 'y1': 235, 'x2': 398, 'y2': 256}, {'x1': 272, 'y1': 451, 'x2': 294, 'y2': 484}, {'x1': 248, 'y1': 480, 'x2': 342, 'y2': 578}, {'x1': 331, 'y1': 445, 'x2': 406, 'y2': 502}, {'x1': 243, 'y1': 35, 'x2': 322, 'y2': 69}, {'x1': 14, 'y1': 165, 'x2': 98, 'y2': 229}, {'x1': 425, 'y1': 556, 'x2': 464, 'y2': 648}, {'x1': 82, 'y1': 46, 'x2': 162, 'y2': 100}, {'x1': 482, 'y1': 65, 'x2': 532, 'y2': 129}, {'x1': 254, 'y1': 1, 'x2': 329, 'y2': 77}, {'x1': 431, 'y1': 471, 'x2': 504, 'y2': 525}, {'x1': 242, 'y1': 169, 'x2': 306, 'y2': 225}, {'x1': 400, 'y1': 484, 'x2': 420, 'y2': 578}, {'x1': 167, 'y1': 464, 'x2': 246, 'y2': 485}, {'x1': 416, 'y1': 479, 'x2': 443, 'y2': 500}, {'x1': 272, 'y1': 281, 'x2': 358, 'y2': 313}, {'x1': 357, 'y1': 10, 'x2': 444, 'y2': 30}, {'x1': 337, 'y1': 55, 'x2': 421, 'y2': 137}, {'x1': 555, 'y1': 588, 'x2': 624, 'y2': 668}, {'x1': 330, 'y1': 213, 'x2': 395, 'y2': 280}, {'x1': 452, 'y1': 332, 'x2': 540, 'y2': 391}, {'x1': 265, 'y1': 491, 'x2': 301, 'y2': 573}, {'x1': 433, 'y1': 256, 'x2': 450, 'y2': 297}, {'x1': 309, 'y1': 212, 'x2': 376, 'y2': 268}, {'x1': 435, 'y1': 113, 'x2': 467, 'y2': 186}, {'x1': 406, 'y1': 584, 'x2': 420, 'y2': 632}, {'x1': 37, 'y1': 72, 'x2': 137, 'y2': 137}, {'x1': 101, 'y1': 465, 'x2': 191, 'y2': 541}, {'x1': 591, 'y1': 432, 'x2': 644, 'y2': 457}, {'x1': 419, 'y1': 330, 'x2': 481, 'y2': 425}, {'x1': 437, 'y1': 314, 'x2': 475, 'y2': 346}, {'x1': 156, 'y1': 453, 'x2': 176, 'y2': 524}, {'x1': 16, 'y1': 285, 'x2': 90, 'y2': 348}, {'x1': 75, 'y1': 353, 'x2': 94, 'y2': 441}, {'x1': 55, 'y1': 81, 'x2': 72, 'y2': 112}, {'x1': 520, 'y1': 152, 'x2': 544, 'y2': 162}, {'x1': 139, 'y1': 577, 'x2': 225, 'y2': 624}, {'x1': 415, 'y1': 364, 'x2': 438, 'y2': 445}, {'x1': 406, 'y1': 387, 'x2': 459, 'y2': 428}, {'x1': 317, 'y1': 77, 'x2': 390, 'y2': 107}, {'x1': 390, 'y1': 282, 'x2': 439, 'y2': 338}, {'x1': 380, 'y1': 10, 'x2': 460, 'y2': 69}, {'x1': 261, 'y1': 358, 'x2': 336, 'y2': 452}, {'x1': 132, 'y1': 482, 'x2': 214, 'y2': 507}, {'x1': 167, 'y1': 432, 'x2': 250, 'y2': 473}, {'x1': 45, 'y1': 550, 'x2': 137, 'y2': 603}, {'x1': 265, 'y1': 278, 'x2': 315, 'y2': 312}, {'x1': 207, 'y1': 517, 'x2': 227, 'y2': 571}, {'x1': 303, 'y1': 286, 'x2': 320, 'y2': 350}, {'x1': 406, 'y1': 214, 'x2': 493, 'y2': 277}, {'x1': 532, 'y1': 325, 'x2': 549, 'y2': 391}, {'x1': 337, 'y1': 158, 'x2': 355, 'y2': 210}, {'x1': 25, 'y1': 482, 'x2': 53, 'y2': 561}, {'x1': 255, 'y1': 62, 'x2': 317, 'y2': 160}, {'x1': 215, 'y1': 190, 'x2': 284, 'y2': 284}, {'x1': 93, 'y1': 495, 'x2': 185, 'y2': 547}, {'x1': 500, 'y1': 46, 'x2': 539, 'y2': 99}, {'x1': 405, 'y1': 256, 'x2': 481, 'y2': 273}, {'x1': 361, 'y1': 416, 'x2': 419, 'y2': 477}, {'x1': 203, 'y1': 486, 'x2': 237, 'y2': 574}, {'x1': 356, 'y1': 137, 'x2': 415, 'y2': 230}, {'x1': 240, 'y1': 466, 'x2': 252, 'y2': 501}, {'x1': 203, 'y1': 418, 'x2': 289, 'y2': 440}]
    # print(number_of_collisions(objects))

# 2 Tic Tac

def possibilities(board, player):

    def which_is(board, player):

        diagonal_1 = list([board[0][0], board[1][1], board[2][2]])
        diagonal_2 = list([board[0][2], board[1][1], board[2][0]])

        coluna_1 = list([board[0][0], board[0][1], board[0][2]])
        coluna_2 = list([board[1][0], board[1][1], board[1][2]])
        coluna_3 = list([board[2][0], board[2][1], board[2][2]])

        linha_1 = list(board[0])
        linha_2 = list(board[1])
        linha_3 = list(board[2])

        all_possibilities = (diagonal_1, diagonal_2, coluna_1, coluna_2, coluna_3, linha_1, linha_2, linha_3)
        not_player = "x" if player == "o" else "o"

        for item in all_possibilities:
            if item.count(player) == 2 and item.count(not_player) == 0:
                break

        return item
    
    return which_is(board, player)

def string_to_list(astring):

    alist = [[], [], []]

    i = 0
    for item in astring.split("\n"):
        for substring in item:
            alist[i].append(substring)
        i = i + 1

    return alist

def tic_tac_toe(board, player):

    game = string_to_list(board)
    jogada_correcta = possibilities(game, player)

    return jogada_correcta

board = 'x x\n o \nxoo'
player = "o"
print(tic_tac_toe(board, player))
      
def possibilities(board, player):

    def which_is(board, player):

        diagonal_1 = list([board[0][0], board[1][1], board[2][2]])
        diagonal_2 = list([board[0][2], board[1][1], board[2][0]])

        coluna_1 = list([board[0][0], board[1][0], board[2][0]])
        coluna_2 = list([board[0][1], board[1][1], board[2][1]])
        coluna_3 = list([board[0][2], board[1][2], board[2][2]])

        linha_1 = list(board[0])
        linha_2 = list(board[1])
        linha_3 = list(board[2])

        all_possibilities = list([diagonal_1, diagonal_2, coluna_1, coluna_2, coluna_3, linha_1, linha_2, linha_3])
        not_player = "x" if player == "o" else "o"

        for item in all_possibilities:
            if item.count(player) == 2 and not_player not in item:
                break

        return all_possibilities, item

    def coordenadas(atuple):

        letra = 0
        posição = 0

        all_possibilities = atuple[0]
        item = atuple[1]

        if item == all_possibilities[0]:
            # Diagonal 1
            local = item.index(" ")
            return local, local

        if item == all_possibilities[1]:
            # Diagonal 2
            local = item.index(" ")
            return 2-local, local
        
        colunas = list([all_possibilities[2], all_possibilities[3], all_possibilities[4]])
        if item in colunas:
            n = list([colunas[i] for i in range(3) if colunas[i] == item])
            posição = colunas.index(item)
            letra = n[0].index(" ")
            return letra, posição

        linhas = list([all_possibilities[5], all_possibilities[6], all_possibilities[7]])
        if item in linhas:
            n = list([linhas[i] for i in range(3) if linhas[i] == item])
            posição = n[0].index(" ")
            letra = linhas.index(item)
            return letra, posição
    
    return coordenadas(which_is(board, player))

def string_to_matrix(astring):

    alist = [[], [], []]

    i = 0
    for item in astring.split("\n"):
        for substring in item:
            alist[i].append(substring)
        i = i + 1

    return alist

def tic_tac_toe(board, player):

    game = string_to_matrix(board)
    jogada_correcta = possibilities(game, player)

    (letra, posição) = jogada_correcta

    from string import ascii_uppercase as abc
    l = abc[letra]
    i = posição + 1

    return "{}{}".format(l, i)
      
def combinations(alist):

    combinations = list([(x, y) for x in alist for y in alist if x != y])
    return combinations

def is_coliding(atuple):

    def A_B(atuple):

        # A is to the left of B
        ret_A = atuple[0]
        ret_B = atuple[1]

        first_condition = ret_A['x2'] > ret_B['x1'] and ret_A['x2'] < ret_B['x2']
        second_condition = ret_A['y1'] > ret_B['y2'] and ret_A['y1'] < ret_B['y1']

        third_condition = ret_A['x2'] > ret_B['x1'] and ret_A['x2'] < ret_B['x2']
        fourth_condition = ret_A['y2'] > ret_B['y2'] and ret_A['y1'] < ret_B['y1']

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    def B_A(atuple):

        # B is to the left of A
        ret_A = atuple[1]
        ret_B = atuple[0]

        first_condition = ret_A['x2'] > ret_B['x1'] and ret_A['x2'] < ret_B['x2']
        second_condition = ret_A['y1'] > ret_B['y2'] and ret_A['y1'] < ret_B['y1']

        third_condition = ret_A['x2'] > ret_B['x1'] and ret_A['x2'] < ret_B['x2']
        fourth_condition = ret_A['y2'] > ret_B['y2'] and ret_A['y1'] < ret_B['y1']

        return (first_condition and second_condition) or (third_condition and fourth_condition)

    return A_B(atuple) or B_A(atuple)

def number_of_collisions(objects):

    prob_colisions = combinations(objects)

    total = 0
    for item in prob_colisions:

        if is_coliding(item):
            total = total + 1
        else:
            continue

    return total
      
def combinations(alist):

    combinations = list([(x, y) for x in alist for y in alist if x != y])
    return combinations

def is_coliding(atuple):

    ret_A = atuple[0]
    ret_B = atuple[1]

    # If XXs are not close
    answer1 = ret_A['x2'] < ret_B['x1'] or ret_A['x1'] > ret_B['x2'] 

    # If YYs are not close
    # In programming the YYs grow down!
    answer2 = ret_B['y1'] > ret_A['y2'] or ret_A['y1'] > ret_B['y2'] 

    return not (answer1 or answer2)

def number_of_collisions(objects):

    prob_colisions = combinations(objects)

    total = 0
    for item in prob_colisions:

        if is_coliding(item):
            total = total + 1
        else:
            continue
    
    # Duplicate elimination
    answer = total // 2
    return answer
      
def possibilities(board, player):

    def which_is(board, player):

        diagonal_1 = list([board[0][0], board[1][1], board[2][2]])
        diagonal_2 = list([board[0][2], board[1][1], board[2][0]])

        coluna_1 = list([board[0][0], board[1][0], board[2][0]])
        coluna_2 = list([board[0][1], board[1][1], board[2][1]])
        coluna_3 = list([board[0][2], board[1][2], board[2][2]])

        linha_1 = list(board[0])
        linha_2 = list(board[1])
        linha_3 = list(board[2])

        all_possibilities = list([diagonal_1, diagonal_2, coluna_1, coluna_2, coluna_3, linha_1, linha_2, linha_3])
        not_player = "x" if player == "o" else "o"

        for item in all_possibilities:
            if item.count(player) == 2 and not_player not in item:
                break

        return all_possibilities, item

    def coordenadas(atuple):

        letra = 0
        posição = 0

        all_possibilities = atuple[0]
        item = atuple[1]

        if item == all_possibilities[0]:
            # Diagonal 1
            local = item.index(" ")
            return local, local

        if item == all_possibilities[1]:
            # Diagonal 2
            local = item.index(" ")
            return 2-local, local
        
        colunas = list([all_possibilities[2], all_possibilities[3], all_possibilities[4]])
        if item in colunas:
            n = list([colunas[i] for i in range(3) if colunas[i] == item])
            posição = colunas.index(item)
            letra = n[0].index(" ")
            return letra, posição

        linhas = list([all_possibilities[5], all_possibilities[6], all_possibilities[7]])
        if item in linhas:
            n = list([linhas[i] for i in range(3) if linhas[i] == item])
            posição = n[0].index(" ")
            letra = linhas.index(item)
            return letra, posição
    
    return coordenadas(which_is(board, player))

def string_to_matrix(astring):

    alist = [[], [], []]

    i = 0
    for item in astring.split("\n"):
        for substring in item:
            alist[i].append(substring)
        i = i + 1

    return alist

def tic_tac_toe(board, player):

    game = string_to_matrix(board)
    jogada_correcta = possibilities(game, player)

    (letra, posição) = jogada_correcta

    from string import ascii_uppercase as abc
    l = abc[letra]
    i = posição + 1

    return "{}{}".format(l, i)

      import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def card_value(card):
    
    numbers = "2345678910"
    letters = "JQKA"
    double_points = "♠♣"

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters:
        pontos = pontos + 10

    if card[0] in double_points:
        pontos = pontos * 2

    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
    # Randomly play cards from each player's hand until empty

    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

        for name in turn_order:
            card = choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]
        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1
            print(vencedor)

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "
    print(pontos)
    return answer.strip()

print(play(35791113))

      import random
from typing import List, Tuple
import cards

def card_value(card):
    
    numbers = "2345678910"
    letters = "JQKA"
    double_points = "♠♣"

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters:
        pontos = pontos + 10

    if card[0] in double_points:
        pontos = pontos * 2

    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)
    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
    # Randomly play cards from each player's hand until empty

    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

        for name in turn_order:
            card = cards.choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]
        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()

      import random

def cows_bulls(seed):

    # Generate a number with random.seed
    rng = random.Random(seed)
    number = rng.randrange(0000, 10000)
    print(number)
    guess = 9887

    # Comparation
    cows = 0
    index = 0
    for n in str(number):
        if n == str(guess)[index]:
            cows = cows + 1
        else:
            index = index + 1
            continue
    
    bulls = 0
    percorridos = []
    for n in str(number):
        if n in str(guess):
            bulls = bulls + 1
        else:
            continue

    return cows, bulls

seed = 62678
print(cows_bulls(seed))

import random
from typing import List, Tuple
import cards

def card_value(card):
    
    numbers = "2345678910"
    letters = "JQKA"
    double_points = "♠♣"

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters:
        pontos = pontos + 10

    if card[0] in double_points:
        pontos = pontos * 2

    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)
    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
    # Randomly play cards from each player's hand until empty

    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

        for name in turn_order:
            card = cards.choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]
        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()
# Modules import
import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def card_value(card):
    
    numbers = ['2','3','4','5','6','7','8','9','10']
    letters = ['J','Q','K','A']
    double_points = ['♠','♣']

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters and card[1] != 'A':
        pontos = pontos + 10

    if card[1] == 'A':
        pontos = pontos + 11

    if card[0] in double_points:
        pontos = pontos * 2
    
    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)

    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
        
        for name in turn_order:
            card = choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]

        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()

# Another solution, with JCL's module "cards" in FPRO
      
# Import module from FPRO JCL
import cards
import random

def card_value(card):
    
    numbers = ['2','3','4','5','6','7','8','9','10']
    letters = ['J','Q','K','A']
    double_points = ['♠','♣']

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters and card[1] != 'A':
        pontos = pontos + 10

    if card[1] == 'A':
        pontos = pontos + 11

    if card[0] in double_points:
        pontos = pontos * 2
    
    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)

    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
        
        for name in turn_order:
            card = cards.choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]

        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()

seed = 98765432
print(play(seed))
seed = 98765432
print(play(seed))
      
      
      def partida(board):

    cardinal = ["N", "S", "E", "O"]

    # Search in matriz
    for x, y in enumerate(board):
        for z, c in enumerate(y):
            if c in cardinal:

                ponto = (x, z)
                sentido_inicial = c

                return ponto, sentido_inicial

def new_direction(coordinate, objecto):

    return new_coordinate

def move_ball(board):

    coordinates = []

    directions = {
        "N" : (0, -1),
        "S" : (0, +1),
        "E" : (+1, 0),
        "O" : (-1, 0),
    }

    final = "x"
    begin = partida(board)
    coordinates.append(begin[0])

    x = begin[0][0]
    y = begin[0][1]
    rumo = begin[1]

    while final not in board[x][y]:

        sentido = directions[rumo]


        #Atenção a isto!!
        coordinates.append(x+sentido[1], y+sentido[0])
        rumo = new_direction(rumo, board[x][y])

    return coordinates

board = ['E \\', '/ /', '   ', '\\ X']
print(move_ball(board))

      # Import module random
import random

def cows_bulls(seed):
    
    # Random seed from FPRO
    random.seed(seed)
    
    def how_many(guess):

        certo = random.randint(0000, 9999)
        
        correct = [x for x in str(certo)]
        number = [x for x in str(guess)]
        
        # Cows - Correct number in correct position
        cows = 0
        for index, value in enumerate(number):

            if value == correct[index]:                
                if index == correct.index(value):
                        
                        cows = cows + 1
                        correct[index] = "x"
                        
        # Bulls - Correct number in wrong position
        bulls = 0        
        for index, value in enumerate(number):
           
            if value in correct:      
                bulls = bulls + 1
                correct[correct.index(value)] = "x"
                    
        return cows, bulls
    
    return how_many
      
  def partida(board):

    cardinal = ["N", "S", "E", "O"]

    # Search in matriz
    for x, y in enumerate(board):
        for z, c in enumerate(y):
            if c in cardinal:

                ponto = (x, z)
                sentido_inicial = c

                return ponto, sentido_inicial

def new_direction(coordinate, objecto):

    if objecto == "\\" and (coordinate == "E" or coordinate == "S"):
        c = ["E", "S"]
        return c[c.index(coordinate)-1]

    if objecto == "\\" and (coordinate == "O" or coordinate == "N"):
        c = ["O", "N"]
        return c[c.index(coordinate)-1]

    if objecto == "/" and (coordinate == "E" or coordinate == "N"):
        c = ["E", "N"]
        return c[c.index(coordinate)-1]

    if objecto == "/" and (coordinate == "O" or coordinate == "S"):
        c = ["O", "S"]
        return c[c.index(coordinate)-1]

    return coordinate

def move_ball(board):

    coordinates = []

    directions = {
        "N" : (0, -1),
        "S" : (0, +1),
        "E" : (+1, 0),
        "O" : (-1, 0),
    }

    begin = partida(board)
    final = "X"
    coordinates.append(begin[0])

    x = begin[0][0]
    y = begin[0][1]
    rumo = begin[1]

    while final not in board[x][y]:

        sentido = directions[rumo]
        x = x + sentido[1]
        y = y + sentido[0]
        coordinates.append((x, y))
        rumo = new_direction(rumo, board[x][y])

    return coordinates
      
 def ordenação(alist):
    return sorted(alist, key = lambda x: x[0])

def distâncias(ponto1, ponto2):

    from math import sqrt as raiz
    x1 = ponto1[0]
    x2 = ponto2[0]
    y1 = ponto1[1]
    y2 = ponto2[1]

    distance = round(raiz((x1 - x2)**2 + (y1 - y2)**2))
    return distance

def separação(alist):

    middle = len(alist)//2

    left = alist[:middle]
    right = alist[middle:]

    return (left, right)

def closest_pair(points):

    # Initial conditions
    if len(points) == 2:
        return distâncias(points[1], points[0])
    if len(points) == 3:
        return min( distâncias(points[0], points[1]), 
                    distâncias(points[0], points[2]), 
                    distâncias(points[1], points[2]))

    points = ordenação(points)

    left = separação(points)[0]
    right = separação(points)[1]

    min_distance = min(closest_pair(left), closest_pair(right))

    all_values = list([min_distance]) + list([distâncias(l, r) for l in left for r in right if abs(r[0]-l[0]) < min_distance])
    answer = min(all_values)

    return answer
      
 def search_map(amap, map_rectangle, search_rectangle):

    # Condição Base
    if amap is None:
        return set()
    
    if type(amap) == str:
        return set(amap)

    # Definir os mapas
    mapx = map_rectangle[0]
    mapy = map_rectangle[1]
    mapz = map_rectangle[2]
    mapt = map_rectangle[3]

    # Definir áreas procuradas
    x = search_rectangle[0]
    y = search_rectangle[1]
    z = search_rectangle[2]
    t = search_rectangle[3]

    answer = set() # Acumulador dos objectos

    if x <= mapx + mapz/2 and y <= mapy + mapt/2:
        # Se estiver no quadrante 1, chamada recursiva
        answer = answer | search_map(amap[0], (mapx, mapy, mapz/2, mapt/2), search_rectangle)

    if (x + z) >= mapx + mapz/2 and y <= mapy + mapt/2:
        # Se estiver no quadrante 2, chamada recursiva
        answer = answer | search_map(amap[1], (mapx + mapz/2, mapy, mapz/2, mapt/2), search_rectangle)

    if (x + z) >= mapx + z/2 and (y + t) >= mapy + mapt/2:
        # Se estiver no quadrante 3, chamada recursiva
        answer = answer | search_map(amap[2], (mapx + mapz/2, mapy + mapt/2, mapz/2, mapt/2), search_rectangle)

    if x <= mapx + mapz/2 and (y + t) >= mapy + mapt/2:
        # Se estiver no quadrante 4, chamada recursiva
        answer = answer | search_map(amap[3], (mapx, mapy + mapt/2, mapz/2, mapt/2), search_rectangle)

    return set(answer)

map_rectangle = (0, 0, 735, 959)
search_retangle = (417, 697, 316, 238)

print(search_map(('A', (None, None, 'E', 'F'), ('D', None, None, 'B'), 'C'), map_rectangle, search_retangle))
      
def maximum_depth(alist):
    
    # Caso base
    if alist == []:
        return 1

    # Else
    total = 0
    for item in alist:
        sub_total = maximum_depth(item)
        if sub_total > total:
            total = sub_total

    total = total + 1 # Add [] form        
    return total
      
def maximum_depth(alist):
    
    # Caso base
    if alist == []:
        return 1

    # Else
    total = 0
    for item in alist:
        sub_total = maximum_depth(item)
        if sub_total > total:
            total = sub_total

    total = total + 1 # Add [] form        
    return total

# First solution

# importing functools for reduce()
import functools

def nested_fmr(f, m, r, lst):
    # using recursion to deal with the nested list
    # base case
    if type(lst) != list:
        return lst
    # iteration with the recursive call
    aux = []
    for l in lst:
        aux.append(nested_fmr(f, m, r, l))
    
    return functools.reduce(r, map(m, filter(f, aux)))

# Second solution

def nested_fmr2(f, m, r, lst):
    # solve it with the focus on data (as in PE04)  
    if type(lst) != list:
        return lst
    aux = [nested_fmr2(f, m, r, l) for l in lst]

    return functools.reduce(r, map(m, filter(f, aux)))

# Created on January, 2021
# @author: Fábio Araújo de Sá

def which_room(name):
    
    # A dict with all allowed exam's classrooms
    classrooms = {  
                    'B104': ("Adam Gershenson Nogueira", "Fábio Cunha Morais"),
                    'B201': ("Felipe Siqueira Espinheira", "Gustavo Miguel Soeiro Machado"),
                    'B207': ("Henrique Oliveira Silva", "José Marcelino Zacarias Júnior"),
                    'B208': ("José Maria Borges Pires do Couto e Castro", "Nuno André Gomes França"),
                    'B213': ("Nuno Francisco Moreira dos Santos", "Walter Muhanyele Massango") 
                 }

    # Name normalization
    name = name.strip()
    name_list = name.split(" ")

    # Find a correct classroom
    correct_classroom = ""
    counter = 0
    for key in classrooms.keys():

        # Initial conditions
        start = ((classrooms[key])[0]).split(" ")
        end = ((classrooms[key])[1]).split(" ")
        name_search = name_list[counter]

        # Search
        if name_search >= start[counter] and name_search <= end[counter]:
            correct_classroom = key

    # Get answers    
    answer_1 = "A tua sala é a {}".format(correct_classroom)
    block = correct_classroom[0]
    floor = correct_classroom[1]
    door = int(correct_classroom[2:])
    answer_2 = "Exame no bloco {}, piso {} e na porta {}".format(block, floor, door)
    
    return "{}{}{}{}{}".format(answer_1, "\n", "Informações adicionais:", "\n", answer_2)

    # name = str(input("Qual o teu nome? \n"))
    # print(which_room(name))
      
def intro():

    # Introduction
    print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")

    # Possibilities
    print("A. Grab a nearby rock and throw it at the orc")
    print("B. Lie down and wait to be mauled")
    print("C. Run")

    answer_intro = str(input("Your choice: ")).strip()
    game_over = "Welp, that was quick. You died!"

    if answer_intro.upper() == "A":
        rock() 
    if answer_intro.upper() == "B":
        print(game_over)
    if answer_intro.upper() == "C":
        run()

def rock():

    # Introduction
    print("The orc is stunned, but regains control. He begins running towards you again.")

    # Possibilities
    print("A. Run")
    print("B. Throw another rock")
    print("C. Run towards a nearby cave")

    answer_rock = str(input("Your choice: ")).strip()
    game_over = "The rock flew well over the orcs head. You missed. You died!"

    if answer_rock.upper() == "A":
        run() 
    if answer_rock.upper() == "B":
        print(game_over)
    if answer_rock.upper() == "C":
        cave()

def run():

    # Introduction
    print("You run as quickly as possible.")

    # Possibilities
    print("A. Hide behind boulder")
    print("B. Trapped, so you fight")
    print("C. Run towards an abandoned town")

    run_answer = str(input("Your choice: ")).strip()

    if run_answer.upper() == "A":
        print("You're easily spotted. You died!")
    if run_answer.upper() == "B":
        print("You're no match for an orc. You died!")
    if run_answer.upper() == "C":
        town()

def cave():

    # Introduction
    print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
    sword = str(input("Your choice: ")).strip()

    print("What do you do next?")
    # Possibilities
    print("A. Hide in silence")
    print("B. Fight")
    print("C. Run")

    cave_answer = str(input("Your choice: ")).strip()
    game_over1 = "I think orcs can see very well in the dark, right? You died!"
    game_over2 = "You're defenseless. You died!"

    if cave_answer.upper() == "A":
        print(game_over1)
    if cave_answer.upper() == "B":
        if sword.upper() == "Y":
            print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
        if sword.upper() == "N":
            print(game_over2)
    if cave_answer.upper() == "C":
        print("The orc turns around and sees you running.")
        run()

def town():

    # Introduction
    print("You notice a purple flower near your foot. Do you pick it up? Y/N")

    town_answer = str(input("Your choice: ")).strip()

    if town_answer.upper() == "Y":
        print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
    if town_answer.upper() == "N":
        print("Maybe you should have picked up the flower. You died!")

intro()

def division(a, b):

    try:
        number = a/b
        return "{}/{} = {}".format(a, b, number)

    except ZeroDivisionError:
        return "can't divide by 0!"
        
    except TypeError:
        return "unsupported operand type(s) for division"
      
def longest(filename):

    longest_word = []
    length = 0

    with open(filename, "r") as this_file:
        for line in this_file:
            search = line.split(" ")
            for word in search:
                if len(word) > length:
                    longest_word.append(word)
                    length = len(word)

    return longest_word[-1]
        
def reciprocals(alist):

    answer = []

    for item in alist:

        try:
            number = 1/item
            answer.append(round(number, 3))
        
        except TypeError:
            continue
            
        except ZeroDivisionError:
            continue

    return answer

def count_exceptions(f, n1, n2):

    counter = 0
    integers = list([x for x in range(n1, n2+1)])

    for number in integers:

        try:
            f(number)

        except: # Any error
            counter = counter + 1
            continue

    return counter

      def interleave(f1, f2):

    result = ""

    with open(f1, "r") as file_1:
        with open(f2, "r") as file_2:
            
            lines_f1 = list([line for line in file_1])
            lines_f2 = list([line for line in file_2])

            for l1 in lines_f1:
                for l2 in lines_f2:

                    if lines_f1.index(l1) == lines_f2.index(l2):
                        result = result + l1 + l2
    
    return result
      
def mail_merge(names, mail_template):

    all_emails = []

    with open(names, "r") as nomes:
        all_names = nomes.readlines()

    with open(mail_template, "r") as email:
        template = email.read()

    for name in all_names:
        new_email = template.replace("<name>", name[:-1])
        all_emails.append(new_email)

    return all_emails
      
def diff(filename1, filename2):

    all_lines = []
    mais = "+ "
    menos = "- "

    with open(filename1, "r") as f1:
        lines_1 = list([line for line in f1.readlines()])

    with open(filename2, "r") as f2:
        lines_2 = list([line for line in f2.readlines()])

    for line in lines_1:
        local_line = ""
        if line in lines_2:
            local_line = menos + line
            all_lines.append(local_line)
        else:
            local_line = mais + line
            all_lines.append(local_line)

    return all_lines
      
def diff(filename1, filename2):

    all_lines = []
    mais = "+ "
    menos = "- "

    with open(filename1, "r") as f1:
        lines_1 = list([line for line in f1.readlines()])

    with open(filename2, "r") as f2:
        lines_2 = list([line for line in f2.readlines()])

    for line1 in lines_1:
        for line2 in lines_2:

            if lines_1.index(line1) == lines_2.index(line2):

                local_line = ""

                if line1 not in lines_2:
                    local_line = local_line + menos + line1
                    all_lines.append(local_line)

    for line1 in lines_1:
        for line2 in lines_2:

            if lines_1.index(line1) == lines_2.index(line2):

                local_line = ""

                if line2 not in lines_1:
                    local_line = local_line + mais + line2
                    all_lines.append(local_line)

    result = ""
    for item in all_lines:
        result = result + item
    
    return result

def nested_exceptions(tree):

    all_answers = []

    for item in tree:

        # Base case, is a function
        if callable(item):
            try:
                item()
                all_answers.append(False)
            except:
                all_answers.append(True)

        else:
            # Recursive search
            something = nested_exceptions(item)
            all_answers.append(something)

    answers = tuple(all_answers)
    return answers
      
def lists_to_dict(list1, list2):
    
    result = {}
    
    for key in list1:
        for value in list2:
            
            if list1.index(key) == list2.index(value):
                
                result[key] = value
                
    return result
                
def sum_dicts(lst):
    
    result = {}
    
    for dictionary in lst:
        for key in dictionary:
            
            result[key] = 0
    
    for dictionary in lst:
        for key in dictionary:
            
            result[key] = result[key] + dictionary[key]
            
            
    return result
      
def rec_fib(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    else:
        return rec_fib(n-1) + rec_fib(n-2)
    
    
def fib(start, end):
    
    all_numbers = []
    
    for n in range(start, end+1):
        all_numbers.append(rec_fib(n))
    
    for number in all_numbers:
        yield number
      
def overlaps(segments):
    
    result = []
    
    for i in range(len(segments)):
        
        for j in range(i, len(segments)):
            
            if j > i:
                
                alist1 = [x for x in range(segments[i][0], segments[i][1])]
                alist2 = [x for x in range(segments[j][0], segments[j][1])]
                local_tuple = ()
                
                for number in alist2:
                    if number in alist1:
                        
                        # Interseção!
                        local_tuple = i, j
                        result.append(local_tuple)

    return set(result)
      
import functools, itertools

def rec_hof(hofs, lst):
    
    # Se já não houver funções, a lista pretendida é a que está em lst
    if hofs == []:
        return lst
    
    # Se ainda houver funções, chamada recursiva entre o resto das funções e 
    # a lista derivada da função em índice 0

    else:
        return rec_hof(hofs[:len(hofs)-1], hofs[-1][0](hofs[-1][1], lst))
import time

def rec_fib(n):

    fib_values = {

        1 : 1,
        2 : 1,
        3 : 2,

    }

    if n in fib_values.keys():
        return fib_values[n]

    else:
        fib_values[n] = rec_fib(n-1) + rec_fib(n-2)
        return fib_values[n]

    
def fib(start, end):
    
    all_numbers = []
    total = 0
    t0 = time.perf_counter()

    for n in range(start, end+1):
        print("Número {} da Sequência de Fibonacci --> {}".format(n, rec_fib(n)))
        t1 = time.perf_counter()
        total = total + t1
        print("Tempo que demorou: {} segundos".format(round(t1-t0, 2)))
        print(" ")
        all_numbers.append(rec_fib(n))
    
    t1 = time.perf_counter()
    
    print(" ")
    return "Processo finalizado. Tempo total utilizado: {} minutos!".format(total//60)

start = 10
end = 40
print(fib(10, 40))

      
import time

def rec_fib(n, fib_values):

    if n in fib_values.keys():
        return fib_values[n]

    else:
        fib_values[n] = rec_fib(n-1, fib_values) + rec_fib(n-2, fib_values)
        return fib_values[n]

    
def fib(start, end):
    
    all_numbers = []

    fib_values = {
        
        1 : 1,
        2 : 1,
        3 : 2, 

    }

    total = 0
    t0 = time.perf_counter()

    for n in range(start, end+1):
        print("Número {} da Sequência de Fibonacci --> {}".format(n, rec_fib(n, fib_values)))
        t1 = time.perf_counter()
        total = total + t1
        print("Tempo que demorou: {} segundos".format(round(t1-t0, 2)))
        print(" ")
        all_numbers.append(rec_fib(n, fib_values))
    
    t1 = time.perf_counter()
    
    print(" ")
    return "Processo finalizado. Tempo total utilizado: {} segundos!".format(round(total, 2))
    
931487 segundos = 10 dias aproximadamente!
start = 1
end = 10000
print(fib(start, end))
      
def is_overlap(s1, s2) -> bool:
    """ find out if the two segments (start, end) overlap """
    return not (s1[0] > s2[1] or s1[1] < s2[0])
    
def overlaps(segments):
    # using a set comprehension, compare each segment with all the others
    return {(i, j) for i in range(len(segments)) for j in range(i+1, len(segments)) if is_overlap(segments[i], segments[j])}
      
# alternative solution 1
def rec_hof(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists
    aux = [rec_hof(hofs[1:], x) for x in lst]
    # apply the first higher-order function to the sub-lists
    (f_op, f_arg) = hofs[0]
    return f_op(f_arg, aux)

# alternative solution 2
def rec_hof2(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists
    aux = []
    for l in lst:
        aux.append(rec_hof(hofs[1:], l))
        # apply the first higher-order function to the sub-lists
        (f_op, f_arg) = hofs[0]

    return f_op(f_arg, aux)

# alternative solution 3
import functools
def rec_hof3(hofs, lst):

    if hofs == []:
    # base case, there's no more functions to apply
        return lst

    # get the transformed sub-lists using partial function application
    aux = map(functools.partial(rec_hof, hofs[1:]), lst)
    # apply the first higher-order function to the sub-lists
    (f_op, f_arg) = hofs[0]

    return f_op(f_arg, aux)
      
import difflib
def diff(filename1, filename2):

    file1 = open(filename1, 'r').readlines()
    one = list([" " + line for line in file1])
    file2 = open(filename2, 'r').readlines()
    two = list([" " + line for line in file2])

    diff = difflib.unified_diff(one, two)
    delta = ''.join(diff)
    return delta[26:]

print(len("--- \n+++ \n@@ -1,5 +1,5 @@\n"))

from difflib import unified_diff as df
# https://docs.python.org/3/library/difflib.html

def diff(filename1, filename2):

    file1 = open(filename1, 'r').readlines()
    one = list([" " + line for line in file1])
    file2 = open(filename2, 'r').readlines()
    two = list([" " + line for line in file2])

    difference = list(df(one, two, fromfile = "file1", tofile = "file2", lineterm=""))
    
    for line in difference:
        if line[0] == " ":
            difference.remove(line)

    acumulator = ""
    for line in difference:
        acumulator = acumulator + line

    return acumulator[33:]

      def is_column(board):

    for possible_winner in [1, 2]:
        for c in range(len(board[0])):
            for r in range(len(board)-3):

                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    if board[r][c] == possible_winner:
                        return tuple((r, c))

    return False

def is_row(board):

    for possible_winner in [1, 2]:
        for c in range(len(board[0])-3):
            for r in range(len(board)):

                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    if board[r][c] == possible_winner:
                        return tuple((r, c))  

    return False

def is_diagonal(board):

    def diagonal_positiva(board):

        for possible_winner in [1, 2]:
            for c in range(len(board[0])-3):
                for r in range(len(board)-3):

                    if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                        if board[r][c] == possible_winner:
                            return tuple(("positiva", r, c))

        return False

    def diagonal_negativa(board):
        
        for possible_winner in [1, 2]:
            for c in range(len(board[0])-3):
                for r in range(3, len(board)):

                    if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                        if board[r][c] == possible_winner:
                            return tuple(("negativa", r, c))
        
        return False 

    return diagonal_positiva(board) if diagonal_positiva(board) != False else diagonal_negativa(board)

def four_in_line(board):

    result = set()

    if is_column(board) != False:

        x, y = is_column(board)

        result.add((x, y))
        result.add((x+3, y))

    if is_row(board) != False:

        x, y = is_row(board)

        result.add((x, y))
        result.add((x, y+3))

    if is_diagonal(board) != False:

        pos_or_neg, x, y = is_diagonal(board)

        if pos_or_neg == "positiva":

            result.add((x, y))
            result.add((x+3,y+3))

        if pos_or_neg == "negativa":

            result.add((x, y))
            result.add((x-3, y+3))

    return result

def find_all_zeros(board):

    alist = []

    for x in range(len(board[0])):
        for y in range(len(board)):

            if board[x][y] == 0:
                atuple = tuple((x, y))
                alist.append(atuple)

    return alist

def is_row(board, coordinate, possibilities):
    
    row = board[coordinate[0]]
    value = sum(possibilities) - sum(row)
    
    return value, row

def is_column(board, coordinate, possibilities):

    column = [board[x][coordinate[1]] for x in range(len(board))]
    value = sum(possibilities) - sum(column)

    return value, column

def is_square(board, coordinate, possibilities):

    def which_quadrant(coordinate, board):
    
        y, x = coordinate

        # Q == (1 or 2 or 3)
        if y < 3:
            if x < 3:
                return list([board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]])
            if x >= 3 and x < 6:
                return list([board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]])
            if x >= 6 and x < 9:
                return list([board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]])

        # Q == (4 or 5 or 6)
        if y >= 3 and y < 6:
            if x < 3:
                return list([board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]])
            if x >= 3 and x < 6:
                return list([board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]])
            if x >= 6 and x < 9:
                return list([board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]])

        # Q == (7 or 8 or 9)        
        if y >= 6 and y < 9:
            if x < 3:
                return list([board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]])
            if x >= 3 and x < 6:
                return list([board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]])
            if x >= 6 and x < 9:
                return list([board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]])

        return "Error!"

    square = which_quadrant(coordinate, board)
    value = sum(possibilities) - sum(square)

    return value, square

def solve_sudoku(board):

    possibilities = list([x for x in range(1, 10)])
    all_zeros = find_all_zeros(board)

    for coordinate in all_zeros:

        vc, column = is_column(board, coordinate, possibilities)
        vr, row = is_row(board, coordinate, possibilities)
        vs, square = is_square(board, coordinate, possibilities)

        if vs != 0 and vs not in square:
            board[coordinate[0]][coordinate[1]] = vs   

        if vr != 0 and vr not in row:
            board[coordinate[0]][coordinate[1]] = vr   

        if vc != 0 and vc not in column:
            board[coordinate[0]][coordinate[1]] = vc

    return board

board =[[9, 3, 7, 1, 4, 2, 5, 8, 6], 
        [5, 6, 2, 7, 3, 8, 1, 4, 0], 
        [4, 8, 1, 9, 5, 6, 7, 2, 3], 
        [1, 4, 6, 0, 9, 3, 8, 5, 0], 
        [3, 2, 5, 6, 8, 7, 9, 1, 4], 
        [8, 7, 9, 4, 0, 5, 3, 6, 2], 
        [7, 9, 4, 8, 2, 1, 6, 3, 5], 
        [6, 5, 8, 3, 7, 4, 2, 9, 1], 
        [2, 1, 3, 5, 6, 9, 4, 7, 8]]

print(solve_sudoku(board))

      def find_it(seq):

    adict = {}
    
    for number in seq:
        if number in adict.keys():
            adict[number] += 1
        else:
            adict[number] = adict.get(number, 0) + 1
    
    for number in adict.keys():
        if adict[number]%2 == 1:
            return number

    return "There isn't a odd occurence"

def morse_code(a_message):

    morse = {   
                'A':'.-', 
                'B':'-...', 
                'C':'-.-.', 
                'D':'-..', 
                'E':'.', 
                'F':'..-.', 
                'G':'--.', 
                'H':'....', 
                'I':'..', 
                'J':'.---', 
                'K':'-.-', 
                'L':'.-..', 
                'M':'--', 
                'N':'-.', 
                'O':'---', 
                'P':'.--.', 
                'Q':'--.-', 
                'R':'.-.', 
                'S':'...', 
                'T':'-', 
                'U':'..-', 
                'V':'...-', 
                'W':'.--', 
                'X':'-..-', 
                'Y':'-.--', 
                'Z':'--..', 
                '1':'.----', 
                '2':'..---', 
                '3':'...--', 
                '4':'....-', 
                '5':'.....', 
                '6':'-....', 
                '7':'--...', 
                '8':'---..', 
                '9':'----.', 
                '0':'-----', 
                ', ':'--..--', 
                '.':'.-.-.-', 
                '?':'..--..', 
                '/':'-..-.', 
                '-':'-....-', 
                '(':'-.--.', 
                ')':'-.--.-'     
                
            } 

    def encrypt(message, morse):

        # Split parts of message --> words, sentences
        sentences_words = list([sentence.split(" ") for sentence in message.split(".")])
        print(sentences_words)
        answer = "" # Acumulator
        for sentence in sentences_words:
            for word in sentence:
                for letter in word:

                    try:
                        answer = answer + morse[letter]
                    except:
                        continue

                answer = answer + " " # Add space
            answer = answer + "/ " # Add comma for next sentence
        
        return answer.strip() # Remove needless spaces

    def decrypt(message, morse):

        # Split parts of message --> words, sentences
        sentences_words = list([sentence.split(" ") for sentence in message.split("/")])
        print(sentences_words)
        answer = "" # Acumulator
        for sentence in sentences_words:
            print(sentence)
            for word in sentence:
                print(word)
                for letter in word:

                    answer = answer + morse[letter]


                answer = answer + " " # Add space
            answer = answer + " / "
        return answer.strip() # Remove needless spaces

    # Alphabetic import
    from string import ascii_letters as abc 

    # Imput normalization ()
    message = str(a_message).strip().replace(". ",".").replace(", ", " ").upper()

    if message[0] in abc:
        # Return an encrypted message:
        return encrypt(message, morse)

    if message[0] not in abc:
        # Return a decrypted message:
        return decrypt(message, morse)

    else:
        return "Input error. Try again!"

print(morse_code("isto e apenas, mais um. um teste"))

def which_room(student):
      
    student_dist = 
      
      {
      'B101': ("Adam Gershenson Nogueira", "Alexandre Guimaraes Gomes Correia"),
      'B104': ("Alexandre Manuel Luz Rodrigues da Costa", "Duarte Filipe Campos Barbosa Lopes"),
      'B105': ("Eduardo Duarte da Silva", "Francisco Lopes Mendonça"),
      'B201': ("Francisco Miguel Alcobia Maia Prada", "Guilherme Soares Sequeira"),
      'B203': ("Guilherme Valler Moreira", "Igor Liberato de Castro"),
      'B204': ("Igor Rodrigues Diniz", "Joana Inês Gonçalves dos Santos"),
      'B207': ("Joana Vale Amaro de Sousa", "José Marcelino Zacarias Júnior"),
      'B208': ("José Maria Borges Pires do Couto e Castro", "Mariana Mota Azevedo"),
      'B213': ("Mariana Solange Monteiro Rocha", "Pedro Miguel Magalhães Nunes"),
      'B304': ("Pedro Miguel Moreira Ramalho", "Ricardo Filipe Resende Teixeira Pereira"),
      'B305': ("Ricardo Jorge Costa Nogueira", "Sérgio Manuel de Sousa Carvalho e Boura Carvalhais"),
      'B311': ("Simião Jorge Mavie", "Walter Muhanyele Massango") 
      }

    from unidecode import unidecode

    def name_in(name, left, right):
        return unidecode(left).lower() <= unidecode(name).lower() <= unidecode(right).lower()

name = input("Give me the full Name? ")
room = [k for k, v in student_dist.items() if name_in(name, v[0], v[1])]
if len(room): 
      print(f"In the next assign '{name}' goes to '{room[0]}'!")

def begin():

    # Introduction
    print(" ")
    print("Welcome to another text-based game!")

    # Possibilities
    print("Which language do you prefere to cath the adventure?\nEN --> English\nPT --> Portuguese")
    answer = str(input("Your choice: ")).strip()

    if answer.upper() == "EN":
        en_adventure()
    if answer.upper() == "PT":
        pt_adventure()
    else:
        print("Your input is not valid. Try again!")
        print(" ")
        begin()

def pt_adventure():
        
    def intro():

        # Introduction
        print("Depois de uma noite de copos com amigos, acordas numa floresta sombria e assustadora. De repente um ogre começa a correr na tua direção")

        # Possibilities
        print("A. Agarras na pedra mais próxima e atiras na direção do ogre")
        print("B. Deitaste e esperas ser atacado")
        print("C. Corres")

        answer_intro = str(input("A tua escolha: ")).strip()
        game_over = "Bem, foi uma caçada rápida. Morreste!"

        if answer_intro.upper() == "A":
            rock() 
        if answer_intro.upper() == "B":
            print(game_over)
        if answer_intro.upper() == "C":
            run()

    def rock():

        # Introduction
        print("O ogre está distraído, mas ainda está à tua procura. Entretanto, ele continua a correr atrás de ti...")

        # Possibilities
        print("A. Corres")
        print("B. Pegas noutra rocha")
        print("C. Corres até à caverna mais próxima")

        answer_rock = str(input("A tua escolha ")).strip()
        game_over = "A pedra parece apropriada para despistar um ogre. Mas não funcionou. Morreste!"

        if answer_rock.upper() == "A":
            run() 
        if answer_rock.upper() == "B":
            print(game_over)
        if answer_rock.upper() == "C":
            cave()

    def run():

        # Introduction
        print("Então tu correr o mais rápido que consegues e...")

        # Possibilities
        print("A. Escondeste atrás de um pedregulho")
        print("B. Ficas encurralado, a tua única solução é lutar")
        print("C. Corres em direção à vila abandonada")

        run_answer = str(input("A tua escolha: ")).strip()

        if run_answer.upper() == "A":
            print("Esondeste-te num spot fraco. Morreste!")
        if run_answer.upper() == "B":
            print("Não és um alvo difícil para um ogre. Morreste!")
        if run_answer.upper() == "C":
            town()

    def cave():

        # Introduction
        print("Antes de entrar totalmente, notas uma espada brilhante no chão. Pegas na espada? S/N")
        sword = str(input("A tua escolha: ")).strip()

        print("O que vais fazer a seguir?")
        # Possibilities
        print("A. Esconder-me em silêncio")
        print("B. Lutar")
        print("C. Correr")

        cave_answer = str(input("A tua escolha: ")).strip()
        game_over1 = "Penso que os ogres conseguem ver muito bem no escuro. Morreste!"
        game_over2 = "Estás indefeso. Morreste!"

        if cave_answer.upper() == "A":
            print(game_over1)
        if cave_answer.upper() == "B":
            if sword.upper() == "S":
                print("Ainda bem que pegaste na espada! Com uma luta empiedosa conseguiste derrotá-lo. Sobreviveste!")
            if sword.upper() == "N":
                print(game_over2)
        if cave_answer.upper() == "C":
            print("O ogre olha para trás e vê-te a correr sem parar")
            run()

    def town():

        # Introduction
        print("Durante a fuga encontras uma pela flor no meio do caminho. Pegas nela? S/N")

        town_answer = str(input("A tua escolha: ")).strip()

        if town_answer.upper() == "S":
            print("Pegas rapidamente na flor roxa. Afinal o ogre estava somente à procura do seu amor. Sim, isto ficou estranho, mas pelo menos sobreviveste!")
        if town_answer.upper() == "N":
            print("Talvez o melhor a fazer era teres pegado a flor. Morreste!")

    intro()

def en_adventure():

    def intro():

        # Introduction
        print("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.")

        # Possibilities
        print("A. Grab a nearby rock and throw it at the orc")
        print("B. Lie down and wait to be mauled")
        print("C. Run")

        answer_intro = str(input("Your choice: ")).strip()
        game_over = "Welp, that was quick. You died!"

        if answer_intro.upper() == "A":
            rock() 
        if answer_intro.upper() == "B":
            print(game_over)
        if answer_intro.upper() == "C":
            run()

    def rock():

        # Introduction
        print("The orc is stunned, but regains control. He begins running towards you again.")

        # Possibilities
        print("A. Run")
        print("B. Throw another rock")
        print("C. Run towards a nearby cave")

        answer_rock = str(input("Your choice: ")).strip()
        game_over = "The rock flew well over the orcs head. You missed. You died!"

        if answer_rock.upper() == "A":
            run() 
        if answer_rock.upper() == "B":
            print(game_over)
        if answer_rock.upper() == "C":
            cave()

    def run():

        # Introduction
        print("You run as quickly as possible.")

        # Possibilities
        print("A. Hide behind boulder")
        print("B. Trapped, so you fight")
        print("C. Run towards an abandoned town")

        run_answer = str(input("Your choice: ")).strip()

        if run_answer.upper() == "A":
            print("You're easily spotted. You died!")
        if run_answer.upper() == "B":
            print("You're no match for an orc. You died!")
        if run_answer.upper() == "C":
            town()

    def cave():

        # Introduction
        print("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?")
        sword = str(input("Your choice: ")).strip()

        print("What do you do next?")
        # Possibilities
        print("A. Hide in silence")
        print("B. Fight")
        print("C. Run")

        cave_answer = str(input("Your choice: ")).strip()
        game_over1 = "I think orcs can see very well in the dark, right? You died!"
        game_over2 = "You're defenseless. You died!"

        if cave_answer.upper() == "A":
            print(game_over1)
        if cave_answer.upper() == "B":
            if sword.upper() == "Y":
                print("As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!")
            if sword.upper() == "N":
                print(game_over2)
        if cave_answer.upper() == "C":
            print("The orc turns around and sees you running.")
            run()

    def town():

        # Introduction
        print("You notice a purple flower near your foot. Do you pick it up? Y/N")

        town_answer = str(input("Your choice: ")).strip()

        if town_answer.upper() == "Y":
            print("You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!")
        if town_answer.upper() == "N":
            print("Maybe you should have picked up the flower. You died!")

    intro()

if __name__ == "__main__":
    begin()

def argmax1(lst):
    return (lst.index(max(lst)))

def argmax2(lst):

    maior = -10000000
    for number in lst:
        if number > maior:
            maior = number

    for index in range(len(lst)):
        if maior == lst[index]:
            return index
        index = index + 1

    return None

def sum_sublists(lst):

    sum_lists = []

    pointer = 0
    index_max = len(lst[0])

    while pointer < index_max:

        total = 0
        for sublist in lst:
            total = total + sublist[pointer]

        sum_lists.append(total)
        pointer = pointer + 1

    return sum_lists

def sqrt(num, k):

    answer_list = []
    auxiliar = num
    delta = 100

    # List constructor
    initial = auxiliar / 2
    answer_list.append(initial)
    while len(answer_list) != k:

        next = (initial + auxiliar/initial)/2
        answer_list.append(round(next, 2))
        delta = initial - next
        initial = next
        if delta >= 0.0001:
            continue
        else:
            break

    # Generator
    for number in answer_list:
        yield number 

def n_lists(alist, n):
    
    for thing in alist:
        if type(thing[0]) is int:
        
            new = []
            for sublist in alist:

                if len(sublist) <= n:
                    new.append(sublist)

                else:
                    while len(sublist) > n:
                        new.append(sublist[:n])
                        sublist = sublist[n:]
                    new.append(sublist)
            
            return new

        else: # it's a list --> recursive search
            return list(n_lists(thing, n))

def balanced_parenthesis(expression):

    if len(expression) in [0, 1] or expression in [')(', '][']:
        return -1

    else:

        retos = ""
        curvos = ""
        total = ""

        mirror =    {
                        ")" : "(",
                        "(" : ")",
                        "[" : "]",
                        "]" : "[",
                    }

        for char in expression:
            if char == ")" or char == "(":
                curvos = curvos + char
                total = total + char
            elif char == "]" or char == "[":
                retos = retos + char
                total = total + char
            else:
                continue
        
        qdt_retos = len(retos)
        qdt_curvos = len(curvos)

        flag = (qdt_curvos % 2 == 0) and (qdt_retos % 2 == 0)
        if flag:

            for index in range(qdt_curvos // 2):
                flag = flag and (curvos[index] != curvos[-index-1])

            for index in range(qdt_retos // 2):
                flag = flag and (retos[index] != retos[-index-1])

            if flag:

                qtd_total = len(total) // 2
                for index in range(qtd_total):
                    char = total[index]
                    flag = flag and (mirror[char] == total[-index-1])

                if flag:
                    number_of_pairs = ( len(retos) + len(curvos) ) // 2
                    return number_of_pairs

                else:
                    return -1
            else:
                return -1
        else:
            return -1

# Aula de Métodos Estatísticos com Python
# Teórico-Prática 1, com João Mendes Moreira, dia 02-03-2021 @13:30 -> @15:30 
# Modules

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import os

# Styles

plt.style.use('seaborn-whitegrid')
plt.rc('text', usetex=True)
plt.rc('font', family='times')
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
plt.rc('font', size=12)

# Data Mining

def example1 ():
    
    # Manipulating data with python's dictionary
    
    data =  {
        
            'year': [2010, 2011, 2012, 2010, 2011, 2012, 2010, 2011, 2012],
            'team': ['FCBarcelona', 'FCBarcelona', 'FCBarcelona', 'RMadrid', 'RMadrid', 'RMadrid', 'ValenciaCF', 'ValenciaCF', 'ValenciaCF'],
            'wins':   [30, 28, 32, 29, 32, 26, 21, 17, 19],
            'draws':  [6, 7, 4, 5, 4, 7, 8, 10, 8],
            'losses': [2, 3, 2, 4, 2, 5, 9, 11, 11]
            
            }
    
    football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'draws', 'losses'])
    return football


def example2 ():
    
    # Manipulating data with cvs' database
    
    pwd = os.getcwd()
    edu = pd.read_csv(pwd + '/educ_figdp_1_Data.csv', na_values=':', usecols=['TIME', 'GEO', 'Value'])
    
    def read_data(edu):
    
        print (edu)
        print (edu.head())
        print (edu.tail())
        print (edu.columns)
        print (edu.index)
        print (edu.values)
        print (edu.describe())
        
        return None
    
    
    def select_data(edu):
        
        print (edu['Value'])
        print (edu[10:14])
        print (edu.ix[90:94, ['TIME', 'GEO']])
        
        return None
    
    
    def filtering_data(edu):
        
        return edu[edu['Value'] > 6.5].tail()
    
    
    def filtering_miss_value(edu):
        
        return edu[edu['Value'].isnull()].head()
    
    
    def manipulating_data(edu):
        
        print (edu.max(axis=0))
        print ('Pandas max function:', edu['Value'].max())
        
        s = edu['Value'] / 100
        s = edu['Value'].apply(lambda d: d**2)
        print (s.head())
        
        edu['ValueNorm'] = edu['Value'] / edu['Value'].max()
        print (edu.tail())
        
        edu.drop('ValueNorm', axis=1, inplace=True)
        print (edu.head())
        
        edu = edu.append({'TIME': 2000, 'Value': 5.00, 'GEO': 'a'}, ignore_index=True)
        print (edu.tail())
        
        
        edu.drop(max(edu.index), axis=0, inplace=True)
        print (edu.tail())
        
        eduDrop = edu.drop(edu['Value'].isnull(), axis=0)
        print (edu.head())
        
        eduDrop = edu.dropna(how='any', subset=['Value'], axis=0)
        print (edu.head())
        
        eduFilled = edu.fillna(value={'Value': 0})
        print (edu.head())
        
        return None
    
    
    def data_sorting(edu):
        
        edu.sort_values(by='Value', ascending=False, inplace=True)
        print (edu.head())
        
        edu.sort_index(axis=0, ascending=True, inplace=True)
        print (edu.head())

        return None
    
    
    def grouping_data(edu):
        
        group = edu[['GEO', 'Value']].groupby('GEO').mean()
        
        return group.head()
    
    
    def rearranging_data(edu):
        
        filtered_data = edu[edu['TIME'] > 2005]
        pivedu = pd.pivot_table(filtered_data, values='Value', index=['GEO'], columns=['TIME'])
        print (pivedu.head())
        
        return pivedu.ix[['Spain', 'Portugal'], [2006, 2011]]
    
    
    def ranking_data(edu):
        
        pivedu = pivedu.drop(['Euro area (13 countries)',
                              'Euro area (15 countries)',
                              'Euro area (17 countries)',
                              'Euro area (18 countries)',
                              'European Union (25 countries)',
                              'European Union (27 countries)',
                              'European Union (28 countries)'
                              ], axis=0)
        
        pivedu = pivedu.rename(index={'Germany (until 1990 former territory of the FRG)': 'Germany'})
        pivedu = pivedu.dropna()
        pivedu.rank(ascending=False, method='first').head()
        
        totalSum = pivedu.sum(axis=1)
        totalSum.rank(ascending=False, method='dense').sort_values().head()

        return totalSum
    
    
    def plotting_data(edu):
        
        fig = plt.figure(figsize=(12, 5))
        totalSum = pivedu.sum(axis=1).sort_values(ascending=False)
        totalSum.plot(kind='bar', style='b', alpha=0.4, title='Total Values for Country')
        plt.savefig('Totalvalue_Country.png', dpi=300, bbox_inches='tight')
        
        my_colors = ['b', 'r', 'g', 'y', 'm', 'c']
        ax = pivedu.plot(kind='barh', stacked=True, color=my_colors, figsize=(12, 6))
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig('Value_Time_Country.png', dpi=300, bbox_inches='tight')
        
        return None
    
    return some_function

def print_degrees():

    # Exercício de Engenharia Mecânica da Universidade de Coimbra resolvido com Python para um amigo.
    # Ajuda para o Henrique

    from math import pi, cos, sin
    all_angles = [x for x in range(1, 90, 1)]
    all_deslocamentos = []

    v = int(input("Módulo da velocidade? "))

    for angle in all_angles:
        x = angle*pi/180
        a = sin(x)
        b = cos(x)
        r = round((v*v*a*b)/5, 2)
        all_deslocamentos.append(r)

    answer = all_angles[all_deslocamentos.index(max(all_deslocamentos))], max(all_deslocamentos)
    print("O ângulo que permite o maior valor de deslocamento é {} graus".format(answer[0]))
    print("O deslocamento máximo para a velocidade {} m/s e ângulo {} graus é {} metros".format(v, answer[0], answer[1]))

    return None

def decrypt1 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str(abc.find(caracter)))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    for par in message.split(" "):
        try:
            print(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

    print("Total = {}\nPrimeira parte = {}\nSegunda Parte = {}".format(round(total_1 + total_2, 3), round(total_1, 3), round(total_2, 3)))

def decrypt2 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str((abc.find(caracter)+1)%10))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    for par in message.split(" "):
        try:
            print(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

# Part 1 -> Decrypt message using a = 0 until j = 9

def decrypt (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str(abc.find(caracter)))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    numbers = []
    for par in message.split(" "):

        try:
            numbers.append(float(par))
            print(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

    print("Somatório total = {}\nPrimeira parte, antes do '+' = {}\nSegunda Parte, depois do '+' = {}".format(round(total_1 + total_2, 3), round(total_1, 3), round(total_2, 3)))

    return numbers

def get_coordinates ( alist ) :

    from math import floor as rd 
    possibilities = []
    available = []

    for number in alist:
        if (len(str(rd(number))) == 2) and rd(number) < 60:
            if len(str(number)) == 5:
                string = str(number) + "0"
                available.append(string)
            else:
                available.append(str(number))

        else:
            continue
    
    n = "N 41 "
    w = " W 008 "
    combinations = [(x, y) for x in available for y in available]
    for norte, oeste in combinations:
        attemp = n + norte + w + oeste
        possibilities.append(attemp)

    for pos in possibilities:
        print(pos)
    return possibilities

code = "bch.ga dc.ag bia.jeh bf.jjj hc.gda bf.jjj ea.ahi bc.abb b.aai bbe.ibi gj.hcd cg.jib bcg.jae he.jcb + eh.igh fi.jdd"
numbers = decrypt(code)
print(numbers)
print(get_coordinates(numbers))

from string import ascii_uppercase as abc

instructions = "Para Santiago por vezes segue-se o azul e só depois o amarelo. Nas termas recupera-se melhor a cantar."

message1 = "9-13-1-6-21-18-9-19"
message2 = "19-9-13-15-4-1-12-9-19-21-9-19"
message3 = "12-9-18-9-19-1-12-15-4"

def to_letters(numbers, offset):

    astring = ""
    for number in numbers.split("-"):
        astring = astring + str(abc[int(number) - 1 + offset])

    return astring

# A == 1
m1 = to_letters(message1, 1) # JNBGVSJT
m2 = to_letters(message2, 1) # TJNPEBMJTVJT
m3 = to_letters(message3, 1) # MJSJTBMPE

# A == 0
m1 = to_letters(message1, 0) # IMAFURIS
m2 = to_letters(message2, 0) # SIMODALISUIS
m3 = to_letters(message3, 0) # LIRISALOD

def frequency(message):

    dictionary = {}
    for letter in message:
        if letter not in dictionary.keys():
            dictionary[letter] = dictionary.get(letter, 0) + 1
        else:
            dictionary[letter] += 1

    return dictionary

def sum_freqs (rd):

    main_dict = {}
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = 0
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = main_dict[key] + dictionary[key]

    return main_dict

a1 = [int(x) for x in sorted(message1.split("-"), key = lambda x: int(x))]
print(a1, sum(a1))

a2 = [int(x) for x in sorted(message2.split("-"), key = lambda x: int(x))]
print(a2, sum(a2))

a3 = [int(x) for x in sorted(message3.split("-"), key = lambda x: int(x))]
print(a3, sum(a3))

all_messages = [m1, m2, m3]
dicts = []
for message in all_messages:
    print(frequency(message))
    # {'I': 2, 'M': 1, 'A': 1, 'F': 1, 'U': 1, 'R': 1, 'S': 1}
    # {'S': 3, 'I': 3, 'M': 1, 'O': 1, 'D': 1, 'A': 1, 'L': 1, 'U': 1}
    # {'L': 2, 'I': 2, 'R': 1, 'S': 1, 'A': 1, 'O': 1, 'D': 1}
    dicts.append(frequency(message))

print("\nTotal sum: {}".format(sum_freqs(dicts)))
# Total sum: {'I': 7, 'M': 2, 'A': 3, 'F': 1, 'U': 2, 'R': 2, 'S': 5, 'O': 2, 'D': 2, 'L': 3}

all_numbers = [a1, a2, a3]
dicts_numbers = []
for numbers in all_numbers:
    print(frequency(numbers))
    # A == 0
    # {1: 1, 6: 1, 9: 2, 13: 1, 18: 1, 19: 1, 21: 1}
    # {1: 1, 4: 1, 9: 3, 12: 1, 13: 1, 15: 1, 19: 3, 21: 1}
    # {1: 1, 4: 1, 9: 2, 12: 2, 15: 1, 18: 1, 19: 1}

    dicts_numbers.append(frequency(numbers))

print("\nTotal sum: {}".format(sum_freqs(dicts_numbers)))
# Total sum: {1: 3, 6: 1, 9: 7, 13: 2, 18: 2, 19: 5, 21: 2, 4: 2, 12: 3, 15: 2}

def sort_numbers (message):

    solution = ""
    for number in sorted(message.split("-"), key = lambda y: int(y)):
        solution += number + "-"

    return solution[:len(solution)-1]

for message in [message1, message2, message3]:
    print(sort_numbers(message))
    # 1-6-9-9-13-18-19-21
    # 1-4-9-9-9-12-13-15-19-19-19-21
    # 1-4-9-9-12-12-15-18-19

def remove_py_com(txt):

    flag = False    # Indica se está dentro de uma string. No início está falso.
    solution = ""   # Vai acumular os caracteres

    for character in txt:

        if character != '#' and character != '"':   # Se não for nenhum dos dois itens essenciais,
            solution += character                   # Acrescenta à solução.

        if character == '"':
            flag = not flag         # Flag passa a Verdade, ou seja, está dentro de uma string e tudo
            solution += character     # o que está lá dentro vai ser considerado. Quando encontrar um novo '"'
                                    # Passa novamente a falso, ou seja, sai da string.

        if character == '#' and flag:
            solution += character       # Se estiver dentro da string (flag == true), 
                                        # coloca o símbolo '#' na mesma.

        if character == "#" and not flag:
            break                           # Se estiver fora de uma string (flag == false), ignora tudo o que está à frente
                                            # Pára o ciclo e retorna o resultado
    return solution

test1 = 'def f(x): # f function'
test2 = 'x = x + "abc # def" + "cd# +" # + "abc"'

print(remove_py_com(test1)) # Output: 'def f(x): '
print(remove_py_com(test2)) # Output: 'x = x + "abc # def" + "cd# +"'

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

def run ():

    c = []
    for i in range(4, 60):
        comentario = str(input("Next: "))
        if i < 10:
            c.append("[Atualização 15:0{}] : {} ".format(i, comentaSrio))
        else:
            c.append("[Atualização 15:{}] : ".format(i, comentario))
    
    for ci in c:
        print(ci)
        
print(run())

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

from string import ascii_lowercase as abc

def score(word):

    score = 0
    for char in word:
        score = score + int(abc.find(char)+1)
    return score

def high(x):
    
    words = [x for x in x.lower().split(" ")]
    max_word = ""
    max_score = 0

    for word in words:

        max_word = word if score(word) > max_score else max_word
        max_score = score(word) if score(word) > max_score else max_score

    return max_word

print(high('what time are we climbing up the volcano'))

def make_a_window(num): 
    
    begin = (3 + 2 * num) * '-' + '\n'
    end = (3 + 2 * num) * '-'
    middle = '|' + num * '-' + '+' + num * '-' +  '|' + '\n'
    static = '|' + num * '.' + '|' + num * '.' + '|' + '\n'

    return begin + num*static + middle + num*static + end

print(make_a_window(10))

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

def make_sentences(parts):
    
    alist = list([x for x in parts if x != "."]) + ['.']
    sentence = alist[0]

    for word in alist[1:]:  
        if word != '.' and word != ',':
            sentence += " " + word
        else:
            sentence += word
            
    return sentence

sentence = ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.']
print(make_sentences(sentence))

def decipher_message(message):
    
    from math import sqrt
    qtd = int(sqrt(len(message)))
    
    square = []
    line = ""
    for letter in message:
        line += letter
        if len(line) == qtd:

            chars = []
            for char in line:
                chars.append(char)

            line = ""
            square.append(chars)

        else:
            continue

    solution = ""
    counter = 0

    while (counter != qtd):

        for chars in square:
            solution += chars[counter]
        counter = counter + 1
 
    return solution     

print(decipher_message('ArNran u rstm5twob  e ePb'))

def multiplication_table(size):
    return list([list([(x+1)*n for x in range(size)]) for n in [x+1 for x in range(size)]])

def print_table(number):

    alist = multiplication_table(number)
    for line in alist:
        for number in line:
            print("{} ".format(number), end = "")
        print("")

print(print_table(200))

def to_nato(words):
    
    dictionary = {
                    'A' : 'Alfa' ,
                    'B' : 'Bravo' ,
                    'C' : 'Charlie' ,
                    'D' : 'Delta' ,
                    'E' : 'Echo' ,
                    'F' : 'Foxtrot' ,
                    'G' : 'Golf' ,
                    'H' : 'Hotel' ,
                    'I' : 'India' ,
                    'J' : 'Juliett' ,
                    'K' : 'Kilo' ,
                    'L' : 'Lima' ,
                    'M' : 'Mike' ,
                    'N' : 'November' ,
                    'O' : 'Oscar' ,
                    'P' : 'Papa' ,
                    'Q' : 'Quebec' ,
                    'R' : 'Romeo' ,
                    'S' : 'Sierra' ,
                    'T' : 'Tango' ,
                    'U' : 'Uniform' ,
                    'V' : 'Victor' ,
                    'W' : 'Whiskey' ,
                    'X' : 'Xray' ,
                    'Y' : 'Yankee' ,
                    'Z' : 'Zulu' ,
                }
    
    ponctuation = ['.', '?', '!']
    solution = ""

    for char in words:
        if char.upper() in dictionary.keys():
            solution += dictionary[char.upper()] + " "
        elif char in ponctuation:
            solution += char + " "
        else:
            continue
    
    return solution.strip()

def to_binary (number):

    string = ""
    while (number):

        aux = number % 2
        string = str(aux) + string
        number = (number - aux) // 2

    return string

def swap(s,n):

    binary = to_binary(n)
    while (len(binary) < len(s)):
        binary += binary
    
    keys = ""
    key_counter = 0
    for i in range(len(s)):
        if s[i] == " ":
            keys += " "
        else:
            keys += binary[key_counter]
            key_counter += 1

    solution = ""
    for index in range(len(s)):

        letter = s[index]
        if keys[index] == '1':
            letter = letter.swapcase()
        solution += letter

    print(keys)
    print(s)
    print(solution)
    return solution

print(swap('the quick broWn fox leapt over the fence', 11))