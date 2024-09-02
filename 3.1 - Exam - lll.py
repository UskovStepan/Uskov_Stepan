# Каждый n-ый элемент
# x = input().split()
# n = int(input())
# s = [[]*n for _ in range(n)]
# for i in range(n):
#     for q in range(i, len(x), n):
#         s[i].append(n[q])
# print(s)

#Максимальный в области 2
n = int(input())
matrix = []
for k in range(n):
    tmp = [int(x) for x in input().split()]
    matrix.append(tmp)

# Max = matrix[0][0]

# for i in range(n):
#     for q in range(n):
#         if i >= n - 1 - q and matrix[i][q] > Max:
#             Max = matrix[i][q]

# Транспонирование матрицы
# n = int(input())
# matrix = []
# for i in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)

# for q in range(n):
#     for i in range(n):
#         print(matrix[i][q], end = ' ')
#     print()

# Снежинка
# n = int(input())
# matrix = []
# for _ in range(n):
#     tmp = ['.' for e in range(n)]
#     matrix.append(tmp)

# for i in range(n):
#     for q in range(n):
#         if i == q or i == n - 1 - q:
#             matrix[i][q] = '*'
#         elif n // 2 == i or n // 2 == q:
#             matrix[i][q] = '*'

# for i in range(n):
#     print(*matrix[i])


# Симметричная матрица
# n = int(input())
# matrix = []
# flag = True
# for _ in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
# matrix.reverse()

# for i in range(n):
#     for q in range(n):
#         if matrix[i][q] != matrix[q][i]:
#             flag = False
#             break
# if flag:
#     print('YES')
# else:
#     print('NO')

# Латинский квадрат 🌶️
# n = int(input())
# matrix = []
# flag = True
# for _ in range(n):
#     tmp = [int(x) for x in input().split()]
#     matrix.append(tmp)
# latin_list = [i for i in range(1, n+1)]

# for i in range(n):
#     x = sorted(matrix[i])
#     y = sorted([matrix[q][i] for q in range(n)])
#     if x != latin_list or y != latin_list:
#         flag = False
#         break

# if flag:
#     print('YES')
# else:
#     print('NO')


# Ходы ферзя
# x, y = input()
# n = 8
# matrix = [["."] * n for _ in range(n)]
# y = n - int(y)
# x = ord(x) - 97

# for i in range(n):
#     for q in range(n):
#         if i == y or q == x:
#             matrix[i][q] = "*"
#         elif (i + q == y + x) or (i - q == y - x):
#             matrix[i][q] = "*"
# matrix[y][x] = "Q"
# for x in range(n):
#     print(*matrix[x])

# Диагонали, параллельные главной
# n = int(input())
# matrix = []
# for _ in range(n):
#     tmp = [0 for e in range(n)]
#     matrix.append(tmp)
    
# for i in range(n):
#     for q in range(n):
#         if q > i:
#             matrix[i][q] = q - i
#         if i > q:
#             matrix[i][q] = i - q
            
# for i in range(n):
#     print(*matrix[i])

