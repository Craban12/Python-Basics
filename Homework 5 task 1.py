
def odd_nums(number:int):
    x = (i for i in range(1, number + 1, 2))
    return x

odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
