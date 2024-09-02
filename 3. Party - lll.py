# n, m = int(input()), int(input())
# l = []
# for i in range(n):
#     t = []
#     for j in range(m):
#         t.append(input())
#     l.append(t)
# for i in range(n):
#     for j in range(m):
#         print(l[i][j], end=' ')
#     print()

# n, m = int(input()), int(input())
# l = []
# for i in range(n):
#     t = []
#     for j in range(m):
#         t.append(input())
#     l.append(t)
# for i in range(n):
#     for j in range(m):
#         print(l[i][j], end=' ')
#     print()
# print()
# for i in range(m):
#     for j in range(n):
#         print(l[j][i], end = ' ')
#     print()

# n = int(input())
# l = []
# total = 0
# count = 0
# for i in range(0, n):
#     l.append(input().split())
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             count = int(l[i][j])
#             total += count
# print(total)


# n = int(input())
# l = []
# for i in range(0, n):
#     l.append(input().split())

# for i in range(n):
#     Sum = 0
#     count = 0
#     for j in range(n):
#         Sum += l[i][j]
#     for r in range(n):
#         if l[i][r] > Sum / n:
#             count += 1
#     print(count)

# Максимальный в области 1
# n = int(input())
# l = []
# for i in range(0, n):
#     l.append(input().split())
#     max = int(l[0][0])
# for i in range(n):
#     for j in range(n):
#         if int(l[i][j])> max:
#             max = int(l[i][j])
#         if [i] == [j]:
#             break
# print(max)


# Максимальный в области 2 🌶️
# n = int(input())
# l = []
# for i in range(0, n):
#     l.append(input().split())
#     max = int(l[0][0])
# for i in range(n):
#     for j in range(n):
#         if i<j and i<n-1-j:
#             break
#         if i>j and i>n-1-j:
#             break
#         if int(l[i][j])> max:
#             max = int(l[i][j])

# print(max)


# Суммы четвертей
# n = int(input())
# s1 = s2 = s3 = s4 = 0
# l = []
# for i in range(0, n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# for i in range(n):
#     l[i][i] = 0
#     l[i][n - i - 1] = 0
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j:
#             s1 += l[i][j]
#         elif i < j and i > n - 1 - j:
#             s2 += l[i][j]
#         elif i > j and i > n - 1 - j:
#             s3 += l[i][j]
#         elif i > j and i < n - 1 - j:
#             s4 += l[i][j]
# print("Верхняя четверть:", s1)
# print("Правая четверть:", s2)
# print("Нижняя четверть:", s3)
# print("Левая четверть:", s4)


# n, m = int(input()), int(input())
# for i in range(n):
#     mult = []
#     for j in range(m):
#         mult.append(str(i*j).ljust(3))
#     print(*mult)

# n, m = int(input()), int(input())
# l = []
# for i in range(n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# p = l[0][0]
# for i in range(len(n)):
#     for j in range(len(m)):
#         if l[i][j] > p:
#             p = l[i][j]


# Обмен столбцов
# n, m = int(input()), int(input())
# l = []
# for i in range(n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# x, y =[int(i) for i in input().split()]
# for j in range(n):
#     l[j][x], l[j][y] = l[j][y], l[j][x]
# for q in range(n):
#     print(*l[q])


# Симметричная матрица
# n = int(input())
# count = 0
# l = []
# for i in range(n):
#     x =[int(i) for i in input().split()]
#     l.append(x)
# for i in range(n):
#     l[i][i] = 0

# for i in range(n):
#     for j in range(i):
#         if l[i][j] == l[j][i]:
#             count += 1
#         elif i == j:
#             continue

# if n == 2 and count == 1:
#     print('YES')
# elif n == 3 and count == 3:
#     print('YES')
# elif n == 4 and count == 6:
#     print('YES')
# elif n == 5 and count == 10:
#     print('YES')
# else:
#     print('NO')

# Обмен диагоналей
# n = int(input())
# l = []
# for i in range(n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# for i in range(n):
#     for j in range(i):
#         if i == j:
#             l[i][j], l[i][n-j] = l[i][n-j], l[i][j]
# print(l)


