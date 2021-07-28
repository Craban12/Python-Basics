def type_logger(func):
    def wrapper(*args):
        res = func(*args)
        print(type(res))
    return wrapper()


@type_logger
def calc_cube(x):
    result = x ** 3
    return result


print(calc_cube(int(input())))
