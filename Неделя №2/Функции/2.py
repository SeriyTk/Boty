def minimum(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
        return m


def my_range(start, stop, step):
    result = []
    if step > 0:
        x = start
        while x < stop:
            result += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            result += [x]
            x += step
    return result


print(my_range(2, 5, 1))
print(my_range(2, 15, 3))