# from math import*
# n = int(input())
# l = []
# q = 0
# for i in range(n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# if n % 2 == 0:
#     p = int(n/2)
#     for i in range(0, p):
#         for j in range(0, n):
#             l[i][j], l[n-1-i][j] = l[n-1-i][j], l[i][j]
#     for i in range(n):
#         print(*l[i])
# if n % 2 != 0:
#     p = ceil(int(n/2))
#     for i in range(0, p):
#         for j in range(0, n):
#             l[i][j], l[n-1-i][j] = l[n-1-i][j], l[i][j]
#     for i in range(n):
#         print(*l[i])


# Поворот матрицы
# n = int(input())
# l = []
# for i in range(n):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# for i in range(n):
#     for j in range(n-1,-1,-1):
#         print(l[j][i], end = ' ')
#     print()


# Ходы коня
# x,y = input()
# n = 8
# l = [['.']* n for _ in range(n)]
# y = n - int(y)
# x = ord(x)- 97
# l[y][x] = 'N'

# for i in range(n):
#     for j in range(n):
#         if abs(i-y) * abs(j - x) == 2:
#             l[i][j] = '*'

# for x in range(n):
#     print(*l[x])


# Магический квадрат 🌶️
# q = int(input())
# l = []
# for _ in range(q):
#     x = [int(i) for i in input().split()]
#     l.append(x)
# digits = [i for i in range(1, q**2+1)]
# d1, d2 = 0, 0
# for i in range(q):
#     s1_sum, s2_sum = 0, 0
#     for j in range(q):
#         s1_sum += l[j][i]
#         s2_sum += l[i][j]
#         if l[i][j] in digits:
#             digits.remove(l[i][j])
#     d1 += l[i][i]
#     d2 += l[i][q-1-i]
#     if s1_sum != s2_sum:
#         break
# if s1_sum == s2_sum == d1 == d2 and digits == []:
#     print('YES')
# else:
#     print('NO')


# Шахмотная доска
# x = input().split()
# l = []
# q, n = int(x[0]), int(x[1])
# for i in range(int(q)):
#     tmp = [i for i in range(n)]
#     l.append(tmp)
# for i in range(int(q)):
#     for j in range(int(n)):
#         if (i+j)%2 == 0:
#             l[i][j] = '.'
#         else:
#             l[i][j] = '*'
# for i in range(q):
#     print(*l[i])


# Побочная диагональ
# q = int(input())
# l = []
# for i in range(q):
#     x = [2 for i in range(q)]
#     l.append(x)
# for i in range(q):
#     for j in range(q):
#         if i+j<q and i ==j:
#             l[i][j] = 0
#         if i < j and i < q - 1 - j:
#             l[i][j] = 0
#         elif i > j and i < q - 1 - j:
#             l[i][j] = 0

# for j in range(q):
#         l[j][q-j-1] = 1
# for i in range(q):
#     print(*l[i])


# Заполнение 1
# n = input().split()
# x, y  = int(n[0]), int(n[1])
# l = []
# for i in range(x):
#     tmp = [i for i in range(y)]
#     l.append(tmp)
# count = 1
# for i in range(x):
#     for j in range(y):
#         l[i][j] = count
#         count += 1
# for i in range(x):
#     for j in range(y):
#         print(str(l[i][j]).ljust(3), end = ' ')
#     print()


# Заполнение 2
# n = input().split()
# x, y  = int(n[0]), int(n[1])
# l = []
# for i in range(x):
#     tmp = [int(0) for i in range(y)]
#     l.append(tmp)

# count = 1
# for i in range(y):
#     for j in range(x):
#         l[j][i] += count
#         count += 1

# for i in range(x):
#     print(*l[i])


# Заполнение 3
# n = int(input())
# l = []
# for i in range(n):
#     w = [int(0) for i in range(n)]
#     l.append(w)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             l[i][j] = 1
#         elif i+j+1 == n:
#             l[i][j] = 1
# for i in range(n):
#     print(*l[i])


# Заполнение 4
# n = int(input())
# l = []
# for i in range(n):
#     x = [int(0) for i in range(n)]
#     l.append(x)
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             l[i][j] = 1
#         elif n == i+j+1:
#             l[i][j] = 1
#         elif i<j and i < n-1-j:
#             l[i][j] = 1
#         elif i>j and i > n-1-j:
#             l[i][j] = 1

