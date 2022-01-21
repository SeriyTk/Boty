a, b, c= input(': ').split()
a = float(a)
b = float(b)
if b == 0:
    print('Делить на ноль нельзя.')
else:
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        print(a / b)
    elif c == '//':
        print(a // b)
    elif c == '*':
        print(a * b)
    elif c == '%':
        print(a % b)

