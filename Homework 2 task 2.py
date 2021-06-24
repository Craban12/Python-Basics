data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for x, i in enumerate(data):
    if i.isdigit() or i[1:].isdigit():
        if len(i)<2:
            i = "0" + i
        elif i[1:].isdigit() and not i.isdigit():
            i = i[0] + '0' + i[1]
        number = data.pop(x)
        data.insert(x, '"')
        data.insert(x, i)
length = len(data)
while length > 0:
    length -=1
    number = data[length]
    if data[length].isdigit():
        data.insert(length, '"')
    elif number[1:].isdigit():
        data.insert(length, '"')
print(data)
print(' '.join(data))