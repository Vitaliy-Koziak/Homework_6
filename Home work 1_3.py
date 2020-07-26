#Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4, записати їх в список. Порахувати кількість додатних, від’ємних і нульових
#елементів. Вивести на екран елементи списку і пораховані кількості.
import random
size = 20
array = []
print("Our  list: ")
for i in range(size):
    array.append(random.randint(-5,4))
    print("%3d " %array[i], end ="")
print()
positive = 0
negetive = 0
zero = 0
for item in array:
    if item > 0 :
        positive += 1
    elif item < 0 :
        negetive += 1
    else:
        zero+=1
print("Positive: %d\nNegetive: %d\nzeros: %d"%(positive,negetive,zero))