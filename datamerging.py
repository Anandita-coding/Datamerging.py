import csv
import pandas as pd

file1 = 'webscraping1.csv'
file2 = 'webscraping2.csv'

d1 = []
d2 = []

with open(file1) as f:
    reader = csv.reader(f)
    for i in reader:
        d1.append(i)

with open(file2) as f:
    reader2 = csv.reader(f)
    for j in reader2:
        d2.append(j)

h1 = d1[0]
h2 = d2[0]
h = h1+h2

rows1 = d1[1:]
rows2 = d2[1:]

rows = []

for i in rows1:
    rows.append(i)

for j in rows2:
    rows.append(j)

with open('mergedData.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(h)
    writer.writerows(rows)

