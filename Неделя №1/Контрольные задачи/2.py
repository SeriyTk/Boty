number_of_programmers = int(input('Количество программистов: '))
if number_of_programmers == 0 or 5 <= number_of_programmers <= 20 or number_of_programmers == (number_of_programmers // 10) * 10:
    print(f'{number_of_programmers} программистов.')
elif number_of_programmers == 1 or number_of_programmers == ((number_of_programmers // 10) * 10 + 1):
    print(f'{number_of_programmers} программист.')
elif 2 <= number_of_programmers <= 4:
    print(f'{number_of_programmers} программиста.')
