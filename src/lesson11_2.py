# Задача 1
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми, и
# округляет их до целых, если это не так.
import time
from os.path import split


def check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result
    return wrapper

@check_integers
def get_float():
    return 3.7

print(get_float())  # Вывод: 4

@check_integers
def get_list():
    return [1.2, 3.7, 5]

print(get_list())  # Вывод: [1, 4, 5]

@check_integers
def get_tuple():
    return 1.5, 2.3, "hello"

print(get_tuple())  # Вывод: (2, 2, "hello")


# Задача 2
# Напишите декоратор, который повторно вызывает декорируемую функцию три раза. Каждый раз через три секунды, если произошла ошибка.

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except:
                time.sleep(3)
        raise Exception('Function call failed after multiple retries.')
    return wrapper


# Задача 3
# Напишите декоратор, который позволяет возвращать элементы декорируемой функции по одному через
# yield
# , если эта функция возвращает список или кортеж.

def elements(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) in (list, tuple):
            for i in result:
                yield i
        else:
            yield result
    return wrapper


@elements
def get_elements():
    return [1, 2, 3]


print(type(['1', 'qs', 're']))


# Задача 4
# Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, в котором каждое слово
# сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.


def shortening_words(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        list_word = result.split(' ')
        slice_word = [x[:8] + '.' if len(x) > 8 else x for x in list_word ]
        return ' '.join(slice_word)

    return wrapper

@shortening_words
def check_word():
    return ('Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст, в '
            'котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.')

print(check_word())




