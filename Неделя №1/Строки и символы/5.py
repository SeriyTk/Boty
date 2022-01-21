genom = 'ATGG'
for i in genom:
    print(i)
print()
genom1 = input('')
cnt = 0
for j in genom1:
    if j == 'C':
        cnt += 1
print(cnt)
print(genom1.count('A'))
