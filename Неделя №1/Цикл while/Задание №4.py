a = int(input('Количество людей в команде №1: '))
b = int(input('Количество людей в команде №2: '))
d = a
while d % b != 0:
    d += a
print(d)
