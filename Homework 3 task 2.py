def num_translate(number: str):
    dictionary = {'one':"один", 'two':"два", 'three':"три", 'four':"четыре", 'five':"пять", 'six':"шесть", 'seven':"семь", "eight":"восемь", 'nine':"девять", 'ten':"десять"}
    if number.istitle() is True:
        number = number.lower()
        number_lower = str(dictionary.get(number))
        return number_lower.capitalize()
    else:
        return dictionary.get(number)


print(num_translate(input()))