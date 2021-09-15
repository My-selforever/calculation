import csv
import os

os.system('cls')

f = open('merge2.csv')

r = csv.reader(f)

data = []

for row in r:
    data.append(row)

header = data[0]
rows = data[1:]

for row in range(1, 51, 2):
    rows[row][3] = float(rows[row][3])*1.989e+30
    rows[row][4] = float(rows[row][4])*6.957e+8

# for index,row in enumerate(rows):
#    if(index%2==1 and row[1]!= "Sun"):
#        rows.remove(row)


# the above code is not working as expected so i tried by adding the "Sun" part. Then is is removing sirius.


print(len(rows), rows[1:4])


with open('filtered.csv', 'w') as ff:
    fr = csv.writer(ff)
    fr.writerow(header)
    fr.writerows(rows)
