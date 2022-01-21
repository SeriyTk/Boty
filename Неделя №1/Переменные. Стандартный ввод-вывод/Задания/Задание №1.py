def time_to_sleep():
    hours = int(input('Сколько часов спите? '))
    minutes = int(input('Сколько минут спите? '))
    hours_to_minutes = hours * 60
    total_minutes = minutes + hours_to_minutes
    print(total_minutes)


time_to_sleep()
