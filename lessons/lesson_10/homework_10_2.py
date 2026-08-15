from abc import ABC, abstractmethod

# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур,
# та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
         return self.__side_a * self.__side_b

    def perimeter(self):
        return self.__side_a * 2 +  self.__side_b * 2

class Square(Shape):

    def __init__(self, side_a):
        self.__side_a = side_a

    def area(self):
         return self.__side_a * 4

    def perimeter(self):
        return self.__side_a **2

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
         return self.__radius**2 * 3.14

    def perimeter(self):
        return self.__radius * 2 * 3.14


rectangle = Rectangle(5, 8)
square = Square(6)
circle = Circle(4)

for shape in [rectangle, square, circle]:
    print(type(shape).__name__)
    print("area:", shape.area())
    print("perimeter:", shape.perimeter())
    print("="*20)