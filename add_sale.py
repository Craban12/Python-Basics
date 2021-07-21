import csv
import sys

x = [sys.argv[1],]
with open('bakery.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(x)