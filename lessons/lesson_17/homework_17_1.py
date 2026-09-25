#   Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

gen = even_numbers_generator(10)
for item in gen:
    print(item)

print("="*25)
#   Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
#   0, 1, 1, 2, 3, 5, 8, 13...

def fibo_generator(n):
    fibo_list = [0, 1]
    i = len(fibo_list)
    last_element = fibo_list[-1]

    while last_element <= n:
        result = fibo_list[i-1] + fibo_list[i-2]
        i += 1
        if result > n:
            break
        fibo_list.append(result)
        last_element = fibo_list[-1]
        yield result


gen = fibo_generator(20)

result_list = [0, 1]
result_list.extend(list(gen))

print(result_list)