# for i in range(n):
#     print(*l[i])


# Заполнение 5🌶️
# q = input().split()
# n, m = int(q[0]), int(q[1])
# x = [i for i in range(1, m + 1)]
# l = []

# for i in range(n):
#     l.append(x)
#     x = x[1:]+[x[0]]


# for i in range(n):
#     for j in range(m):
#         print(str(l[i][j]).ljust(3), end = ' ')
#     print()


# Заполнение змейкой
# q = input().split()
# n, m = int(q[0]), int(q[1])
# l = []
# for i in range(n):
#     x = [int(0) for i in range(1, m + 1)]
#     l.append(x)
# num = 1
# for i in range(n):
#     for j in range(m):
#         l[i][j] = num
#         num += 1
#     if i%2!=0:
#         l[i][:] = l[i][::-1]
# for i in range(n):
#     for j in range(m):
#         print(str(l[i][j]).ljust(3), end = ' ')
#     print()

#Заполнение диагоналями 🌶️
# q = input().split()
# n, m = int(q[0]), int(q[1])
# l = []
# for i in range(n):
#     x = [i for i in range(m)]
#     l.append(x)
# count = 1
# for k in range(n*m):
#     for i in range(n):
#         for j in range(m):
#             if i+j == k:
#                 l[i][j] = count
#                 count += 1

# for i in range(n):
#     for j in range(m):
#         print(str(l[i][j]).ljust(3), end = ' ')
#     print()


#Заполнение спиралью 😈😈
# q = input().split()
# n, m = int(q[0]), int(q[1])
# matrix = []
# for i in range(n):
#     x = [0 for i in range(m)]
#     matrix.append(x)
# x, y = 0, 0
# d_x, d_y = 0, 1
# matrix[0][0] = 1
# count = 2
# while count <= n * m:
#     if  0 <= x + d_x <= n - 1 and 0<=y+d_y<= m - 1 and matrix[x+d_x][y+d_y] == 0:
#         matrix[x+d_x][y+d_y] = count
#         count += 1
#         x += d_x
#         y += d_y
#     else:
#         if d_y == 1:
#             d_y = 0
#             d_x = 1
#         elif d_x == 1:
#             d_x = 0
#             d_y = -1
#         elif d_y == -1:
#             d_y = 0
#             d_x =-1
#         elif d_x == -1:
#             d_x = 0
#             d_y = 1              
# for i in range(n):
#     for q in range(m):
#         print(str(matrix[i][q]).ljust(3), end = ' ')
#     print()



# Сложение матриц
# q = input().split()
# n, m = int(q[0]), int(q[1])
# l = []
# l1 = []
# c = []
# l = [[int(i) for i in input().split()] for _ in range(n)]
# z = input()
# l1 = [[int(i) for i in input().split()] for _ in range(n)]
# c = [[int(i) for i in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         c[i][j] = l[i][j] + l1[i][j]
# for i in range(n):
#     print(*c[i])


#Умножение матриц 🌶️
# n, m = [int(i) for i in input().split()]
# matrix1 = [[int(i) for i in input().split()] for j in range(n)]
# input()
# n2, m2 = [int(i) for i in input().split()]
# matrix2 = [[int(i) for i in input().split()] for j in range(n2)]
# matrix3 = [[0]*m2 for _ in range(n)]
# for i in range(n):
#     for j in range(m2):
#         for k in range(m):
#             matrix3[i][j] += matrix1[i][k]* matrix2[k][j]
# for i in matrix3:
#     print(*i)
    
    
    
#Возведение матрицы в степень 🌶️
# n = int(input())

# matrix1 = [[int(i) for i in input().split()] for j in range(n)]
# matrix2 = matrix1
# x = int(input())
# for _ in range(x-1):
#     matrix3 = [[0]*n for j in range(n)] 
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 matrix3[i][j] += matrix1[i][k]* matrix2[k][j]
#     matrix1 = matrix3
    
    
# for i in matrix3:
#     print(*i)