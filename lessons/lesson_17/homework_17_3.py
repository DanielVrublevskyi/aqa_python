from core.utils.logger import cli_logger
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def decorator(func):

    def wrapper(*args, **kwargs):
        cli_logger.info(f"args: {args}")
        cli_logger.info(f"kwargs: {kwargs}")

        result = func(*args, **kwargs)

        cli_logger.info(f"result: {result}")

        return result

    return wrapper


@decorator
def av_number(*numbers):
    return sum(numbers) / len(numbers)


av_number(10, 20, 30)


cli_logger.warning("\n"*3)
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def handle_exceptions(func):

    def wrapper(*args, **kwargs):
        try:
            cli_logger.info(f"args: {args}")
            result =  func(*args, **kwargs)

            cli_logger.info(f"result: {result}")
        except TypeError as error:
            cli_logger.error(error)

        except ValueError as error:
            cli_logger.error(error)

    return wrapper


@handle_exceptions
def check_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age

check_age("1")
check_age(-1)
check_age(5)