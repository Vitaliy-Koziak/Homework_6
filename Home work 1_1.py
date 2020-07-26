#Заповнити один список випадковими числами, інший - введеними з клавіатури числами, в третій записати суми відповідних елементів перших
#двох. Вивести вміст списків на екран
import random
n = int(input("Enter size of first list: "))
array_1 = []
print("Our first list: ")
for i in range(n):
    array_1.append(random.randint(1,10))
    print("%3d " %array_1[i], end ="")
print()
m = int(input("Enter size of second list: "))
array_2 = []
print("Enter %d elements: "%m)
for i in range(m):
    array_2.append(int(input()))
print("Our second list: ")
for item in array_2:
    print("%3d " %item, end ="")
print()
array_3 = array_1 + array_2
print("Our third list: ")
for item in array_3:
    print("%3d " %item, end ="")