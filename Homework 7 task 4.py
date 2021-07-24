import os

all_star = {}
SOMEBODY = os.path.join(os.getcwd(), "some_data")

for told in os.scandir(SOMEBODY):
    stop = 1
    x = 1
    while stop > 0:
        x = x +1
        data = told.stat().st_size
        stop = data // (10**x)
        if stop == 0:
            hpp = 10**x
            all_star.setdefault(hpp, 0)
            all_star[hpp] = all_star[hpp] + 1
print(all_star)