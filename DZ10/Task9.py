
row = []
row1 = []
n = int(input('enter a number row  '))
for i in range(n):
    for k in range(i + 1):
        if k == 0 or k == i:
            row1.append(1)
        else:
            row1.append(row[k - 1] + row[k])
    row = row1
    print(row1)
    row1 = []

