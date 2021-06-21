for number in range(1, 20):
    # number = int(input("Введите число от 0 до 20:"))
    word = "процент"
    number2_4="та"
    number5_20="ов"
    if number >= 2 and number <= 4:
        print(number, word + number2_4)
    elif number >= 5 and number <= 20:
        print(number, word + number5_20)
    else: print(number, word)