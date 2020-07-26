#Заповнити список випадковими додатними і від’ємними цілими числами. Вивести його на екран. Видалити з списку всі від’ємні елементи і знову
#вивести.
import random
size = 20
array = []
print("Our list: ")
for i in range(size):
    array.append(random.randint(-15,10))
    print("%4d " %array[i], end ="")
print()
print("Our list without negetive numbers: ")
i=0

while i < len(array):
    if array[i] < 0:
        array.pop(i)
    else:
        i+=1
for i in range(len(array)):
    print("%4d " %array[i], end ="")
print()