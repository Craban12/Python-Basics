def thesaurus(name: str):
    name = name.split(', ')
    answer_1 = {}
    for i in name:
        answer_1.setdefault(str(i[0]), [])
    for x in name:
        answer_1[x[0]].append(x)
    return answer_1

print(thesaurus(input('Введите данные без ковычек, через запитую:')))