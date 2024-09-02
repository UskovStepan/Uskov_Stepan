# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# list1 = []
# total = 0
# new_number = list(numbers)
# for i in range(len(numbers)):
#     for j in range(len(numbers[i])):
#         total += new_number[i][j]
#     total = total/len(numbers[i])
#     list1.append(total)
#     total = 0
# print(list(list1))

# a, b, c = int(input()), int(input()), int(input())
# cor = []
# x = (-1)*(b/(2*a))
# y = (4*a*c-b**2)/(4*a)
# cor.append(x)
# cor.append(y)
# cor_up = tuple(cor)
# print(cor_up)

# n = int(input())
# list1 = [1 for i in range(n)]
# if n>3:
#     for i in range(3, n):
#         print(i)
#         list1[i] = list1[i-3]+list1[i-2]+list1[i-1]
# print(*list1)

# n, m, k, x, y, z, t, a = (int(input()) for _ in range(8))
# s1 = n+m-x-t
# s2 = m+k-y-t
# s3 = n+k-z-t
# s = (n-s1-s3-t) + (m-s1-s2-t) + (k -s2-s3-t)
# print(s)
# print(s1+s2+s3)
# print(a-s-s1-s2-s3-t)


# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
# sortfruits = sorted(fruits, reverse=True)
# print(*sortfruits, sep = '\n')

# Все 10 цифр
# num1 = input()
# num2 = input()
# num3 = set(num1 + num2)
# if len(num3) == 10:
#     print('YES')
# else:
#     print('NO')

# Одинаковые наборы
# num1 = input()
# num2 = input()
# if sorted(set(num1)) == sorted(set(num2)):
#     print('YES')
# else:
#     print('NO')

# Три слова
# treeword = input().split()
# answer = 'YES'
# for i in range(1, len(treeword)):
#     if set(treeword[i-1]) != set(treeword[i]):
#         answer = 'NO'
#         break
# print(answer)

# myset = set()
# for i in range(10):
#     if i % 2 == 0:
#         myset.add('even')
#     else:
#         myset.add('odd')
# print(len(myset))

# Уникальные символы 1
# num = int(input())
# for _ in range(num):
#     print(len(set(input().lower())))


# Уникальные символы 2
# num = int(input())
# m = set()
# for _ in range(num):
#     for i in input().lower():
#         m.add(i)
# print(len(m))


# Количество слов в тексте
# s = input().lower().split()
# for i in range(len(s)):
#     s[i] = s[i].strip('.,;:-?!')

# set_word = set(s)

# print(len(set_word))

# Встречалось ли число раньше?
# numbers = [int(i) for i in input().split()]
# my_set = set()

# for i in range(len(numbers)):
#     if numbers[i] in my_set:
#         print('YES')
#     else:
#         print('NO')
#         my_set.add(numbers[i])

# Счетчик верных решений

# complete = set()
# n = int(input())
# correct = 0

# for _ in range(n):
#     result = input().split(': ')

#     if result[1] == 'Correct':
#         correct += 1
#         complete.add(result[0])

# if correct:
#     print(f'Верно решили {len(complete)} учащихся')
#     print(f'Из всех попыток {round(((correct / n)* 100) + 0.001)}% верных')
# else:
#     print('Вы можете стать первым, кто решит эту задачу')

# Количество совпадающих
# my_set1 = input().split()
# my_set2 = input().split()
# my_set3 = (set(my_set1) & set(my_set2))
# print(len(my_set3))

# Общие числа
# set1 = set(int(i) for i in input().split())
# set2 = set(int(i) for i in input().split())
# print(*sorted(set1&set2))

# Числа первой строки
# str1 = set(int(i) for i in input().split())
# str2 = set(int(i) for i in input().split())
# print(*sorted(str1-str2))

# Общие цифры
# n = int(input())
# odject1 = set()
# for i in range(n+1):
#     odject1.add(set(int(i) for i in input().split()))
# print(odject1)

# Общие цифры
# n = int(input())
# ob = set()
# ob1 = set()
# for _ in range(1):
#     num = int(input())
#     while num>0:
#         ob.add(num%10)
#         num = num//10
#     for _ in range(n-1):
#         num = int(input())
#         while num>0:
#             ob1.add(num%10)
#             num = num//10
#         ob.intersection_update(ob1)
#         ob1.clear()
# print(*sorted(ob))

# #Одинаковые цифры
# num1 = set(int(i) for i in input().split())
# num2 = set(int(i) for i in input().split())
# num3 = set(int(i) for i in input().split())
# print(*sorted((num1&num2)-num3, reverse=True))

# #Урок математики

