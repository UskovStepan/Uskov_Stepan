class Wheel:
    min_diametr = 10
    max_diametr = 22

    def __init__(self, diametr=min_diametr, width=None, release_date=None, price=0):
        self.verify_diametr(diametr)

        self.diametr = diametr
        self.width = width
        self.release_date = release_date
        self.price = price

    @classmethod
    def verify_diametr(cls, diametr):
        if diametr < cls.min_diametr or diametr > cls.max_diametr:
            raise TypeError("Диаметр колеса не может быть меньше 10 и больше 22")

    def info_wheel(self):
        return f"""
            - Диаметр: {self.diametr} 
            - Ширина: {self.width}
            - Дата выпуска: {self.release_date}
            - Цена колес: {self.price*4} рублей"""


class Car:
    def __init__(
        self,
        brand=None,
        year=None,
        engine=None,
        car_body=None,
        colour=None,
        price=0,
        wheel=Wheel(),
    ):
        self.verify_diametr_bmw(brand, wheel.diametr)
        self.verify_diametr_lada(brand, wheel.diametr)

        self.brand = brand
        self.year = year
        self.engine = engine
        self.car_body = car_body
        self.colour = colour
        self.price = price
        self.wheel = wheel

    @classmethod
    def verify_diametr_bmw(cls, brand, diametr):
        if brand == "BMW" and 17 > diametr:
            raise TypeError("У BMW диски не могут быть меньше 17")

    @classmethod
    def verify_diametr_lada(cls, brand, diametr):
        if brand == "Lada" and 15 > diametr:
            raise TypeError("У Lada диски не могут быть меньше 15")

    def get_car_info(self):
        return f"""
            Марка: {self.brand} 
            Год выпуска: {self.year} 
            Двигатель: {self.engine} 
            Тип кузова: {self.car_body}
            Цвет: {self.colour}
            Цена: {self.price}
            Колеса: {self.wheel.info_wheel()}
            Общая цена: {self.price + self.wheel.price*4}"""


my_car = Car(Wheel())
# "Volkswagen", "2011", "1.4 TSI", "Внедорожник", "Серый", 900000,
print(my_car.get_car_info())
