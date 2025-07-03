# Задача 1
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми, и
# округляет их до целых, если это не так. Декоратор должен принимать параметр
# precision
# , который указывает, до скольких цифр после запятой округлять числа.
from datetime import time
from functools import wraps


def decorator_integer(precision):
    def check_int(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in result]
                # Возвращаем тот же тип, что и исходный (list или tuple)
                return type(result)(rounded)
            else:
                return result
        return wrapper
    return check_int

@decorator_integer(5)
def example_func(value):
    return value

print(example_func(5.343545454532))


# Задача 2
# Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время,
# если произошла ошибка. Параметры, передаваемые в декоратор, обязательно должны быть именованными.


def retry(*, retries=3, delay=3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception():
                    time.sleep(delay)
            raise Exception('Function call failed after multiple retries.')
        return inner
    return wrapper


# Задача 3
# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, в котором каждое слово
# сокращено до определенной длины. Если слово было сокращено, в конце слова ставится переданный символ. Количество
# символов в слове и знак в конце сокращенного слова — параметры декоратора, причем символ обязательно должен
# передаваться как именованный аргумент.

def formate_txt(*, max_length, symbol):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            list_word = result.split(' ')
            return ' '.join([x[:max_length] + f'{symbol}' if len(x) > max_length else x for x in list_word])
        return inner
    return wrapper


@formate_txt(max_length=3, symbol="-")
def clean(value):
    return value

print(clean('Если слово было сокращено, в конце слова ставится переданный символ. Количество '
            'символов в слове и знак в конце сокращенного слова — параметры декоратора'))
