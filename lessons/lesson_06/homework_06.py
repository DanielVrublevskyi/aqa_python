#task 6.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
text = input("Input string: ")
chars_set = set(text)
print(len(chars_set) > 10)

#task 6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
required_letter = 'h'
def get_string_from_input():
    return input(f"Input word with '{required_letter}': ")
word_with_req_letter = get_string_from_input()

while required_letter not in word_with_req_letter.lower():
    print(f"'{required_letter}' not found in {word_with_req_letter}")
    word_with_req_letter = get_string_from_input()

#task 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) == str:
        lst2.append(i)
print(lst2)

#task 6.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
lst1 = [1,2,3,4,5,6,7,8,10,22]
sum_even_num = 0
for i in lst1:
    if i%2 == 0:
        sum_even_num += i
print(sum_even_num)