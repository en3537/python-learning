m = [[0 for i in range(5)] for j in range(5)]
has_zero=0

while True:
    inxy = input("x,y:")

    if inxy == '':
        break

    xy = inxy.split(',')
    x = int(xy[0])
    y = int(xy[1])

    m[x][y] = 1

print("=============")

for i in range(5):
    for j in range(5):
        print(m[i][j], end=" ")
    print()

# [],[] = [row],[column]

print("=== All Zero Row ===") # 橫列
for a in range(5):
    for b in range(5):
        if m[a][b] != 0:
            break
    else:
        has_zero=1
        print(f"Row {a}")

if has_zero == 0:
    print("None")

has_zero=0

print("=== All Zero Column ===") # 直行

for d in range(5):
    for e in range(5):
        if m[e][d] != 0:
            break
    else:
        has_zero=1
        print(f"Column {d}")

if has_zero == 0:
    print("None")