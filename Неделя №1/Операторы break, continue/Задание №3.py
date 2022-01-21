while True:
    number = int(input('Введите число: '))
    if number < 10:
        continue
    elif number > 100:
        break
    print(number)
