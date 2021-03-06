# Словарь - это объект-контейнер, который хранит коллекцию данных. Каждый элемент в словаре имеет две части: ключ и
# значение. Ключ используется, чтобы установить местонахождение конкретного значения.
# Структура данных, позволяющая  идентифицировать ее элементы не по числовому индексу, а по произвольному, называется словарем или ассоциативным
# массивом. Соответствующая структура данных в языке Питон называется dict.
# имя_ словаря [ключ]   - чтобы получить значение из словаря
Capitals = dict()

Capitals['Россия'] = 'Москва'
Capitals['Украина'] = 'Киев'
Capitals['США'] = 'Вашингтон'

Countries = ['Россия', 'Франция', 'США', 'Украина']

for country in Countries:
    if country in Capitals:
        print(f'Столица {country}: {Capitals[country]}.')


print(Capitals)
