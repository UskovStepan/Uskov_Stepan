# class Point:
#     min_coords = 0
#     max_coords = 100


#     def __init__(self, x = 0, y = 0):
#         self.__x = self.__y = 0
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y

#     @classmethod
#     def __check_value(cls, x):
#         return type(x) in (int, float)


#     def set_coords(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError('Координаты должны быть числами')
#     def get_coords(self):
#         return self.__x, self.__y


# pt = Point()
# pt.set_coords(10, 20)
# print(dir(pt))


# class Person:
#     def __init__(self, name, old) -> None:
#         self.__name = name
#         self.__old = old
#     @property
#     def old(self):
#         return self.__old
#     @old.setter
#     def old(self, old):
#         self.__old = old


#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name
#     name = property(get_name, set_name)

# p = Person('Степан', 20)
# p.old = 27
# p.old2 = 25
# p.name = 'Ivan'
# print(p.name, p.old, p.__dict__)

from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО ведено не верно. ФИО должно быть одной трокой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("ФИО ведено не верно. Либо введено не полностью")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for i in f:
            if len(i) < 1:
                raise TypeError("В ФИО должен быть хотябы один символ")
            if len(i.strip(letters)) != 0:
                raise TypeError("В ФИО присутствуют недопустывые символы")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or 14 > old or old > 120:
            raise TypeError(
                "Возраст должен соответствовать формату int и быть в диапазоне от 14 до 120"
            )

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError(
                "Возраст должен соответствовать формату int и быть в диапазоне от 14 до 120"
            )

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Формат должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Введен неверный формат данных")
        for j in s:
            if not j.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")
            
            
    @property
    def fio(self):
        return self.__fio
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight
    
    @property
    def passport(self, ps):
        return self.__passport
    
    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps
    
        

p = Person("Усков Степан Андреевич", 30, "6255 587612", 111.2)
print(p.__dict__)