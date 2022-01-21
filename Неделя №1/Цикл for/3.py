def sum_of_odd_numbers(a, b):
    total = 0
    a = int(a)
    b = int(b)
    for i in range(a, b + 1):
        if i % 2 == 1:
            total += i
    print(total)


a, b = input('Введите числа через пробел: ').split()
sum_of_odd_numbers(a, b)


