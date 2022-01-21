def time_to_sleep():
    total_minutes = int(input('Введите минуты: '))
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(f'Часы: {hours}.')
    print(f'Минуты: {minutes}.')


time_to_sleep()
