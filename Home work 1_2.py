#Заповнити список дійсними числами  введенням з клавіатури. Порахувати суму і добуток елементів списку. Вивести на екран сам список, отримані
#суму і добуток його елементів.
m = int(input("Enter size of list: "))
array = []
print("Enter %d elements: "%m)
for i in range(m):
    array.append(float(input()))
sum = 0
prod = 1
for item in array:
    print("%.2f "%item,end="")
print()
for item in array:
    sum+=item
print("Sum of elements = %.2f"%sum)
for item in array:
    prod*=item
print("Product of elements = %.2f"%prod)