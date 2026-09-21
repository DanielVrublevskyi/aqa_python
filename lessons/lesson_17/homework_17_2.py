#   Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:
    def __init__(self, items):
        self.items = items
        self.index = len(items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.items[self.index]
        self.index -= 1
        return value

numbers = [10, 20, 30, 40]

reverse_iterator = ReverseIterator(numbers)

for number in reverse_iterator:
    print(number)

print("="*25)
#   Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            result = self.current
            self.current += 1

            if result % 2 == 0:
                return result

        raise StopIteration


even_numbers_iterator = EvenNumbersIterator(10)
for number in even_numbers_iterator:
    print(number)