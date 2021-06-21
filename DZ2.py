result_a = 0
result_b = 0

# Часть a
for i in range(1, 1000):
    if i % 2 != 0:
        i **= 3
        arg = []
        arg.append(i)
        length = len(str(i))
        numbers_sum = 0
        numbers = []
        while i > 0:
            numbers.append(i % 10)
            i //= 10
        while length > 0:
            length -= 1
            numbers_sum += numbers[length]
        if numbers_sum % 7 == 0:
            result_a += arg[0]
            # print(result_a) для проверки
print('Ответ задания a =', result_a)

#Часть b
for i in range(1, 1000):
    if i % 2 != 0:
        i **= 3
        i += 17
        arg = []
        arg.append(i)
        length = len(str(i))
        numbers_sum = 0
        numbers = []
        while i > 0:
            numbers.append(i % 10)
            i //= 10
        while length > 0:
            length -= 1
            numbers_sum += numbers[length]
        if numbers_sum % 7 == 0:
            result_b += arg[0]
            # print(result_a) для проверки
print('Ответ задания b =', result_b)