# Created on October, 2020
# @author: Fábio Araújo de Sá

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
