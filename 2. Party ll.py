# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)

# print(list1)

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = []
# for i in range(len(list1)):
#     maximum += [max(list1[i])]
# l = max(maximum)
# print(l)


# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# l = []
# for i in range(len(list1)):
#     l += [(list1[i][::-1])]
# print(l)

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for i in range(len(list1)):
#     total += sum(list1[i])
#     counter += len(list1[i])
# print(total/counter)

# q = 5
# l = []
# for i in range(1, q+1):
#     l.append(i)

# print(*([l]*3), sep = '\n')

# q = int(input())
# l = []
# for i in range(1, q+1):
#     l.append(i)
#     print(*([l]), sep='\n')

# Треугольник Паскаля 1 🌶️

# q = int(input())
# l = []
# for i in range(0, q+1):
#     row = [1]*(i+1)
#     for j in range(i+1):
#         if  j != 0 and j !=i:
#             row[j] = l[i-1][j-1] + l[i-1][j]
    
#     l.append(row)

# for k in l:
#     print(k)
    
