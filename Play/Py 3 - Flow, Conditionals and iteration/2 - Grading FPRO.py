# Created on October, 2020
# @author: Fábio Araújo de Sá

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
