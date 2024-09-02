# def print_kub():
#     for i in range(10):
#         if i == 0 or i == 9:
#             print("*" * 10)
#         else:
#             print("*" + " " * 8 + "*")


# def draw_triangle(fill, base):
#     for i in range(1, base+1):
#         if i < (base / 2)+1:
#             print(fill * i)
#         else:
#             print(fill * (base - (i-1)))

# draw_triangle("*", 99)


# def matrix(a = 1, b = None, c = 0):
#     if b == None:
#         b = 1
#     return [[c]*b for _ in range(a)]
# print(matrix(5,6))


# def my_sum(*args):
#     return sum(args)


# print(my_sum(*[1, 2, 3, 4]))
# print(my_sum(1, 2, 3, 4))
# print(my_sum(int('11'),int('22'),int('67')))


# def mean(*args):
#     s = [i for i in args if type(i) in (int, float)]
#     if len(s) == 0:
#         return 0.0
#     return sum(s) / len(s)


# def greet(name, *args):
#     n = "Hello,"
#     name = [name]
#     name.extend(i for i in args)
#     result = n + " " + " and ".join(name)+'!'
#     return result
# print(greet("Timur", "Roman", "Ruslan"))


# def print_products(*args):
#     spisok = []
#     products = [i for i in args if type(i) is (str) and len(i) > 0]
#     if len(products) == 0:
#         print("Нет продуктов")
#     else:
#         for i in range(len(products)):
#             spisok.append(f"{i+1}) {products[i]}")
#     return print(*spisok, sep='\n')
# print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5, True)


# def info_kwargs(**kwargs):
#     result = []
#     arg = sorted(kwargs)
#     for key in range(len(arg)):
#         result.append(f"{arg[key]}: {kwargs[arg[key]]}")

#     return print(*result, sep='\n')


# info_kwargs(first_name="Timur", last_name="Guev", age=28, job="teacher")

# def comparator(number):
#     a = sum(number)/len(number)
#     return a


# numbers = [
#     (10, 10, 10),
#     (30, 45, 56),
#     (81, 39),
#     (1, 2, 3),
#     (12,),
#     (-2, -4, 100),
#     (1, 2, 99),
#     (89, 9, 34),
#     (10, 20, 30, -2),
#     (50, 40, 50),
#     (34, 78, 65),
#     (-5, 90, -1, -5),
#     (1, 2, 3, 4, 5, 6),
#     (-9, 8, 4),
#     (90, 1, -45, -21),
# ]
# print(max(numbers, key=comparator))
# print(min(numbers, key=comparator))


# def point(point):
#     sorted(point[0] ** 2 + point[1] ** 2)
# points = [
#     (-1, 1),
#     (5, 6),
#     (12, 0),
#     (4, 3),
#     (0, 1),
#     (-3, 2),
#     (0, 0),
#     (-1, 3),
#     (2, 0),
#     (3, 0),
#     (-9, 1),
#     (3, 6),
#     (8, 8),
# ]
# print(max(points,key = point))


# def number(number):
#     return min(number)+max(number)

# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
# print(sorted(numbers, key = number))


# def sportsman(athletes):
#     def soterovka(parametrs):
#         for key in range(athletes):
#             if parametrs == 1:
#                 return sorted(key)
#             elif parametrs== 2:
#                 return sorted(key[0])
#             elif parametrs == 3:
#                 return sorted(key[1])
#             elif parametrs == 4:
#                 return sorted(key[2])
#     return soterovka
# athletes = [
#     ("Дима", 10, 130, 35),
#     ("Тимур", 11, 135, 39),
#     ("Руслан", 9, 140, 33),
#     ("Рустам", 10, 128, 30),
#     ("Амир", 16, 170, 70),
#     ("Рома", 16, 188, 100),
#     ("Матвей", 17, 168, 68),
#     ("Петя", 15, 190, 90),
# ]
# parametrs = int(input())
# print(sorted(athletes), key = sportsman)


# from functools import reduce

# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]


# my_list = filter(lambda city: city[1] > 10**7 and city[2] == 'primary', data)
# my_list = map(lambda city: city[0], my_list)
# my_list = sorted(my_list)
# my_list = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', my_list)
# print(my_list)


# is_non_negative_num = lambda x: x.replace('.', '' ,1).isdigit()


# words = [
#     "beverage",
#     "monday",
#     "abroad",
#     "bias",
#     "abuse",
#     "abolish",
#     "abuse",
#     "abuse",
#     "bid",
#     "wednesday",
#     "able",
#     "betray",
#     "accident"]

# sor_func = list(sorted(filter(lambda x: len(x) ==6 , words)))
# print(*sor_func)


# numbers = [
#     46,
#     61,
#     34,
#     17,
#     56,
#     26,
#     93,
# ]

# sor_func = list(filter(lambda x: not (x > 47 and x % 2 != 0) , numbers))
# map_func = map(lambda y: y // 2 if y%2==0 else y, sor_func)
# print(*map_func)

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]


# sor_fanc = sorted(filter(lambda x: x[1][-1], data))
# print(*map(lambda x: f'{x[1]}: {x[0]}', sor_fanc), sep='\n')

# countries = ['Russia']
# capitals = ['Moscow']
# population = [145_934_462]

# my_leg = zip(capitals,countries,population)
# for x, y, z in my_leg:
#     print(f'{x} is the capital of {y}, population equal {z} people.')


# def generate_letter(mail, name, date, time, place, teacher ='Тимур Гуев', number = 17):
#     str = f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}.
# Экзамен будет проводить {teacher} в кабинете {number}.
# Желаем удачи на экзамене!'''
#     return str


# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))


# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])


# def concat(*args, sep = ' '):
#     return sep.join([str(i) for i in args])


# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

# #Версия №1
# from functools import reduce

# def fil_num(num):
#     return num % 2 == 1

# def abb(x, y):
#     return x*y

# def product_of_odds(data1):
#     return reduce(abb , filter(fil_num, data1), 1)

# #Версия № 2 
# from functools import reduce

# def product_of_odds(data):
#     return reduce(lambda x, y: x*y, filter(lambda x: x % 2 == 1, data), 1)


# words = 'the world is mine take a look what you have started'.split()

# print(*map(lambda x: f'"{x}"', words))

# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda num: not str(num) == str(num[::-1]), numbers))


# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

# sorted_numbers = sorted(numbers, key=lambda x: sum(x), reverse=True)

# print(sorted_numbers)




# def genatria(word):
#     return sum(map(lambda x: ord(x.upper()) - ord('A'), word)) ,word

# words = [input() for _ in range(int(input()))]

# print(*sorted(words, key= genatria))


