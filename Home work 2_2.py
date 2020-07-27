#Сформувати матрицю з чисел від 0 до 999, вивести її на екран. Порахувати кількість двозначних чисел в ній.
import random
m = int(input("Input M:"))
n = int(input("Input N:"))
numbers = [[0] * n for i in range (m)]

for i in range(m):
    for j in range(n):
        numbers[i][j] = random.randint(0,999)

for i in range(m):
    for j in range(n):
         print("%4d"%numbers[i][j],end=" ")
    print()
print()
amount = 0
for i in range(m):
    for j in range(n):
        if (numbers[i][j]/10) >=1  and (numbers[i][j]/10) <10:
            amount+=1
print()
print(amount)

