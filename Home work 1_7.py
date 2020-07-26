#У списку знайти елементи, які в ньому зустрічаються тільки один раз, і вивести їх на екран.
import random
size = 20
numbers = []
print("Our list: ")
for i in range(size):
    numbers.append(random.randint(1,15))
    print("%3d, " %numbers[i], end ="")
print()
print("Unique elements: ")
for item in numbers:
    if numbers.count(item)==1:
        print (item)