# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    multiplier = 1

    while multiplier <= 25:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1


multiplication_table(25)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_of_2_num(a: int | float, b: int | float):
    return a + b


print(sum_of_2_num(34, 2.5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def arithmetic_mean(*args: int | float):
    return sum(args) / len(args)


print(arithmetic_mean(1, 2, 3, 4, 5))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_str(s: str):
    return s[::-1]


print(reverse_str("Hello"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_str(s: str):
    return max(len(s) for s in s)


print(longest_str("Hello"))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    str1.find(str2)
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
"""
Написати програму, яка розраховує оподаткування на основі річного доходу користувача.

Отримайте річний дохід користувача.
Ми припускаємо, що користувач ЗАВЖДИ буде вводити нормальне число (≥0)
На основі введеного доходу розрахуйте податок за такими умовами:
Якщо дохід менше 10 000 грн, податок складає 10% від доходу.
Якщо дохід від 10 000 до 50 000 грн, податок складає 15% від доходу.
Якщо дохід більше 50 000 грн, податок складає 20% від доходу.
Запишіть результат у змінну tax_amount.
"""


def calculate_tax(user_income):
    tax_amount = 0
    income_10 = 10000
    income_50 = 50000
    if user_income < income_10:
        tax_amount = user_income * 0.1
    elif user_income > income_10 and user_income < income_50:
        tax_amount = user_income * 0.15
    elif user_income > income_50:
        tax_amount = user_income * 0.20
    return tax_amount


print(calculate_tax(5000))
print(calculate_tax(15000))
print(calculate_tax(150000))
# task 8
"""
Ваша задача - написати функцію, яка визначає, чи є введене користувачем число простим чи складеним. 
Зазначте, що користувач завжди буде вводити цілі числа.
Простим вважаємо число, яке має 2 дільники - одиницю і саме це число
Ваш код повинен використовувати цикл та умови для визначення простоти числа.
Запишіть результат в змінну result.
"""


def is_prime_number(number):
    result = True
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            result = False
            break
        divisor += 1
    return result


print(is_prime_number(2))
print(is_prime_number(3))
print(is_prime_number(6))
print(is_prime_number(10))
# task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def price(month_price, period):
    return month_price * period

print(price(1179, 18))
# task 10

"""
Ви тестуєте програму, яка працює з конфігураційними файлами,
і вам потрібно здійснити тестування різних варіантів конфігурацій.
Задача:
1. Доробіть функцію change_params(старе_значення, нове_значення)
  яка приймає на вхід старе значення параметра та нове значення, яке треба вставити.
2. Функція повинна замінити всі входження старого значення на нове і повернути замінені дані.
"""
def change_params(old_value:str, new_value:str):
    filetext = """\
    screen_size = 800x600
    paralel_processes = 10
    db_conection = localhost:5432"""
    filetext = filetext.replace(old_value, new_value)

    return filetext

print(change_params('800x600', '123'))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
