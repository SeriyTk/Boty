students = ['Саша', 'Гриша', 'Маша']
for student in students:
    print(f'Привет {student}!')
print('---------------------------------')
for student in range(len(students)):
    print(f'Прощай {students[student]}.')
print("-------------------------------------------")
students[1] = 'Вася'
print(students)
print('--------------------------------------------')
students += 'Вова'
print(students)
students += ['Вова']
print(students)
students1 = []
students1 += students
print(students1)