# student1 = set(int(i) for i in input().split())
# student2 = set(int(i) for i in input().split())
# student3 = set(int(i) for i in input().split())

# print(*sorted((student1 | student2 | student3)-(student1&student2&student3)))


# #Урок физики
# num1 = set(int(i) for i in input().split())
# num2 = set(int(i) for i in input().split())
# num3 = set(int(i) for i in input().split())
# print(*sorted((num3 - num1 - num2), reverse=True))

# #Урок биологии
# num1 = set(int(i) for i in input().split())
# num2 = set(int(i) for i in input().split())
# num3 = set(int(i) for i in input().split())
# num4 = set(int(i) for i in range(11))
# print(*sorted((num3 - num1 - num2)))

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
# num1 = set(int(i) for i in items)
# print(*sorted(num1))

# words = [
#     "Plum",
#     "Grapefruit",
#     "apple",
#     "orange",
#     "pomegranate",
#     "Cranberry",
#     "lime",
#     "Lemon",
#     "grapes",
#     "persimmon",
#     "tangerine",
#     "Watermelon",
#     "currant",
#     "Almond",
# ]
# words1 = set()
# for i in range(len(words)):
#     words1.add(words[i].lower())
# print(*sorted(set((i[0]) for i in words1)))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# num = {i.lower().strip(':,.?!();') for i in sentence.split()}
# print(*sorted(num))

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# num = {i.lower().strip(':,.?!();') for i in sentence.split() if len(i.strip(':,.?!();')) < 4}
# print(*sorted(num))


# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# my_set = {i.lower() for i in files if i.lower().endswith('png')}
# print(*sorted(my_set))


# Словари
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# spisok_suk = []
# for i in users:
#     if i['phone'][-1] == '8':
#         spisok_suk.append(i['name'])
# print(*sorted(spisok_suk))


# spisok_suk = []
# for i in users:
#     if 'email' not in i or i['email'] == '':
#         spisok_suk.append(i['name'])
# print(*sorted(spisok_suk))

# num = int(input())
# num_list = []
# my_list = []

# figure = {
#     0: 'zero',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
# }
# while num != 0:
#     num_list.append(num % 10)
#     num //= 10

# for i in num_list:
#     my_list.append(figure[i])
# print(*my_list[::-1])

# num = input()
# inf_stydu = {
#     "CS101": ["3004", "Хайнс", "8:00"],
#     "CS102": ["4501", "Альвардо", "9:00"],
#     "CS103": ["6755", "Рич", "10:00"],
#     "NT110": ["1244", "Бэрк", "11:00"],
#     "CM241": ["1411", "Ли", "13:00"],
# }
# if num in inf_stydu:
#     my_list = inf_stydu[num]
# print(f'{num}:', *inf_stydu[num], sep=', ')


# num = input()
# inf_stydu = {
#     "CS101": "3004, Хайнс, 8:00",
#     "CS102": "4501, Альварадо, 9:00",
#     "CS103": "6755, Рич, 10:00",
#     "NT110": "1244, Берк, 11:00",
#     "CM241": "1411, Ли, 13:00",
# }
# print(f"{num}: {inf_stydu[num]}")



# d = {
#     ".": "1",
#     ",": "11",
#     "?": "111",
#     "!": "1111",
#     ":": "11111",
#     "A": "2",
#     "B": "22",
#     "C": "222",
#     "D": "3",
#     "E": "33",
#     "F": "333",
#     "G": "4",
#     "H": "44",
#     "I": "444",
#     "J": "5",
#     "K": "55",
#     "L": "555",
#     "M": "6",
#     "N": "66",
#     "O": "666",
#     "P": "7",
#     "Q": "77",
#     "R": "777",
#     "S": "7777",
#     "T": "8",
#     "U": "88",
#     "V": "888",
#     "W": "9",
#     "X": "99",
#     "Y": "999",
#     "Z": "9999",
#     " ": "0",
# }


# text = input().upper().replace('"', "")
# my_list = []
# for i in range(len(text)):
#     for j in range(len(text[i])):
#         if text[i][j] in d:
#             my_list.append(d[text[i][j]])
# print(*my_list)


# morze = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
# }

# text = input().upper().replace('"', "")
# my_list = []
# for i in range(len(text)):
#     for j in range(len(text[i])):
#         if text[i][j] in morze:
#             my_list.append(morze[text[i][j]])
# print(*my_list, sep = ' ')


# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4]
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1
# print(result)

# n = int(input())

# for i in range(n):
#     for j in range(n):
#         print(min(i + 1, j + 1, n - i, n - j), end=' ')
#     print()

numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]

result = {key: numbers[key]**2 for key in range(len(numbers))}
print(result)