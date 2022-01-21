lst = [5, 8, 2, 7, 8, 8, 2, 4]
x = int(input('Введите число: '))
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
