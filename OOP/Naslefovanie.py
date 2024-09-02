class Animals:
    def __init__(self, color=None, years=None, leg=4):
        self.color = color
        self.years = years
        self.leg = leg


class Cat(Animals):
    def __init__(self, color=None, years=None, leg=4, weight=0):
        super().__init__(color, years, leg)
        print("Инициализатор Сat")
        self.weight = weight

    def draw(self):
        return "Домашнии животные"


class Dog(Animals):
    def __init__(self, color=None, years=None, leg=4, breed=None):
        super().__init__(color, years, leg)
        print('Инициализатор Dog')
        self.breed= breed
        
    def draw(self):
        return 'Собаки лучшие друзья человекаrrrr'

c = Cat("black", 4, 4, 8)
d = Dog('brown', 3, 4,'Bulldog')

# print(c.draw())
# print(c.draw())
