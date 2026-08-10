# # Умова задачі
# Створити клас геометричної фігури «Ромб».
# Клас повинен мати наступні атрибути:
# * `side_a` — довжина сторони ромба;
# * `corner_a` — кут між сторонами;
# * `corner_b` — суміжний кут до `corner_a`.
# Необхідно реалізувати наступні вимоги:
# * значення `side_a` повинно бути більше `0`;
# * кути `corner_a` та `corner_b` повинні задовольняти умову: `corner_a + corner_b = 180`;
# * при заданому значенні одного кута значення другого кута обчислюється автоматично;
# * для встановлення та перевірки значень атрибутів використовується метод `__setattr__`.

# # Рішення
# * Під час створення об'єкта достатньо передати значення хоча б одного з кутів: `corner_a` або `corner_b`.
# Другий кут розраховується автоматично як `180 - значення заданого кута`.

# * Якщо передані обидва кути, пріоритет має значення, яке встановлюється останнім.
# Оскільки в `__init__` спочатку встановлюється `corner_a`, а потім `corner_b`,
# передане значення `corner_b` перераховує `corner_a` таким чином, щоб сума двох кутів завжди дорівнювала `180` градусів.

# * При подальшій зміні `corner_a` або `corner_b` значення другого кута також автоматично перераховується,
# тому умова `corner_a + corner_b = 180` завжди зберігається.

# * Значення сторони та кутів перевіряються у методі `__setattr__`.
# Сторона повинна бути більшою за `0`, а значення кута повинно знаходитися між `0` та `180` градусами.

# * Якщо під час створення об'єкта не передано значення ні `corner_a`, ні `corner_b`,
# створення об'єкта завершується помилкою `AttributeError`.

class Rhombus:
    def __init__(self, side_a: int | float, corner_a: int | float | None = None, corner_b: int | float | None = None):
        if corner_a is None and corner_b is None:
            raise AttributeError("corner_a or corner_b should be provided")
        self.side_a = side_a
        self.corner_a = corner_a
        self.corner_b = corner_b


    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, (int, float)):
                raise AttributeError(f"'{key}' should be a int or float")
            if value > 0:
                self.__dict__[key] = value
            else:
                raise AttributeError(f"'{key}' should be more than 0")
        elif key == 'corner_a':
            if value is None:
                return
            if not isinstance(value, (int, float)):
                raise AttributeError(f"'{key}' should be a int or float or None")
            if 0 < value < 180:
                self.__dict__[key] = value
                self.__dict__['corner_b'] = 180 - value
            else:
                raise AttributeError(f"'{key}' should be between 0 and 180")

        elif key == 'corner_b':
            if value is None:
                return
            if not isinstance(value, (int, float)):
                raise AttributeError(f"'{key}' should be a int or float or None")
            if 0 < value < 180:
                self.__dict__[key] = value
                self.__dict__['corner_a'] = 180 - value
            else:
                raise AttributeError(f"'{key}' should be between 0 and 180")


    def __str__(self):
        return f"Rhombus('side_a': {self.side_a}, 'corner_a': {self.corner_a}, 'corner_b': {self.corner_b})"

    def __repr__(self):
        return f"Rhombus({self.side_a}, {self.corner_a}, {self.corner_b})"


shape1 = Rhombus(side_a=10, corner_a=30.30)
print(shape1)

shape2 = Rhombus(side_a=15.7, corner_b=45)
print(shape2)

shape3 = Rhombus(side_a=20, corner_a=30, corner_b=80.69)
print(shape3)

shape4 = Rhombus(side_a=25, corner_a=90)
shape4.corner_a = 15
print(shape4)

shape5 = Rhombus(side_a=12.5, corner_b=60)
shape5.corner_b = 100
print(shape5)

shape6 = Rhombus(side_a=10)