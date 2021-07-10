tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

result = ((tutors[k], klasses[k]) if k < len(klasses) else (tutors[k], None) for k in range(len(tutors)))

print(list(result))