import homeworks
import assertpy

def test_sum_from_tuple():
    tuple_ = ["1,2,3,4", "1,2,3,4,50", "1,2,3"]
    lst = homeworks.get_sum_from_tuple(tuple_)
    exp_len = len(tuple_)
    exp_first_el = 10

    assert len(lst) == exp_len, f"list length should be {exp_len}"
    assert lst[0] == exp_first_el, f"result from first element should be {exp_first_el}"

def test_multiplication_table():
    value = 27
    number = 5
    lst = homeworks.get_multiplication_table(number, value)
    exp_len = value//number

    assert len(lst) == exp_len, f"list length should be {exp_len}"
    with assertpy.soft_assertions():
        for i in range(0, len(lst)):
            assertpy.assert_that((lst[i]), f"{number} multiply {i+1} should be "
                                 ).is_equal_to(number*(i+1))


def test_sum_of_2_num():
    a = 3
    b = 2
    sum_ = homeworks.sum_of_2_num(a, b)

    assert sum_ == (a + b), f"sum of two numbers should be {sum_}"
    assert a == sum_- b, f"a should be {sum_ - b}"

def test_arithmetic_mean():
    nums_list = [1,2,3,4,5]
    av_number = homeworks.arithmetic_mean(*nums_list)

    assertpy.assert_that(av_number, f"{av_number} should be float").is_instance_of(float)
    assertpy.assert_that(av_number, f"{av_number} should be 0 or greater").is_greater_than_or_equal_to(0)

def test_calculate_tax():
    user_income = 22000
    exp_percentage = 15
    tax_amount = homeworks.calculate_tax(user_income)
    act_percentage = tax_amount / user_income * 100

    assert tax_amount < user_income, f"tax_amount should be less than {user_income}"
    assert act_percentage == exp_percentage, f"act_percentage should be equal to {exp_percentage}"
