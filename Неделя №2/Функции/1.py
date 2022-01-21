def min2(a, b):
    if a <= b:
        return a
    else:
        return b
    
m = min2(42,30)
print(m)
m1 = min2(min2(42,30),25)
print(m1)