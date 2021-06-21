duration = int(input("Введите количество секунд:"))
if duration >=60:
    minutes = duration//60
    seconds = duration%60
    if minutes >= 60:
        hours = minutes//60
        minutes = minutes%60
        if hours >= 24:
            days = hours//24
            hours = hours%24
            print(f"{days} дн {hours} час {minutes} мин {seconds} сек")
        else: print(f"{hours} час {minutes} мин {seconds} сек")
    else: print(f"{minutes} мин {seconds} сек")
else: print(f"{duration} сек")