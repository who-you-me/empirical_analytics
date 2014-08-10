# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import csv

with open('crime.csv') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

crime = [int(row[1]) for row in rows[1:]]
unemp = [int(row[2]) for row in rows[1:]]

plt.plot(unemp, crime, '.')
plt.savefig('crime.png')
#plt.show()
