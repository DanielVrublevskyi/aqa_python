def get_sum_from_tuple(tpl):
    res = []
    for item in tpl:
        sum_ = 0
        try:
            lst = item.split(',')
            for i in lst:
                sum_ += int(i)
        except ValueError as e:
            return e
        else:
            res.append(sum_)
    return res


def get_multiplication_table(number, max_value):
    multiplier = 1
    res = []
    while multiplier <= max_value:
        result = number * multiplier
        if result > max_value:
            break
        res.append(result)
        multiplier += 1
    return res


def sum_of_2_num(a: int | float, b: int | float):
    return a + b


def arithmetic_mean(*args: int | float):
    return sum(args) / len(args)


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
