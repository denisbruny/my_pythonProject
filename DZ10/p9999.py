lp = []
n = int(input('enter number'))

for i in range(n):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != 1:
            row[j] = lp[i - 1][j - 1] + lp[i - 1][j]

    lp.append(row)

for rw in lp:
    print(rw)
