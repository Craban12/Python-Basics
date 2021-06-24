date = [60.32, 6, 2.59, 84.2, 64.8, 984.1, 65, 99.9, 74.4, 69, 113.62]

#Часть A
for i in date:
    if type(i) == float:
        ruble = str(i).split('.')
        if int(ruble[1]) < 10:
            ruble[1] = "0" + ruble[1]
        print(f'{ruble[0]} руб {ruble[1]} коп')
    else:
        print(f'{i} руб 00 коп')
print("\n")

#Часть B
print(sorted(date))
print(date)
print("\n")

#Часть C
# print(sorted(date, reverse=True))  <----------можно же не создавая новый список!
date_reverse = sorted(date, reverse=True)
print(date_reverse)
print("\n")

#Часть D
print(sorted(date_reverse[:5]))