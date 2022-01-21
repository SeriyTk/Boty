def sum_of_odd_numbers(a, b):
    total = 0
    a = int(a)
    b = int(b)
    if a % 2 == 0:
        a += 1
    for i in range(a, b + 1, 2):
        total += i
    print(total)


a, b = input('Введите числа через пробел: ').split()
sum_of_odd_numbers(a, b)


