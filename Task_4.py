#1)Заповнити матрицю розмірності MxN і вивести її на екран
import random
m = int(input("Input M:"))
n = int(input("Input M:"))
numbers = [[0] * n for i in range(m)]

for i in range(m):
    for j in range(n):
        numbers[i][j] = random.randint(1,30)

for i in range(m):
    for j in range(n):
         print("%4d"%numbers[i][j],end=" ")
    print()
#2)Знайти мінімальний елемент 3-го рядочка та максимальний елемент 2-го стовпчика і вивести їх на екран
print()
third_row = []
for j in range(n):
     third_row.append(numbers[2][j])
print("Min element of third row is: %d"%min(third_row))
second_colomn = []
for i in range(m):
    second_colomn.append(numbers[i][1])
print("Max element of 2nd colomn is: %d"%max(second_colomn))
#3)Поміняти місцями 2-й та 4-й стовпці матриці. Результат вивести на екран
print()
print("Swaped 2nd and 4th coloums: ")
temp = 0
for i in range(m):
    temp = numbers[i][1]
    numbers[i][1] = numbers[i][3]
    numbers[i][3] = temp
print()
for i in range(m):
    for j in range(n):
         print("%4d"%numbers[i][j],end=" ")
    print()
    #4)Вивести на екран елементи головної діагоналі матриці та їх суму
elements_of_diagonal = []

print()
i = 0
for j in range(n):
    elements_of_diagonal.append(numbers[i][j])
    i+=1
print("Elements of main diagonal: ")
for item in elements_of_diagonal:
    print("%d, " %item, end ="")
sum = 0
for item in elements_of_diagonal:
    sum+=item
print("Their sum = %d"%sum)