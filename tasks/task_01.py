from helpers.custom_exeption import WrongOperatorError
from tasks.task_05_decorators import logger


def to_minutes(hours: int) -> int:
    return hours * 60


def to_hours(minutes: int) -> float:
    return round(minutes / 60, 4)


def is_whole_div(a: int, b: int) -> bool:
    return a % b == 0


@logger
def greeting():
    name = input('What is your name? ')
    age = input('How old are you? ')
    city = input('Where do you live? ')
    print(f'Hello {name},\nYour age is {age},\nYou live in{city}')


@logger
def calculator(a=None, b=None, operator=None):
    while True:
        if a is None:
            a = input('Enter a value for a ')
        if b is None:
            b = input('Enter a value for b ')
        if operator is None:
            operator = input('Choose the operator from list: "+", "-", "*", "/", "//", "%" ')
        if operator not in ["+", "-", "*", "/", "//", "%"]:
            # Here I also can use except to handle this error, but in testing purposes I raise an WrongOperatorError
            raise WrongOperatorError
        try:
            return eval(f'{a} {operator} {b}')
        except ZeroDivisionError:
            print('Error: Enter non-zero values for b if you want to do division')
            continue
        except ValueError:
            print('Error: Please enter valid numeric values for a and b.')
            continue
        finally:
            a, b, operator = None, None, None
