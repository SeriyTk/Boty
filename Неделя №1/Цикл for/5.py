def sum_of_odd_numbers(a, b):
    total = 0
    if a % 2 == 0:
        a += 1
    for i in range(a, b + 1, 2):
        total += i
    print(total)


a, b = (int(i) for i in input('Введите числа через пробел: ').split())
sum_of_odd_numbers(a, b)


