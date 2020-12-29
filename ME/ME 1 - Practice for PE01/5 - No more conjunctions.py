# Created on November, 2020
# @author: Fábio Araújo de Sá

a = int(input())
b = int(input())
count = 0
for i in range(a, b):
    if ((i % 105 == 0) + (i % 77 == 0) > 0 ) + (( i+a > b) + (i % 2 != 1) > 1) > 0:
        count += 1
    else:
        count -= 1
print(count)
