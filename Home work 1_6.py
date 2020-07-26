#У другому списку зберегти індекси парних елементів першого списку. Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, то другий
#треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація починається з нуля), оскільки саме в цих позиціях першого масиву стоять
#парні числа.
import random
size = 10
array = []
print("Our list: ")
for i in range(size):
    array.append(random.randint(1,20))
    print("%3d " %array[i], end ="")
print()
array_of_index = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        array_of_index.append(i+1)
print("Our list of indices of paired elements (starts with 1) : ")
for item in array_of_index:
    print("%3d"%item,end="")
