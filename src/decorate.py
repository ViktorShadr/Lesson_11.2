# Задача 1
# Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми, и
# округляет их до целых, если это не так. Декоратор должен принимать параметр
# precision
# , который указывает, до скольких цифр после запятой округлять числа.

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



