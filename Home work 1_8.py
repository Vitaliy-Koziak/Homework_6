#У списку випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.
import random
n = int(input("Input N "))
numbers = []
print("Our list: ")
for i in range(n):
    numbers.append(random.randint(1,10))
    print("%2d " %numbers[i], end ="")

print()
print("Our new list: ")
id_min_elem = numbers.index(min(numbers))
id_max_elem = numbers.index(max(numbers))

temp = numbers[id_min_elem]
numbers[id_min_elem] = numbers[id_max_elem]
numbers[id_max_elem] = temp

for item in numbers:
    print("%2d " %item, end ="")
print()