import random

file = open("helo.csv", "w")
file.write("")

array =[]

for i in range(0, 19, 1):
    array.append(random.randint(0, 100))

array.sort()
min = array[0]
array.reverse()
max = array[0]

print(min, max, array)

for i in array:
    file = open("helo.csv", "a")
    file.write(str(i))
    file.write(",")
