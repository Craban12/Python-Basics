# file = open('text.txt', 'r', encoding='utf-8')
result = []
with open('text.txt', 'r', encoding='utf-8') as f:
    x = f.readlines()
for z in x:
    # print(z)
    tup = ()
    part_1 = z[:z.find(' - -')]
    z = z.split('"')
    uz = z[1]
    y = z[1].find(' /')
    part_2 = uz[:y]
    part_3 = uz[y:]
    list_result = part_1, part_2, part_3
    result.append(list_result)
print(result)