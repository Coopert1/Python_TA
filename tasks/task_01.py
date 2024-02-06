from helpers.custom_exeption import WrongOperatorError
from tasks.task_05_decorators import logger
from datetime import datetime


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


def temp_converter(temp, initial_scale, to_scale):
    initial_scale = initial_scale.upper()
    to_scale = to_scale.upper()
    temp = float(temp)
    scales = ('F', 'C', 'K')
    if initial_scale not in scales or to_scale not in scales:
        raise ValueError('Enter correct temp scale: possible variants is: "C - Cesium, F - Fahrenheit, K - Kelvin')
    match initial_scale:
        case 'C':
            if to_scale == 'F':
                return round(temp * 1.8 + 32, 2)
            elif to_scale == 'K':
                return round(temp + 273.15, 2)
        case 'K':
            if to_scale == 'F':
                return round(temp * 1.8 - 459.67, 2)
            elif to_scale == 'C':
                return round(temp - 273.15, 2)
        case 'F':
            if to_scale == 'K':
                return round(temp / 1.8 + 459.67, 2)
            elif to_scale == 'C':
                return round((temp - 32.2) / 1.8, 2)


def greatest_number(a, b, c):
    return max([a, b, c])


def date_formats():
    time = datetime.now()
    # a) Current date and time
    print(time)
    # b) Current year
    print(time.year)
    # c) Month of year
    print(time.month)
    # d) Week number of the year
    print(time.strftime("%W"))
    # f) Day of year
    print(time.strftime("%-j"))
    # e) Weekday of the week
    print(time.weekday())


