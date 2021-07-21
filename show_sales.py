import csv
import sys

try:
    date = int(sys.argv[1])
    with open("bakery.csv", 'r') as f:
        x = f.readlines()
        print(x[date])
except IndexError:
    with open('bakery.csv', newline='') as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            print(row)