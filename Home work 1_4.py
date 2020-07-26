#Випадкові числа в діапазоні від -5 до 5 розкласти на два списки: в один помістити тільки додатні, у другий - тільки від’ємні. Числа, рівні нулю,
#ігнорувати. Вивести на екран всі згенеровані випадкові числа і елементи обох списків.
import random
size = 20
array = []
print("Our  generated numbers from -5 to 5: ")
for i in range(size):
    array.append(random.randint(-5,5))
    print("%3d " %array[i], end ="")
print()
first_list = []
print("First list: ")
for item in array:
    if item>0:
        first_list.append(item)
for item in first_list:
    print("%3d "%item,end="")
print()
print("Second list: ")
second_list = []
for item in array:
    if item<0:
        second_list.append(item)
for item in second_list:
    print("%3d "%item,end="")
print()