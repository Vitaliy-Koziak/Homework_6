#Знайти максимальний елемент серед мінімальних елементів стовпців матриці.
import random
m = int(input("Input M:"))
n = int(input("Input N:"))
numbers = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        numbers[i][j] = random.randint(1,30)

for i in range(m):
    for j in range(n):
         print("%4d"%numbers[i][j],end=" ")
    print()
array_of_min = []
t = 0
p = 0
min = numbers[t][p]

for j in range(n):
    for i in range(m):
        if numbers[i][j]< min:
            min = numbers[i][j]
        if i == m-1 and j < n:
            array_of_min.append(min)
            min = numbers[p+1][t+1]
print()
for item in array_of_min:
    print("%4d "%item,end="")
print()
print()
print(" The maximum element among the minimum elements of the matrix columns is: %d"%max(array_of_min))