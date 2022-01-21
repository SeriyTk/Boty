a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a[0][2])
print(a[2][2])
print('-----------------------------')
n = 3
b = [[0] * n for i in range(n)]
print(b)
c = [[1 for j in range(n)] for i in range(n)]
print(c)
