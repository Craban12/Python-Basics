date = {}
with open('users.csv', 'r') as f, open("hobby.csv", 'r') as f_r:
    x = f.readlines()
    y = f_r.readlines()
    x = [line_x.rstrip() for line_x in x]
    y = [line_y.rstrip() for line_y in y]
    for k in range(len(x)):
        if k < len(y):
            date.setdefault(x[k], y[k])
        else:
            date.setdefault(x[k], None)
    with open("result.txt", "a+") as z:
        z.write(str(date))