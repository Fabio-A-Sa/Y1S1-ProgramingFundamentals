# Created on October, 2020
# @author: Fábio Araújo de Sá

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
